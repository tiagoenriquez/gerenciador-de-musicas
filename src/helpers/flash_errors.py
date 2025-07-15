from flask import flash
from marshmallow import ValidationError
from typing import cast

def exibir_primeiro_erro(e: ValidationError) -> None:
    mensagens = cast(dict[str, list[str]], e.messages)
    if mensagens:
        primeira = next(iter(mensagens.values()))[0]
        flash(primeira, "erro")
    else:
        flash("Erro de validação desconhecido.", "erro")
