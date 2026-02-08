function showStage(message) {
  alert(message);
}

function openPanel() {
  document.getElementById("panel").classList.add("open");
  loadData();
}

function closePanel() {
  document.getElementById("panel").classList.remove("open");
}

async function loadData() {
  const info = await fetch("/info").then(r => r.json());
  const health = await fetch("/health").then(r => r.json());

  document.getElementById("status").innerText = health.status;
  document.getElementById("environment").innerText = info.environment;
  document.getElementById("version").innerText = info.version;
  document.getElementById("build").innerText = info.build_number;
  document.getElementById("commit").innerText = info.git_commit;
}
