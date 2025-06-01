from scapy.all import sniff

def capture_packets(packet_handler, iface=None, count=0):
    sniff(prn=packet_handler, iface=iface, count=count, store=False)
