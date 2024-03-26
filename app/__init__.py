from flask import Flask
from dotenv import load_dotenv
import os
from os.path import join, dirname

def create_app():
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    
    secret_key = os.environ.get('SECRET_KEY', 'secret').encode()
    admin_id = os.environ.get('ADMIN_ID', 'admin123')
    flag = os.environ.get('FLAG', 'THIS_IS_NOT_THE_FLAG')

    app = Flask(__name__)
    app.secret_key = secret_key
    app.config['SESSION_COOKIE_HTTPONLY'] = False
    app.config['ADMIN_ID'] = admin_id
    app.config['FLAG'] = flag

    from .routes import main as main_routes
    app.register_blueprint(main_routes)

    return app
