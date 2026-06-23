def get_recommendation(port, state):

    if state != "open":

        return ""

    recommendations = {

        21: (

            "FTP transmits credentials in plain text and can allow unauthorized access.",

            "Disable FTP or replace it with SFTP."

        ),

        22: (

            "SSH can be targeted by brute-force attacks if exposed to the internet.",

            "Restrict access using firewalls and disable password authentication."

        ),

        23: (

            "Telnet sends all data unencrypted and is considered insecure.",

            "Disable Telnet and use SSH instead."

        ),

        25: (

            "SMTP servers are vulnerable to spam relay abuse and spoofing.",

            "Restrict mail relay and configure authentication."

        ),

        80: (

            "HTTP traffic is unencrypted and vulnerable to interception.",

            "Redirect users to HTTPS."

        ),

        443: (

            "HTTPS services may expose web vulnerabilities if misconfigured.",

            "Keep web applications updated and use strong TLS settings."

        ),

        445: (

            "SMB has historically been exploited by malware such as WannaCry.",

            "Disable SMB if unnecessary and restrict network access."

        ),

        3306: (

            "Exposed MySQL databases may allow unauthorized access.",

            "Restrict database access to trusted hosts only."

        ),

        3389: (

            "RDP is frequently targeted by attackers and ransomware groups.",

            "Restrict RDP access and enable MFA."

        )

    }

    default = (

        "Open ports increase the attack surface of the system.",

        "Close unnecessary services and restrict access."

    )

    danger, recommendation = recommendations.get(

        port,

        default

    )

    return (

        f"Why dangerous: {danger}\n"

        f"Recommendation: {recommendation}"

    )