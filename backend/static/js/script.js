document.addEventListener('DOMContentLoaded', () => {
    const recordButton = document.getElementById('record-btn');
    const statusDiv = document.getElementById('status');
    const micIcon = document.getElementById('mic-icon');
    const stopIcon = document.getElementById('stop-icon');
    const spinner = document.getElementById('spinner');
    const audioPlayer = document.getElementById('audio-player');

    let isRecording = false;
    let mediaRecorder;
    let audioChunks = [];
    let sessionId = null;

    const updateStatus = (text, showSpinner = false) => {
        statusDiv.textContent = text;
        spinner.style.display = showSpinner ? 'block' : 'none';
    };

    const toggleRecordingUI = (isRecordingNow) => {
        micIcon.style.display = isRecordingNow ? 'none' : 'block';
        stopIcon.style.display = isRecordingNow ? 'block' : 'none';
        recordButton.classList.toggle('recording', isRecordingNow);
    };

    // --- Session Management ---
    const getSessionId = () => {
        const params = new URLSearchParams(window.location.search);
        let sid = params.get('session_id');
        if (!sid) {
            sid = crypto.randomUUID();
            window.history.replaceState({}, '', `${window.location.pathname}?session_id=${sid}`);
        }
        return sid;
    };

    sessionId = getSessionId();
    updateStatus('Press the button and start talking');

    // --- Audio Recording Logic ---
    const startRecording = async () => {
        if (isRecording) return;
        
        try {
            const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
            isRecording = true;
            audioChunks = [];
            toggleRecordingUI(true);
            updateStatus('Listening...');

            mediaRecorder = new MediaRecorder(stream);
            mediaRecorder.ondataavailable = (event) => {
                audioChunks.push(event.data);
            };

            mediaRecorder.onstop = async () => {
                const audioBlob = new Blob(audioChunks, { type: 'audio/webm' });
                stream.getTracks().forEach(track => track.stop());
                await sendAudioToServer(audioBlob);
            };
            
            mediaRecorder.start();
        } catch (error) {
            console.error('Error accessing microphone:', error);
            updateStatus('Could not access microphone.');
            toggleRecordingUI(false);
        }
    };

    const stopRecording = () => {
        if (mediaRecorder && mediaRecorder.state === 'recording') {
            mediaRecorder.stop();
            isRecording = false;
            toggleRecordingUI(false);
            updateStatus('Thinking...', true);
        }
    };

    // --- Server Communication ---
    const sendAudioToServer = async (audioBlob) => {
        const formData = new FormData();
        formData.append('audio', audioBlob, 'user_recording.webm');
        
        try {
            const response = await fetch(`/api/agent/chat/${sessionId}`, {
                method: 'POST',
                body: formData
            });

            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.error || 'Server error');
            }

            audioPlayer.src = data.audioUrl;
            audioPlayer.play();
            updateStatus('Here is my response...');

        } catch (error) {
            console.error('Error sending audio to server:', error);
            updateStatus('Sorry, an error occurred.');
        }
    };

    audioPlayer.onended = () => {
        updateStatus('Press the button and start talking');
    };

    recordButton.addEventListener('click', () => {
        if (!isRecording) {
            startRecording();
        } else {
            stopRecording();
        }
    });
});

