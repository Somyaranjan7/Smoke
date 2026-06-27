function confirmFix() {

    return confirm(
        "Are you sure you want to block this port?"
    );

}


function confirmLogout() {

    return confirm(
        "Are you sure you want to logout?"
    );

}


// ===============================
// Scan Loading Animation
// ===============================

function startScan() {

    const overlay = document.getElementById(
        "scanOverlay"
    );

    overlay.style.display = "flex";

    const bar = document.getElementById(
        "progressBar"
    );

    const percent = document.getElementById(
        "progressPercent"
    );

    const text = document.getElementById(
        "progressText"
    );

    const messages = [

        "Initializing scanner...",

        "Resolving target...",

        "Checking host availability...",

        "Scanning open ports...",

        "Detecting services...",

        "Analyzing vulnerabilities...",

        "Generating reports..."

    ];

    let progress = 0;

    let messageIndex = 0;

    const timer = setInterval(function () {

        // Fast at first, slower later
        if (progress < 30) {

            progress += Math.random() * 6;

        }

        else if (progress < 60) {

            progress += Math.random() * 3;

        }

        else if (progress < 85) {

            progress += Math.random() * 1.8;

        }

        else if (progress < 99) {

            progress += Math.random() * 0.5;

        }

        if (progress > 99) {

            progress = 99;

        }

        bar.style.width = progress + "%";

        percent.innerHTML =
            Math.floor(progress) + "%";

        const stage = Math.floor(progress / 15);

        if (
            stage < messages.length &&
            stage !== messageIndex
        ) {

            messageIndex = stage;

            text.innerHTML =
                messages[stage];

        }

    }, 250);

    return true;

}