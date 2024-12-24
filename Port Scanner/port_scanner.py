import socket
import sys
from datetime import datetime

def scan_ports(target, start_port, end_port):
    print("=" * 45)
    print(f"Scan Target: {target}")
    print(f"Scanning started at: {datetime.now()}")
    print("=" * 45)

    for port in range(start_port, end_port + 1):
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)  # Set timeout for connection attempts
        
        # Attempt to connect to the port
        result = s.connect_ex((target, port))
        
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
        
        s.close()  # Close the socket

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python port_scanner.py <target> <start_port> <end_port>")
        sys.exit(1)

    target_ip = sys.argv[1]
    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3])

    scan_ports(target_ip, start_port, end_port)
