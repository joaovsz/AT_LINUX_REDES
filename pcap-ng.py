import pcapy
from impacket.ImpactDecoder import EthDecoder
from impacket.ImpactPacket import Ethernet, IP, TCP
import sys

def capturar_pacotes(interface, num_pacotes=5):
    print(f"Capturando {num_pacotes} pacotes na interface: {interface}")
    decoder = EthDecoder()
    capturador = pcapy.open_live(interface, 65536, 1, 1000)

    def callback(hdr, data):
        pacote = decoder.decode(data)
        print(pacote)

    try:
        capturador.loop(num_pacotes, callback)
    except KeyboardInterrupt:
        print("\nCaptura interrompida pelo usuário.")

def injetar_pacote(interface, src_ip="192.168.0.2", dst_ip="192.168.0.3", src_port=1234, dst_port=80):
    print(f"Injetando pacote na interface: {interface}")
    
    eth = Ethernet()
    eth.set_ether_type(0x0800)

    ip = IP()
    ip.set_ip_src(src_ip)
    ip.set_ip_dst(dst_ip)

    tcp = TCP()
    tcp.set_th_sport(src_port)
    tcp.set_th_dport(dst_port)
    ip.contains(tcp)
    eth.contains(ip)

    try:
        sender = pcapy.open_live(interface, 65536, 0, 0)
        sender.sendpacket(eth.get_packet())
        print("Pacote injetado com sucesso!")
    except Exception as e:
        print(f"Erro ao injetar pacote: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: sudo python pcap-ng.py <interface>")
        sys.exit(1)

    interface = sys.argv[1]

    capturar_pacotes(interface)

    injetar_pacote(interface)