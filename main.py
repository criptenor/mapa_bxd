from flask import Flask, jsonify

class MyFlaskApp:
    def __init__(self, name):
        # Cria uma instância do Flask
        self.app = Flask(name)
        self.configure_routes()

    def configure_routes(self):
        # Configura uma rota simples para a home
        @self.app.route('/')
        def home():
            return jsonify(message="Bem-vindo ao Flask!")

        # Outra rota de exemplo
        @self.app.route('/status')
        def status():
            return jsonify(status="Aplicação rodando")

    def run(self, host='127.0.0.1', port=5000):
        # Executa o aplicativo Flask
        self.app.run(host=host, port=port)

# Para rodar a aplicação Flask
if __name__ == "__main__":
    # Instancia a classe que cria o app Flask
    app = MyFlaskApp(__name__)
    # Roda o servidor Flask
    app.run()
