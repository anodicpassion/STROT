import nmap

def service_scan(target_ip):
    """
    Runs an Nmap service scan on the given IP address.

    Args:
        target_ip (str): The IP address to scan.

    Returns:
        dict: Information about the services or an error message.
    """
    # Create an Nmap PortScanner object
    nm = nmap.PortScanner()

    try:
        print(f"Scanning IP: {target_ip} for services...")
        # Run the service scan
        scan_result = nm.scan(hosts=target_ip, arguments="-sV", timeout=1000)
        # scan_result = nm.scan(hosts=target_ip, arguments="-r", timeout=1000)

        # Check if the scan was successful
        if target_ip in scan_result['scan']:
            services = []
            for port in scan_result['scan'][target_ip].get('tcp', {}):
                port_info = scan_result['scan'][target_ip]['tcp'][port]
                services.append({
                    "port": port,
                    "state": port_info.get('state', 'unknown'),
                    "name": port_info.get('name', 'unknown'),
                    "product": port_info.get('product', 'unknown'),
                    "version": port_info.get('version', 'unknown')
                })
            return {
                "status": "success",
                "services": services
            }
        else:
            return {
                "status": "error",
                "message": "No services could be determined."
            }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

if __name__ == "__main__":
    # Input IP address
    target_ip = input("Enter the IP address to scan for services: ")

    # Perform the service scan
    result = service_scan(target_ip)

    if result['status'] == "success":
        print("\nService Scan Results:")
        print("Port\tState\tName\tProduct\tVersion")
        print("----------------------------------------------------------")
        for service in result['services']:
            print(f"{service['port']}\t{service['state']}\t{service['name']}\t{service['product']}\t{service['version']}")
    else:
        print(f"Error: {result['message']}")

