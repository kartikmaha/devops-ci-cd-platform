function openDashboard() {
  document.getElementById("dashboard").style.display = "block";
  loadInfo();
}

function closeDashboard() {
  document.getElementById("dashboard").style.display = "none";
}

async function loadInfo() {
  const info = await fetch("/info").then(r => r.json());
  const health = await fetch("/health").then(r => r.json());

  document.getElementById("environment").innerText = info.environment;
  document.getElementById("version").innerText = info.version;
  document.getElementById("build").innerText = info.build_number;

  const statusEl = document.getElementById("status");
  statusEl.innerText = health.status;
  statusEl.className = "badge up";
}
