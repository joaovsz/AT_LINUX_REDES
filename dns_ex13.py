import dns.resolver

def consultar_dns(dominio):
    tipos = ['A', 'AAAA', 'MX', 'NS', 'TXT']
    for tipo in tipos:
        try:
            respostas = dns.resolver.resolve(dominio, tipo)
            print(f"\n📦 Registros {tipo} de {dominio}:")
            for r in respostas:
                print(f" - {r.to_text()}")
        except Exception as e:
            print(f"Erro {tipo}: {e}")

if __name__ == "__main__":
    dominio = input("Digite o domínio para verificação (ex: google.com): ")
    consultar_dns(dominio)
