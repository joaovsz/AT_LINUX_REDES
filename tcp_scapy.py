from scapy.all import IP, TCP, sr1
import sys

def scan_port(ip, porta):
    pacote = IP(dst=ip)/TCP(dport=porta, flags="S")
    resposta = sr1(pacote, timeout=1, verbose=0)

    if resposta is None:
        print(f"Porta {porta}: sem resposta (possivelmente filtrada)")
    elif resposta.haslayer(TCP):
        if resposta[TCP].flags == 0x12:
            print(f"Porta {porta}: está aberta")
        elif resposta[TCP].flags == 0x14:
            print(f"Porta {porta}: está fechada")
        else:
            print(f"Porta {porta}: recebeu uma resposta inesperada")
    else:
        print(f"Porta {porta}: não possui camada TCP")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Modo de uso: sudo python scanner_tcp_scapy.py <IP-alvo>")
        sys.exit(1)

    alvo = sys.argv[1]
    portas = [22, 80, 443, 8080]

    print(f"Iniciando escaneamento de portas no alvo {alvo}...\n")
    for porta in portas:
        scan_port(alvo, porta)
