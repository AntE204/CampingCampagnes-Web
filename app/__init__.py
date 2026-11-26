from flask import Flask
from .config import Config

app = Flask(__name__)
config = Config("config.json")

app.config["SECRET_KEY"] = config.get("FLASK_SECRET_KEY")

from app import routes, error_handlers