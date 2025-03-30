import requests

caminhos = [
    "admin", "login", "config", "setup", "dashboard", "backup", "test", "debug", ".git", "phpinfo", "api"
]

def initFuzzer(url_base):
    print(f"Iniciando fuzzing em: {url_base}\n")
    for caminho in caminhos:
        url = f"{url_base.rstrip('/')}/{caminho}"
        try:
            resposta = requests.get(url, timeout=3)
            status = resposta.status_code
            if status in [200, 301, 302, 403, 500]:
                print(f"[{status}] ➜ {url}")
        except requests.RequestException:
            print(f"[ERRO]  ➜ {url} (erro de conexão)")

if __name__ == "__main__":
    alvo = input("Digite a URL base: ")
    initFuzzer(alvo)
