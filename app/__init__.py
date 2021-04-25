from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
#import loginmanager l8r


bootstrap = Bootstrap()
db = SQLAlchemy()

#create login manager instance l8r

def make_app():
    app = Flask(__name__,instance_relative_config = True)

    #creating app configs
    app.config.from_object(config_options[config_name])

    #flask extnsions
    bootstrap.init_app(app)
    db.init_app(app

    # Registering the blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')


    # setting config
    from .request import configure_request
    configure_request(app)

    return app