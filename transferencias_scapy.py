from scapy.all import sniff, IP, TCP, UDP, Raw

def detectar_pacotes(pacote):
    if IP in pacote and (TCP in pacote or UDP in pacote) and Raw in pacote:
        protocolo = "TCP" if TCP in pacote else "UDP"
        src = pacote[IP].src
        dst = pacote[IP].dst
        tamanho = len(pacote[Raw].load)

        print(f"[+] {protocolo} com dados detectado:")
        print(f"    {src} → {dst} | {tamanho} bytes")
        print(f"    Conteúdo: {pacote[Raw].load[:60]}")
        print("-" * 50)

if __name__ == "__main__":
    print("Detectando pacotes com carga útil (payload)... Pressione Ctrl+C para parar.")
    sniff(prn=detectar_pacotes, store=0)
