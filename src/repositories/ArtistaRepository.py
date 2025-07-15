from src.connections.DatabaseConnection import db
from src.models.Artista import Artista
from typing import Optional, List


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
        return Artista.query.filter_by(nacional=nacional).order_by(Artista.nome.asc()).all()

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
