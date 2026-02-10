fetch("/info")
  .then(response => response.json())
  .then(data => {
    document.getElementById("env").innerText = data.environment;
    document.getElementById("build").innerText = data.build;
    document.getElementById("time").innerText = data.time;
  })
  .catch(() => {
    document.getElementById("env").innerText = "Unavailable";
    document.getElementById("build").innerText = "Unavailable";
    document.getElementById("time").innerText = "Unavailable";
  });
