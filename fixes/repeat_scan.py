import nmap

def repeat_scan(ip, port):

    nm = nmap.PortScanner()

    nm.scan(

        hosts=ip,

        ports=str(port)

    )

    if (

        ip in nm.all_hosts()

        and

        "tcp" in nm[ip]

        and

        port in nm[ip]["tcp"]

    ):

        state = nm[ip]["tcp"][port]["state"]

    else:

        state = "closed"

    return {

        "port": port,

        "state": state

    }