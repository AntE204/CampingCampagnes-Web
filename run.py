from app import app
from app.config import Config

if __name__ == "__main__":
    config = Config("config.json")
    host = config.get("SERVER_HOST")
    port = config.get("SERVER_PORT")
    app.run(host=host, port=port, debug=True)