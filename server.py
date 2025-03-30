from http.server import HTTPServer, BaseHTTPRequestHandler

class ServidorSimples(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<h1>Executando server - AT</h1>")

if __name__ == "__main__":
    servidor = HTTPServer(("0.0.0.0", 5173), ServidorSimples)
    print("Servidor rodando em http://localhost:5173")
    servidor.serve_forever()

