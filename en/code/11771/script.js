// Change the main title
document.getElementById("clubTitle").innerText = "🎮 Gaming Club";

// Change the meeting information
document.getElementById("meetingInfo").innerText = "Next meeting: checking for update";

// Add a news update after a short delay
setTimeout(() => {
  document.getElementById("latestNews").innerText = "Remember your controller!";
}, 1000);
