from flask import Blueprint
from src.controllers.ArtistaController import (
    atualizar,
    cadastrar,
    editar,
    excluir,
    inserir,
    listar,
)


artista_blueprint = Blueprint("artista", __name__, url_prefix="/artistas")

artista_blueprint.add_url_rule("/cadastro", view_func=cadastrar, methods=["GET"])
artista_blueprint.add_url_rule(
    "/lista/<int:nacional>", view_func=listar, methods=["GET"]
)
artista_blueprint.add_url_rule("/edicao/<int:id>", view_func=editar, methods=["GET"])
artista_blueprint.add_url_rule("/exclusao/<int:id>", view_func=excluir, methods=["GET"])
artista_blueprint.add_url_rule("/insercao", view_func=inserir, methods=["POST"])
artista_blueprint.add_url_rule(
    "/atualizacao/<int:id>", view_func=atualizar, methods=["POST"]
)
