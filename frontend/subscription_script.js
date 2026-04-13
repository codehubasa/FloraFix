// Handle subscription button or chatbot
document.addEventListener("DOMContentLoaded", () => {
  const urlParams = new URLSearchParams(window.location.search);
  const forum = urlParams.get('forum');

  if (forum) {
    // Change to chatbot mode
    document.querySelector('h2').textContent = getForumTitle(forum) + ' Chatbot';
    document.querySelector('.w-full.max-w-md').innerHTML = getChatbotHTML(forum);
  } else {
    // Subscription mode
    const subscribeBtn = document.querySelector("button");
    if (subscribeBtn) {
      subscribeBtn.addEventListener("click", () => {
        alert("✅ Redirecting to payment page...");
        window.location.href = "payment.html";
      });
    }
  }
});

function getForumTitle(forum) {
  switch (forum) {
    case 'disease': return '🌿 Plant Disease Identification';
    case 'organic': return '🌾 Organic Farming Practices';
    case 'urban': return '🌸 Urban Gardening';
    default: return 'Chatbot';
  }
}

function getChatbotHTML(forum) {
  return `
    <div class="bg-white/10 border border-white/20 rounded-2xl p-6 text-center">
      <p class="text-gray-300 mb-4">Chat with our AI assistant for ${getForumTitle(forum).toLowerCase()}.</p>
      <div class="bg-slate-800 p-4 rounded-lg mb-4 h-64 overflow-y-auto">
        <p class="text-left text-gray-300">Bot: Hello! How can I help you with ${getForumTitle(forum).toLowerCase()}?</p>
      </div>
      <input type="text" placeholder="Type your message..." class="w-full p-2 bg-slate-700 rounded-lg text-white mb-2">
      <button class="px-4 py-2 bg-green-500 text-black font-bold rounded-xl">Send</button>
    </div>
  `;
}