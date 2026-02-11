function openTab(tabName) {
    let tabs = document.getElementsByClassName("tab-content");
    for (let i = 0; i < tabs.length; i++) {
        tabs[i].style.display = "none";
    }
    document.getElementById(tabName).style.display = "block";
}

// Load dashboard by default
document.addEventListener("DOMContentLoaded", function () {
    openTab('dashboard');
    fetchMetrics();
});

function fetchMetrics() {
    fetch('/metrics')
        .then(response => response.json())
        .then(data => {
            document.getElementById("metrics").innerHTML = `
                CI Status: ${data.ci_status} <br>
                Build Success Rate: ${data.build_success_rate} <br>
                Active Pods: ${data.active_pods} <br>
                CPU Usage: ${data.cpu_usage} <br>
                Memory Usage: ${data.memory_usage} <br>
                Security Vulnerabilities: ${data.security_vulnerabilities}
            `;
        });
}
