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


// ======================================
// Scan Loading Animation
// ======================================

function startScan() {

    if (!validateTarget()) {

        return false;

    }

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

        "Resolving hostname...",

        "Checking target availability...",

        "Scanning open ports...",

        "Detecting services...",

        "Enumerating versions...",

        "Analyzing vulnerabilities...",

        "Generating reports..."

    ];

    let progress = 0;

    let stage = 0;

    setInterval(function () {

        // Much slower and smoother

        if (progress < 20) {

            progress += 1.1;

        }

        else if (progress < 40) {

            progress += 0.75;

        }

        else if (progress < 60) {

            progress += 0.60;

        }

        else if (progress < 80) {

            progress += 0.50;

        }

        else if (progress < 92) {

            progress += 0.22;

        }

        else if (progress < 98) {

            progress += 0.10;

        }

        bar.style.width = progress + "%";

        percent.innerHTML = Math.floor(progress) + "%";

        const newStage = Math.floor(progress / 14);

        if (

            newStage != stage &&

            newStage < messages.length

        ) {

            stage = newStage;

            text.innerHTML = messages[stage];

        }

    }, 250);

    return true;

}