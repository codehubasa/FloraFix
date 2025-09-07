document.addEventListener("DOMContentLoaded", () => {
  const plantInput = document.getElementById("plantInput");
  const previewSection = document.getElementById("previewSection");
  const previewImage = document.getElementById("previewImage");
  const diagnoseForm = document.getElementById("diagnoseForm");
  const resultSection = document.getElementById("resultSection");
  const resultText = document.getElementById("resultText");

  // ✅ Show preview when a file is selected
  if (plantInput) {
    plantInput.addEventListener("change", (event) => {
      const file = event.target.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = (e) => {
          previewImage.src = e.target.result;
          previewSection.classList.remove("hidden"); // show preview
        };
        reader.readAsDataURL(file);
      } else {
        previewSection.classList.add("hidden"); // hide if no file
      }
    });
  }

  // ✅ Show "Processing..." when form is submitted
  if (diagnoseForm) {
    diagnoseForm.addEventListener("submit", () => {
      if (resultSection && resultText) {
        resultSection.classList.remove("hidden");
        resultText.textContent = "Processing your plant image...";
      }
    });
  }
});
