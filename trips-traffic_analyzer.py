from scapy.all import sniff

def process_packet(packet):
    print(packet.summary())  # Display a summary of each packet

if __name__ == "__main__":
    print("Sniffing network traffic... Press Ctrl+C to stop.")
    # Sniff packets on interface 'enp0s3' (replace 'eth0' with your interface)
    sniff(iface="enp0s3", prn=process_packet, store=False)
