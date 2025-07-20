from typing import cast
from flask import render_template, request, redirect, url_for, flash
from marshmallow import ValidationError
from werkzeug import Response
from src.helpers.flash_errors import exibir_primeiro_erro
from src.models.Artista import Artista
from src.schemas.ArtistaSchema import ArtistaSchema
from src.services.ArtistaService import ArtistaService


def cadastrar() -> str:
    return render_template("artistas/cadastro.html")


def inserir() -> Response:
    try:
        artista = cast(Artista, ArtistaSchema().load(request.form))
        ArtistaService.criar(artista)
        flash("O artista foi cadastrado com sucesso!", "sucesso")
        return redirect(url_for("artista.listar", nacional=artista.nacional))
    except ValidationError as ve:
        exibir_primeiro_erro(ve)
        return redirect(url_for("artista.cadastrar"))
    except Exception as e:
        flash(str(e), "erro")
        return redirect(url_for("artista.cadastrar"))


def listar(nacional: int) -> str:
    try:
        raw = ArtistaService.listar_por_nacional(bool(nacional))
        artistas = [cast(tuple, artista)[0] for artista in raw]
        schema = ArtistaSchema(many=True).dump(artistas)
        return render_template("artistas/lista.html", artistas=schema)
    except Exception as e:
        return render_template("erro.html", erro=str(e))


def editar(id: int) -> str:
    try:
        artista = ArtistaService.buscar_por_id(id)
        return render_template("artistas/edicao.html", artista=artista)
    except Exception as e:
        return render_template("erro.html", erro=str(e))


def atualizar(id: int) -> Response:
    try:
        dados = request.form.to_dict()
        dados["id"] = str(id)
        artista = cast(Artista, ArtistaSchema().load(dados))
        ArtistaService.atualizar(artista)
        flash("O artista foi atualizado com sucesso!", "sucesso")
        return redirect(url_for("artista.listar", nacional=artista.nacional))
    except ValidationError as ve:
        exibir_primeiro_erro(ve)
        return redirect(url_for("artista.editar", id=id))
    except Exception as e:
        flash(str(e), "erro")
        return redirect(url_for("artista.editar", id=id))


def excluir(id: int) -> Response:
    artista: Artista | None = None
    try:
        artista = ArtistaService.excluir(id)
        flash("O artista foi excluído com sucesso!", "sucesso")
    except Exception as e:
        flash(str(e), "erro")
    nacional = 1 if artista and not artista.nacional else 0
    return redirect(request.referrer or url_for("artista.nacional", nacional=nacional))
