from marshmallow import Schema, fields


class NacionalSchema(Schema):
    nacional = fields.Boolean(
        required=True,
        truthy=["1", "true", "True", True],
        falsy=["0", "false", "False", False],
        error_messages={
            "required": "Você precisa informar se o artista é nacional ou não.",
            "invalid": "Valor inválido para o campo nacional. Use 'Sim' ou 'Não'.",
        },
    )
