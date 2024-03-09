from scapy.all import get_if_list
from packet_sniffer import PacketSniffer
from anomaly_detector import AnomalyDetector
from alert_manager import AlertManager

def main():
    # List available network interfaces
    interfaces = get_if_list()
    print("Available interfaces:", interfaces)

    # Initialize components
    detector = AnomalyDetector()
    alert_manager = AlertManager()

    # Try each available interface for packet sniffing
    for interface in interfaces:
        try:
            sniffer = PacketSniffer(interface=interface)
            print(f"Trying interface: {interface}")
            for packet in sniffer.capture_packets():
                # Check for anomalies
                if detector.is_anomalous(packet):
                    # Generate an alert
                    alert_manager.generate_alert(packet)
            break  # Exit the loop if packet capture starts successfully
        except Exception as e:
            print(f"Error with interface {interface}: {e}")

if __name__ == "__main__":
    main()


