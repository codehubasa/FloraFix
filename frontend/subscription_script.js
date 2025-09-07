// Handle subscription button
document.addEventListener("DOMContentLoaded", () => {
  const subscribeBtn = document.querySelector("button");

  if (subscribeBtn) {
    subscribeBtn.addEventListener("click", () => {
      alert("✅ Redirecting to payment page...");
      window.location.href = "payment.html";
    });
  }
});