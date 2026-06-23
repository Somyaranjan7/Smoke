from scanner.port_scanner import scan_target
from scanner.service_detection import detect_services
from scanner.enumeration import enumerate_services
from scanner.risk_analysis import get_risk
from scanner.recommendations import get_recommendation


def run_scan(target):

    ports = scan_target(target)

    services = detect_services(target)

    versions = enumerate_services(target)

    result = {}

    for port in ports:

        result[port] = {

            "state":
            ports[port]["state"],

            "service":
            services.get(port, ""),

            "version":
            versions.get(port, {}).get(
                "version", ""
            ),

            "risk":
            get_risk(
            port,
            ports[port]["state"]
            ),

            "recommendation":
            get_recommendation(
            port,
            ports[port]["state"]
            )
        }

    return result