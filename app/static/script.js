async function fetchInfo() {
  const infoRes = await fetch("/info");
  const healthRes = await fetch("/health");

  const info = await infoRes.json();
  const health = await healthRes.json();

  // Environment
  const env = info.environment || "dev";
  document.getElementById("environment").innerText = env.toUpperCase();
  document.getElementById("env-banner").className = env;

  // Status
  const statusEl = document.getElementById("status");
  if (health.status === "UP") {
    statusEl.innerText = "UP";
    statusEl.className = "badge up";
  } else {
    statusEl.innerText = "DOWN";
    statusEl.className = "badge down";
  }

  document.getElementById("version").innerText = info.version;
  document.getElementById("build").innerText = info.build_number;
  document.getElementById("commit").innerText = info.git_commit;
  document.getElementById("deployedAt").innerText =
    timeAgo(new Date(info.deployed_at));
}

// Human readable time
function timeAgo(date) {
  const seconds = Math.floor((new Date() - date) / 1000);
  const minutes = Math.floor(seconds / 60);
  if (minutes < 1) return "Just now";
  if (minutes < 60) return `${minutes} minutes ago`;
  return `${Math.floor(minutes / 60)} hours ago`;
}

// Accordion
document.addEventListener("click", (e) => {
  if (e.target.classList.contains("accordion-btn")) {
    const content = e.target.nextElementSibling;
    content.style.display =
      content.style.display === "block" ? "none" : "block";
  }
});

// Auto refresh every 30s
fetchInfo();
setInterval(fetchInfo, 30000);
