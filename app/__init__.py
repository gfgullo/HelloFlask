from flask import Flask
from flask_bootstrap import Bootstrap

boostrap = Bootstrap()

def create_app():

    app = Flask(__name__)
    boostrap.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app