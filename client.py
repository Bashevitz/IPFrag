from scapy.all import *
import math


def send_udp_message(message, num_fragments, target_ip, target_port):
    fragment_size = math.ceil(len(message) / num_fragments)

    for i in range(num_fragments):
        start = i * fragment_size
        end = min((i + 1) * fragment_size, len(message))
        fragment = message[start:end]

        udp_packet = IP(dst=target_ip) / UDP(dport=target_port) / fragment

        send(udp_packet)
        print(f"Sent fragment {i + 1}: {fragment}")


message = input("Enter the message to send: ")
num_fragments = int(input("Enter the number of fragments: "))
target_ip = input("Enter the server IP: ")
target_port = 55555

send_udp_message(message, num_fragments, target_ip, target_port)
