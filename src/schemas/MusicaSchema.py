from marshmallow import Schema, fields, validate, post_load
from src.models.Musica import Musica
from src.schemas.ArtistaSchema import ArtistaSchema


class MusicaSchema(Schema):
    id = fields.Int()

    nome = fields.Str(
        required=True,
        validate=validate.Length(
            min=1, max=63, error="O nome deve ter no máximo 63 caracteres."
        ),
        error_messages={
            "required": "O nome da música é obrigatório.",
            "validator_failed": "O nome da música deve conter entre 1 e 63 caracteres.",
        },
    )

    artista_id = fields.Int(
        required=True, error_messages={"required": "Você deve escolher um artista."}
    )

    artista = fields.Nested(ArtistaSchema)

    @post_load
    def make_musica(self, data, **kwargs) -> Musica:
        return Musica(**data)
