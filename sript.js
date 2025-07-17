// Select the mic button and chat area
const micButton = document.querySelector('.mic-button');
const chatArea = document.getElementById('agent1-chat');

// Check if SpeechRecognition is supported
const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
const recognition = new SpeechRecognition();

recognition.interimResults = false;
recognition.lang = 'en-US';

// When mic button is clicked
micButton.addEventListener('click', () => {
  recognition.start();
});

// When speech is successfully recognized
recognition.addEventListener('result', (e) => {
  const transcript = e.results[0][0].transcript;

  // Create user message bubble
  const userMessage = document.createElement('div');
  userMessage.className = 'message user';
  userMessage.textContent = transcript;
  chatArea.appendChild(userMessage);

  // Show typing animation
  const typing = document.createElement('div');
  typing.className = 'message agent typing';
  typing.innerHTML = `<span class="dot"></span><span class="dot"></span><span class="dot"></span>`;
  chatArea.appendChild(typing);

  // Scroll to bottom
  chatArea.scrollTop = chatArea.scrollHeight;

  // Simulate assistant reply
  setTimeout(() => {
    chatArea.removeChild(typing);

    const botReply = document.createElement('div');
    botReply.className = 'message agent';
    botReply.textContent = "Got it! Help is on the way 🚑";

    chatArea.appendChild(botReply);
    chatArea.scrollTop = chatArea.scrollHeight;
  }, 1200);
});

// If there's an error
recognition.addEventListener('error', (e) => {
  const errorMsg = document.createElement('div');
  errorMsg.className = 'message agent';
  errorMsg.textContent = "Sorry, I couldn't hear you. Please try again.";
  chatArea.appendChild(errorMsg);
});
