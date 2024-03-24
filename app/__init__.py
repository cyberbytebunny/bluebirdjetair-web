from flask import Flask
from dotenv import dotenv_values
import os

def create_app():
    config = dotenv_values('.env')
    
    secret_key = config.get('SECRET_KEY', 'secret').encode()
    admin_id = config.get('ADMIN_ID', 'admin123')
    flag = config.get('FLAG', 'THIS_IS_NOT_THE_FLAG')

    app = Flask(__name__)
    app.secret_key = secret_key
    app.config['SESSION_COOKIE_HTTPONLY'] = False
    app.config['ADMIN_ID'] = admin_id
    app.config['FLAG'] = flag

    from .routes import main as main_routes
    app.register_blueprint(main_routes)

    return app
