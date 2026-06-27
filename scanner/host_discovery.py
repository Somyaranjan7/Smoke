import nmap


def discover_hosts(network):

    nm = nmap.PortScanner()

    nm.scan(
        hosts=network,
        arguments="-sn"
    )

    hosts = []

    for host in nm.all_hosts():

        hosts.append({

            "ip": host,

            "status": nm[host].state()

        })

    return hosts