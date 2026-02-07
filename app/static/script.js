document.getElementById('view-status-btn').addEventListener('click', () => {
    document.getElementById('home-page').classList.add('hidden');
    document.getElementById('status-page').classList.remove('hidden');
    simulateLogs();
});

document.getElementById('back-btn').addEventListener('click', () => {
    document.getElementById('status-page').classList.add('hidden');
    document.getElementById('home-page').classList.remove('hidden');
});

function simulateLogs() {
    const logs = document.getElementById('dynamic-logs');
    const messages = [
        "> Security scan complete: 0 vulnerabilities.",
        "> Uploading artifacts to S3...",
        "> Triggering production deployment..."
    ];
    
    messages.forEach((msg, i) => {
        setTimeout(() => {
            const p = document.createElement('p');
            p.textContent = msg;
            p.style.color = "#8b949e";
            logs.appendChild(p);
        }, (i + 1) * 1500);
    });
}
