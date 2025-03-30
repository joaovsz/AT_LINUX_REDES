from scapy.all import sniff, IP, TCP, send
import sys

def analisar_pacote(pacote):
    if IP in pacote and TCP in pacote:
        print(f"\n[+] Pacote capturado:")
        print(f"    De: {pacote[IP].src}:{pacote[TCP].sport}")
        print(f"    Para: {pacote[IP].dst}:{pacote[TCP].dport}")

        novo_pacote = pacote.copy()
        novo_pacote[IP].src = "192.168.100.50"
        novo_pacote[IP].dst = "192.168.100.1"
        novo_pacote[TCP].dport = 8080

        del novo_pacote[IP].chksum
        del novo_pacote[TCP].chksum

        print("    [+] Injetando pacote modificado...")
        send(novo_pacote, verbose=0)
        print("    [✓] Pacote enviado com sucesso.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: sudo python scapy_ex8.py <interface>")
        sys.exit(1)

    interface = sys.argv[1]
    print(f"[*] Capturando pacotes na interface {interface}...")
    sniff(iface=interface, prn=analisar_pacote, count=15)
