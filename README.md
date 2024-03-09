# Intrusion Detection System (IDS)

## Project Overview
This project aims to develop a simple Intrusion Detection System (IDS) that monitors network traffic for suspicious activity and alerts administrators to potential threats. The system captures network packets, analyzes them for anomalies, and generates alerts for any detected threats.

## Features
- Real-time packet sniffing on a specified network interface
- Anomaly detection based on predefined criteria
- Alert generation and notification for detected threats
- Logging of network traffic and detected anomalies

## Installation and Setup

### Prerequisites
- Python 3.x
- pip (Python package installer)
- Npcap (for Windows users) or libpcap (for Linux/macOS users)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/intrusion_detection_system.git
   ```
2. Navigate to the project directory:
   ```bash
   cd intrusion_detection_system
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Npcap Installation (Windows)
1. Download the Npcap installer from [the official website](https://nmap.org/npcap/#download).
2. Run the installer and ensure that the "Install Npcap in WinPcap API-compatible Mode" option is checked.
3. Follow the installation prompts to complete the installation.

### libpcap Installation (Linux/macOS)
- **Linux:** Use your package manager to install libpcap. For example, on Debian-based systems:
  ```bash
  sudo apt-get install libpcap-dev
  ```
- **macOS:** libpcap is usually pre-installed on macOS. If it's not, you can install it using Homebrew:
  ```bash
  brew install libpcap
  ```

### Configuration
1. Open the `config/config.yaml` file and set the `interface` to the network interface you want to monitor (e.g., `eth0`, `wlan0`).
2. Adjust the anomaly detection and alert settings as needed.

## Usage
To start the IDS, run the following command from the project root directory:
```bash
python src/main.py
```
Note: On Windows, you may need to run the command prompt as an administrator to allow packet sniffing.

## Testing
- Sample network traffic data can be placed in the `data/test_data/` directory for testing the anomaly detection and alerting functionality.

## Contributing
Contributions to the project are welcome. Please follow the standard GitHub workflow for submitting pull requests.

## Acknowledgments
- [Scapy](https://scapy.net/) for packet sniffing and manipulation
- [Pandas](https://pandas.pydata.org/) and [NumPy](https://numpy.org/) for data manipulation and analysis
- [Sklearn](https://scikit-learn.org/) for machine learning algorithms (if used)
