import nmap

COMMON_PORTS = "21,22,23,25,53,80,110,143,443,3306,3389"


def scan_target(target):

    nm = nmap.PortScanner()

    nm.scan(
        hosts=target,
        ports=COMMON_PORTS
    )

    ports_data = {}

    for host in nm.all_hosts():

        for protocol in nm[host].all_protocols():

            for port in nm[host][protocol]:

                ports_data[port] = {
                    "state": nm[host][protocol][port]["state"]
                }

    return ports_data