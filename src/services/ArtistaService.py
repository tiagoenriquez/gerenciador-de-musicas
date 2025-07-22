from typing import List
from src.repositories.ArtistaRepository import ArtistaRepository
from src.models.Artista import Artista


class ArtistaService:
    @staticmethod
    def criar(artista: Artista) -> Artista:
        existente = ArtistaRepository.buscar_por_nome(artista.nome)
        if existente:
            raise ValueError("O artista já foi cadastrado.")
        return ArtistaRepository.inserir(artista)

    @staticmethod
    def atualizar(artista: Artista) -> Artista:
        _ = ArtistaService.__buscar_ou_lancar_erro(artista.id)
        outro = ArtistaRepository.buscar_por_nome(artista.nome)
        if outro and outro.id != artista.id:
            raise ValueError("Já existe outro artista com esse nome.")
        return ArtistaRepository.atualizar(artista)

    @staticmethod
    def listar_todos() -> List[Artista]:
        artistas = ArtistaRepository.listar_todos()
        if not artistas:
            raise LookupError(f"Não há artista cadastrado.")
        return artistas

    @staticmethod
    def listar_por_nacional(nacional: bool) -> List[Artista]:
        artistas = ArtistaRepository.buscar_por_nacional(nacional)
        if not artistas:
            raise LookupError(
                f"Não há artista {'nacional' if nacional else 'internacional'} cadastrado."
            )
        return artistas

    @staticmethod
    def buscar_por_id(id: int) -> Artista:
        return ArtistaService.__buscar_ou_lancar_erro(id)

    @staticmethod
    def excluir(id: int) -> Artista:
        artista = ArtistaService.__buscar_ou_lancar_erro(id)
        ArtistaRepository.deletar(artista)
        return artista

    @staticmethod
    def __buscar_ou_lancar_erro(id: int) -> Artista:
        artista = ArtistaRepository.buscar_por_id(id)
        if not artista:
            raise LookupError("O artista não foi encontrado.")
        return artista
