def get_risk(port, state):

    if state != "open":

        return "No Risk"

    high_risk_ports = [

        21,     # FTP
        23,     # Telnet
        445,    # SMB
        3389    # RDP

    ]

    medium_risk_ports = [

        22,     # SSH
        25,     # SMTP
        3306,   # MySQL
        5432    # PostgreSQL

    ]

    if port in high_risk_ports:

        return "High"

    elif port in medium_risk_ports:

        return "Medium"

    else:

        return "Low"