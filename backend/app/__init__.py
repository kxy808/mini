from flask import Flask

def launch_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return "Mini backend is live 🚀"
    
    return app