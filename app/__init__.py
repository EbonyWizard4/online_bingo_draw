from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY = 'dev'
    )
    @app.route("/")
    def home():
        return "hoje deu!"
    
    from . import bingo
    app.register_blueprint(bingo.bp)
    
    from . import sorte
    app.register_blueprint(sorte.bp)
    
    return app