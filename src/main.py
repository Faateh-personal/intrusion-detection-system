from packet_sniffer import PacketSniffer
from anomaly_detector import AnomalyDetector
from alert_manager import AlertManager

def main():
    # Initialize components
    sniffer = PacketSniffer(interface="eth0")
    detector = AnomalyDetector()
    alert_manager = AlertManager()

    # Start packet sniffing
    for packet in sniffer.capture_packets():
        # Check for anomalies
        if detector.is_anomalous(packet):
            # Generate an alert
            alert_manager.generate_alert(packet)

if __name__ == "__main__":
    main()
