import nmap

def analyze_os(target_ip):
    """
    Analyzes the operating system of a given IP address using nmap.

    Args:
        target_ip (str): The IP address to analyze.

    Returns:
        dict: Information about the operating system or an error message.
    """
    # Create an Nmap PortScanner object
    nm = nmap.PortScanner()

    try:
        print(f"Scanning IP: {target_ip} for OS detection...")
        # Run the OS detection scan
        scan_result = nm.scan(hosts=target_ip, arguments="-O", timeout=30)
        
        # Check if the scan was successful
        if 'osmatch' in scan_result['scan'][target_ip]:
            os_matches = scan_result['scan'][target_ip]['osmatch']
            return {
                "status": "success",
                "os_matches": os_matches
            }
        else:
            return {
                "status": "error",
                "message": "No OS information could be determined."
            }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

if __name__ == "__main__":
    # Input IP address
    target_ip = input("Enter the IP address to analyze: ")

    # Analyze the OS
    result = analyze_os(target_ip)

    if result['status'] == "success":
        print("\nOperating System Analysis:")
        for match in result['os_matches']:
            print(f"Name: {match['name']}\nAccuracy: {match['accuracy']}%\n")
            break
    else:
        print(f"Error: {result['message']}")

