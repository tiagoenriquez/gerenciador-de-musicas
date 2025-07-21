from sqlalchemy import desc, func
from src.connections.DatabaseConnection import db
from src.models.Artista import Artista
from src.models.Musica import Musica
from typing import Optional, List, cast


class ArtistaRepository:
    @staticmethod
    def inserir(artista: Artista) -> Artista:
        db.session.add(artista)
        db.session.commit()
        return artista
    
    @staticmethod
    def atualizar(artista: Artista) -> Artista:
        existente = Artista.query.get(artista.id)
        if not existente:
            raise ValueError("O artista não foi cadastrado.")
        existente.nome = artista.nome
        existente.nacional = artista.nacional
        db.session.commit()
        return existente

    @staticmethod
    def buscar_por_id(id: int) -> Optional[Artista]:
        return Artista.query.get(id)

    @staticmethod
    def buscar_por_nacional(nacional: bool) -> List[Artista]:
        query = (
            db.session.query(
                Artista,
                func.count(Musica.id).label("n_musicas")
            )
            .outerjoin(Musica, Artista.id == Musica.artista_id)
            .filter(Artista.nacional == nacional)
            .group_by(Artista.id)
            .order_by(func.count(Musica.id).desc() if desc else func.count(Musica.id).asc())
            .order_by(Artista.nome.asc()))
        return [row[0] for row in query]

    @staticmethod
    def buscar_por_nome(nome: str) -> Optional[Artista]:
        return Artista.query.filter_by(nome=nome).first()
    
    @staticmethod
    def listar_todos() -> List[Artista]:
        return Artista.query.order_by(Artista.nome.asc()).all()

    @staticmethod
    def deletar(artista: Artista) -> None:
        db.session.delete(artista)
        db.session.commit()
