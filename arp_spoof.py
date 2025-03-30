from scapy.all import sniff, ARP

tabela_arp = {}

def verificar_arp(pacote):
    if pacote.haslayer(ARP) and pacote[ARP].op == 2:
        ip = pacote[ARP].psrc
        mac = pacote[ARP].hwsrc

        if ip in tabela_arp:
            if tabela_arp[ip] != mac:
                print(f"\n[ALERTA] Possível ARP Spoofing detectado!")
                print(f"   Endereço IP: {ip}")
                print(f"   MAC esperado: {tabela_arp[ip]}")
                print(f"   MAC recebido: {mac}")
        else:
            tabela_arp[ip] = mac

if __name__ == "__main__":
    print("Iniciando monitoramento de pacotes ARP... Pressione Ctrl+C para encerrar.")
    sniff(filter="arp", store=0, prn=verificar_arp)
