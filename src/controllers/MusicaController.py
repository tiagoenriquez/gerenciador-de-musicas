from typing import cast
from flask import flash, redirect, render_template, request, url_for
from marshmallow import ValidationError
from werkzeug import Response
from src.helpers.flash_errors import exibir_primeiro_erro
from src.models.Musica import Musica
from src.schemas.ArtistaSchema import ArtistaSchema
from src.schemas.MusicaSchema import MusicaSchema
from src.schemas.NacionalSchema import NacionalSchema
from src.schemas.TrechoSchema import TrechoSchema
from src.services.ArtistaService import ArtistaService
from src.services.MusicaService import MusicaService


def cadastrar() -> str:
    try:
        artistas = ArtistaService.listar_todos()
        schema = ArtistaSchema(many=True).dump(artistas)
        return render_template("musicas/cadastro.html", artistas=schema)
    except Exception as e:
        return render_template("erro.html", erro=str(e))


def inserir() -> Response:
    try:
        musica = cast(Musica, MusicaSchema().load(request.form))
        MusicaService.criar(musica)
        flash("A música foi cadastrada com sucesso", "sucesso")
        return redirect(url_for("musica.listar", artista_id=musica.artista_id))
    except ValidationError as ve:
        exibir_primeiro_erro(ve)
        return redirect(url_for("musica.cadastrar"))
    except Exception as e:
        flash(str(e), "erro")
        return redirect(url_for("musica.cadastrar"))


def listar(artista_id: int) -> str:
    try:
        musicas = MusicaService.listar_por_artista(artista_id)
        artista = ArtistaService.buscar_por_id(artista_id)
        musicas_schema = MusicaSchema(many=True).dump(musicas)
        artista_schema = ArtistaSchema().dump(artista)
        return render_template(
            "musicas/lista.html", musicas=musicas_schema, artista=artista_schema
        )
    except Exception as e:
        return render_template("erro.html", erro=str(e))


def editar(id: int) -> str:
    try:
        musica = MusicaService.buscar_por_id(id)
        artistas = ArtistaService.listar_todos()
        musica_schema = MusicaSchema().dump(musica)
        artistas_schema = ArtistaSchema(many=True).dump(artistas)
        return render_template(
            "musicas/edicao.html", musica=musica_schema, artistas=artistas_schema
        )
    except Exception as e:
        return render_template("erro.html", erro=str(e))


def atualizar(id: int) -> Response:
    try:
        dados = request.form.to_dict()
        dados["id"] = str(id)
        musica = cast(Musica, MusicaSchema().load(dados))
        MusicaService.atualizar(musica)
        flash("A música foi atualizada com sucesso.", "sucesso")
        return redirect(url_for("musica.listar", artista_id=musica.artista_id))
    except ValidationError as ve:
        exibir_primeiro_erro(ve)
        return redirect(url_for("musica.editar", id=id))
    except Exception as e:
        flash(str(e), "erro")
        return redirect(url_for("musica.editar", id=id))


def excluir(id: int) -> Response:
    try:
        musica = MusicaService.excluir(id)
        flash("A música foi excluída com sucesso.", "sucesso")
        return redirect(url_for("musica.listar", artista_id=musica.artista_id))
    except Exception as e:
        flash(str(e), "erro")
        return redirect(url_for("musica.contar"))


def cadastrar_sorteio() -> str:
    return render_template("musicas/sorteio.html")


def sortear() -> str:
    try:
        nacional = cast(dict[str, bool], NacionalSchema().load(request.form))[
            "nacional"
        ]
        musica = MusicaService.sortear(nacional)
        schema = MusicaSchema().dump(musica)
        return render_template("musicas/sorteada.html", musica=schema)
    except Exception as e:
        return render_template("erro.html", erro=str(e))


def contar() -> str:
    try:
        nacionais = MusicaService.contar(True)
        internacionais = MusicaService.contar(False)
        total = nacionais + internacionais
        return render_template(
            "index.html",
            nacionais=nacionais,
            internacionais=internacionais,
            total=total,
        )
    except Exception as e:
        return render_template("erro.html", erro=str(e))


def cadastrar_procura() -> str:
    return render_template("musicas/procura.html")


def procurar() -> str:
    try:
        trecho = cast(dict[str, str], TrechoSchema().load(request.form))["trecho"]
        musicas = MusicaService.buscar_por_trecho(trecho)
        schema = MusicaSchema(many=True).dump(musicas)
        return render_template("musicas/encontradas.html", musicas=schema)
    except Exception as e:
        return render_template("erro.html", erro=str(e))
