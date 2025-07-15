import os
from dotenv import load_dotenv
from flask import Flask, redirect, url_for
from werkzeug import Response

from init_db import init_db
from src.routes.ArtistaRoute import artista_blueprint
from src.routes.MusicaRoute import musica_blueprint


app = Flask(__name__)
load_dotenv()
app.secret_key = os.getenv("SESSION_KEY")


app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
init_db(app)


@app.route("/")
def index() -> Response:
    return redirect(url_for("musica.contar"))


app.register_blueprint(artista_blueprint)
app.register_blueprint(musica_blueprint)


if __name__ == "__main__":
    app.run(port=7807)
