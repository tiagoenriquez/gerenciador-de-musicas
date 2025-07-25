from typing import List
from src.repositories.MusicaRepository import MusicaRepository
from src.repositories.ArtistaRepository import ArtistaRepository
from src.models.Musica import Musica


class MusicaService:
    @staticmethod
    def criar(musica: Musica) -> Musica:
        artista = ArtistaRepository.buscar_por_id(musica.artista_id)
        outras = MusicaRepository.buscar_por_nome(musica.nome)
        for outra in outras:
            if musica.artista_id == outra.artista_id:
                raise ValueError("A música já foi cadastrada.")
        if not artista:
            raise ValueError("Artista inválido.")
        return MusicaRepository.inserir(musica)

    @staticmethod
    def atualizar(musica: Musica) -> Musica:
        _ = MusicaService.__buscar_ou_lancar_erro(musica.id)
        artista = ArtistaRepository.buscar_por_id(musica.artista_id)
        if not artista:
            raise ValueError("O artista não foi cadastrado.")
        outras = MusicaRepository.buscar_por_nome(musica.nome)
        for outra in outras:
            if musica.artista_id == outra.artista_id and musica.id != outra.id:
                raise ValueError("O artista já tem outra música com este nome.")
        return MusicaRepository.atualizar(musica)

    @staticmethod
    def listar_por_artista(artista_id: int) -> List[Musica]:
        musicas = MusicaRepository.listar_por_artista(artista_id)
        if not musicas:
            raise LookupError("Nenhuma música do artista foi cadastrada.")
        return musicas

    @staticmethod
    def buscar_por_id(id: int) -> Musica:
        return MusicaService.__buscar_ou_lancar_erro(id)

    @staticmethod
    def buscar_por_trecho(trecho: str) -> List[Musica]:
        musicas = MusicaRepository.buscar_por_trecho(trecho)
        if not musicas:
            raise LookupError("Nenhuma música foi encontrada com o trecho informado.")
        return musicas

    @staticmethod
    def excluir(id: int) -> Musica:
        musica = MusicaService.__buscar_ou_lancar_erro(id)
        MusicaRepository.deletar(musica)
        return musica

    @staticmethod
    def sortear(nacional: bool) -> Musica:
        musica = MusicaRepository.sortear(nacional)
        if not musica:
            raise LookupError(
                f"Não há musica {'nacional' if nacional else 'internacional'} cadastrada."
            )
        return musica

    @staticmethod
    def contar(nacional: bool) -> int:
        return MusicaRepository.contar(nacional)

    @staticmethod
    def __buscar_ou_lancar_erro(id: int) -> Musica:
        musica = MusicaRepository.buscar_por_id(id)
        if not musica:
            raise LookupError("A música não foi encontrada.")
        return musica
