from src.connections.DatabaseConnection import db
from src.models.Artista import Artista


class Musica(db.Model):
    __tablename__ = "musicas"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(63), nullable=False)
    artista_id = db.Column(db.Integer, db.ForeignKey("artistas.id"), nullable=False)

    artista = db.relationship("Artista", back_populates="musicas")
