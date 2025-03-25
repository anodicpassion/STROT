from scapy.all import ARP, Ether, srp

def scan_network(ip_range):
    """
    Scans the network for active devices within the specified IP range.

    Args:
        ip_range (str): The IP range to scan, e.g., "192.168.1.1/24".

    Returns:
        list: A list of dictionaries containing IP and MAC addresses of active devices.
    """
    # Create an ARP request packet
    arp_request = ARP(pdst=ip_range)
    # Create an Ethernet frame to wrap the ARP request
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = broadcast / arp_request

    # Send the packet and capture responses
    responses, _ = srp(packet, timeout=2, verbose=False)

    # Parse the responses to extract IP and MAC addresses
    devices = []
    for response in responses:
        devices.append({
            "ip": response[1].psrc,
            "mac": response[1].hwsrc
        })

    return devices

if __name__ == "__main__":
    # Define the IP range to scan
    ip_range = input("Enter the IP range to scan (e.g., 192.168.202.211/24): ")

    print("Scanning network...")
    devices = scan_network(ip_range)

    # Print the results
    if devices:
        print("\nDevices found in the network:")
        print("IP Address\t\tMAC Address")
        print("-----------------------------------------")
        for device in devices:
            print(f"{device['ip']}\t\t{device['mac']}")
    else:
        print("No devices found.")
