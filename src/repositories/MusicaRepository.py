from src.connections.DatabaseConnection import db
from src.models.Musica import Musica
from typing import Optional, List
from src.models.Artista import Artista


class MusicaRepository:
    @staticmethod
    def inserir(musica: Musica) -> Musica:
        db.session.add(musica)
        db.session.commit()
        return musica

    @staticmethod
    def atualizar(musica: Musica) -> Musica:
        existente = Musica.query.get(musica.id)
        if not existente:
            raise ValueError("A música não foi cadastrada.")
        existente.nome = musica.nome
        existente.artista_id = musica.artista_id
        db.session.commit()
        return existente

    @staticmethod
    def buscar_por_id(id: int) -> Optional[Musica]:
        return Musica.query.get(id)

    @staticmethod
    def buscar_por_nome(nome: str) -> List[Musica]:
        return Musica.query.filter_by(nome=nome).all()

    @staticmethod
    def listar_por_artista(artista_id: int) -> List[Musica]:
        return (
            Musica.query.filter_by(artista_id=artista_id)
            .order_by(Musica.nome.asc())
            .all()
        )

    @staticmethod
    def listar_todas() -> List[Musica]:
        return Musica.query.all()

    @staticmethod
    def deletar(musica: Musica) -> None:
        db.session.delete(musica)
        db.session.commit()

    @staticmethod
    def sortear(nacional: bool) -> Optional[Musica]:
        from sqlalchemy.sql import func

        return (
            Musica.query.join(Artista, Musica.artista_id == Artista.id)
            .filter(Artista.nacional == nacional)
            .order_by(func.random())
            .first()
        )

    @staticmethod
    def contar(nacional: bool) -> int:
        return (
            db.session.query(Musica)
            .join(Artista, Musica.artista_id == Artista.id)
            .filter(Artista.nacional == nacional)
            .count()
        )
