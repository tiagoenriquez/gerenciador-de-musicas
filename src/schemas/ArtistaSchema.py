from marshmallow import Schema, fields, validate, post_load
from typing import TYPE_CHECKING
from src.models.Artista import Artista


class ArtistaSchema(Schema):
    id = fields.Int()

    nome = fields.Str(
        required=True,
        validate=validate.Length(
            min=1, max=63, error="O nome deve ter no máximo 63 caracteres."
        ),
        error_messages={
            "required": "O nome do artista é obrigatório.",
            "invalid": "Formato inválido para nome.",
        },
    )

    nacional = fields.Boolean(
        required=True,
        truthy=["1", "true", "True", True],
        falsy=["0", "false", "False", False],
        error_messages={
            "required": "Você precisa informar se o artista é nacional ou não.",
            "invalid": "Valor inválido para o campo nacional. Use 'Sim' ou 'Não'.",
        },
    )

    n_musicas = fields.Method("get_n_musicas")

    @post_load
    def make_artista(self, data, **kwargs) -> "Artista":
        return Artista(**data)

    def get_n_musicas(self, obj) -> int:
        return obj.n_musicas
