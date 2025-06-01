def parse_packet(packet):
    try:
        src = packet[0][1].src
        dst = packet[0][1].dst
        proto = packet[0].proto if hasattr(packet[0], 'proto') else "Unknown"
        return f"Src: {src} -> Dst: {dst} | Protocol: {proto}"
    except Exception as e:
        return f"[!] Error parsing packet: {str(e)}"
