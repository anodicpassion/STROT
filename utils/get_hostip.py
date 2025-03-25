import socket

def get_hostip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))  # Connect to an external server (Google DNS)
    ip_address = s.getsockname()[0]  # Get the IP address of the machine
    s.close()

    return ip_address

if __name__ == "__main__":
    print("host ip:", get_hostip())