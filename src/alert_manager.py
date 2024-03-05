class AlertManager:
    def generate_alert(self, packet):
        # Generate an alert for an anomalous packet
        print(f"Alert: Anomalous packet detected - {packet.summary()}")
