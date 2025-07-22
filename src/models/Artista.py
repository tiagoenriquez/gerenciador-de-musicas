from typing import List, cast
from src.connections.DatabaseConnection import db


class Artista(db.Model):
    __tablename__ = "artistas"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(63), nullable=False, unique=True)
    nacional = db.Column(db.Boolean, nullable=False)

    musicas = db.relationship(
        "Musica", back_populates="artista", cascade="all, delete-orphan"
    )

    @property
    def n_musicas(self) -> int:
        return len(cast(List, self.musicas))
