from marshmallow import Schema, fields


class TrechoSchema(Schema):
    trecho = fields.Str(
        required=True, error_messages={"required": "Você precisa digitar o trecho."}
    )
