// Preview uploaded image
const plantInput = document.getElementById("plantInput");
const previewImg = document.getElementById("previewImg");
const diagnoseBtn = document.getElementById("diagnoseBtn");
const resultText = document.getElementById("resultText");

plantInput.addEventListener("change", function() {
  const file = this.files[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = function(e) {
      previewImg.src = e.target.result;
      previewImg.style.display = "block";
    };
    reader.readAsDataURL(file);
  }
});

// Real diagnosis API call
diagnoseBtn.addEventListener("click", async () => {
  const file = plantInput.files[0];
  if (!file) {
    resultText.textContent = "⚠️ Please upload an image first.";
    return;
  }

  // Show loading state
  resultText.textContent = "⏳ Analyzing image...";
  diagnoseBtn.disabled = true;

  const formData = new FormData();
  formData.append("plantImage", file);

  try {
    const response = await fetch("http://127.0.0.1:8000/diagnose/api/predict/", {
      method: "POST",
      body: formData,
    });

    const data = await response.json();
    
    if (response.ok && data.success) {
      resultText.innerHTML = `<strong>Disease:</strong> ${data.result} <br><strong>Confidence:</strong> ${data.confidence}%`;
    } else {
      // The server successfully replied, but with an error (like model shape issue)
      resultText.textContent = `❌ Server Error: ${data.error || "Unknown error occurred"}`;
    }
  } catch (error) {
    console.error(error);
    resultText.textContent = "❌ Failed to connect to server! Is your Django server running (python manage.py runserver)?";
  } finally {
    diagnoseBtn.disabled = false;
    resultText.classList.add("pop-result");

    // Remove animation after it plays
    setTimeout(() => {
      resultText.classList.remove("pop-result");
    }, 800);
  }
});

// Popup animation
const style = document.createElement("style");
style.innerHTML = `
.pop-result {
  animation: pop 0.8s ease;
}
@keyframes pop {
  0% { transform: scale(0.7); opacity: 0; }
  50% { transform: scale(1.2); opacity: 1; }
  100% { transform: scale(1); }
}`;
document.head.appendChild(style);
