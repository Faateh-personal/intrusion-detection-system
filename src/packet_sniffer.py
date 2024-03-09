from scapy.all import sniff

class PacketSniffer:
    def __init__(self, interface):
        self.interface = interface

    def capture_packets(self):
        return sniff(iface=self.interface, prn=self.process_packet, store=False)

    def process_packet(self, packet):
        # Process packet and extract features
        return packet


