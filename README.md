# Python Port Scanner

A simple and efficient port scanner written in Python using the `socket` module. This tool allows users to scan a range of ports on a target system to determine which ports are open.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Commonly Open Ports](#commonly-open-ports)
- [Code Explanation](#code-explanation)
- [Contributing](#contributing)
- [License](#license)

## Features

- Scans a specified range of ports on a target IP address.
- Reports which ports are open and which are closed.
- Simple command-line interface.
- Configurable timeout for connection attempts.

## Requirements

- Python 3.x
- Basic knowledge of command-line usage.

## Installation

1. **Clone the repository:**
git clone https://github.com/yourusername/python-port-scanner.git
cd python-port-scanner
text

2. **Run the script directly** (no additional dependencies required):
python port_scanner.py
text

## Usage

To use the port scanner, run the script from the command line with the target IP address and the range of ports you want to scan. The syntax is as follows:

python port_scanner.py <target> <start_port> <end_port>
text

### Example

To scan ports from 1 to 1024 on the target IP address `192.168.1.1`, use the following command:

python port_scanner.py 192.168.1.1 1 1024
text

## Commonly Open Ports

Here are some commonly open ports that you might encounter during your scans:

- **Port 21**: FTP (File Transfer Protocol)
- **Port 22**: SSH (Secure Shell)
- **Port 25**: SMTP (Simple Mail Transfer Protocol)
- **Port 53**: DNS (Domain Name System)
- **Port 80**: HTTP (Hypertext Transfer Protocol)
- **Port 443**: HTTPS (HTTP Secure)
- **Port 110**: POP3 (Post Office Protocol)
- **Port 143**: IMAP (Internet Message Access Protocol)
- **Port 3389**: RDP (Remote Desktop Protocol)

## Code Explanation

The script uses the `socket` module to create TCP connections to specified ports on the target system. It checks whether each port is open or closed by attempting to connect and reports the result.

### Key Functions:

- **scan_ports(target, start_port, end_port)**: Scans the specified range of ports on the target IP address and prints out whether each port is open or closed.

### Timeout Configuration:

The script sets a default timeout for connection attempts to avoid long waits for unresponsive ports. You can modify this value in the code if needed.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to create an issue or submit a pull request.

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

