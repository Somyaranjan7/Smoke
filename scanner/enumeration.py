import nmap

COMMON_PORTS = "21,22,23,25,53,80,110,143,443,3306,3389"


def enumerate_services(target):

    nm = nmap.PortScanner()

    nm.scan(
        hosts=target,
        ports=COMMON_PORTS,
        arguments="-sV"
    )

    versions = {}

    for host in nm.all_hosts():

        for protocol in nm[host].all_protocols():

            for port in nm[host][protocol]:

                versions[port] = {

                    "product":
                    nm[host][protocol][port]["product"],

                    "version":
                    nm[host][protocol][port]["version"]
                }

    return versions