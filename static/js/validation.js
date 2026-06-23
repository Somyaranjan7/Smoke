function validateTarget() {

    let target =
        document.getElementById(
            "target"
        ).value;

    target = target.trim();

    if (target === "") {

        alert(
            "Please enter an IP address or hostname."
        );

        return false;
    }

    return true;

}