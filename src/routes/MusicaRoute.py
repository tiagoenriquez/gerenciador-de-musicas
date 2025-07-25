from flask import Blueprint
from src.controllers.MusicaController import (
    atualizar,
    cadastrar,
    cadastrar_procura,
    cadastrar_sorteio,
    contar,
    editar,
    excluir,
    inserir,
    listar,
    procurar,
    sortear,
)


musica_blueprint = Blueprint("musica", __name__, url_prefix="/musicas")

musica_blueprint.add_url_rule("/cadastro", view_func=cadastrar, methods=["GET"])
musica_blueprint.add_url_rule(
    "/lista/<int:artista_id>", view_func=listar, methods=["GET"]
)
musica_blueprint.add_url_rule("/edicao/<int:id>", view_func=editar, methods=["GET"])
musica_blueprint.add_url_rule("/exclusao/<int:id>", view_func=excluir, methods=["GET"])
musica_blueprint.add_url_rule("/principal", view_func=contar, methods=["GET"])
musica_blueprint.add_url_rule("/procura", view_func=cadastrar_procura, methods=["GET"])
musica_blueprint.add_url_rule("/sorteio", view_func=cadastrar_sorteio, methods=["GET"])
musica_blueprint.add_url_rule("/insercao", view_func=inserir, methods=["POST"])
musica_blueprint.add_url_rule(
    "/atualizacao/<int:id>", view_func=atualizar, methods=["POST"]
)
musica_blueprint.add_url_rule("/sorteada", view_func=sortear, methods=["POST"])
musica_blueprint.add_url_rule("/procura", view_func=procurar, methods=["POST"])
