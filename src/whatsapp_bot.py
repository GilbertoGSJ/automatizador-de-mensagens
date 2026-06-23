import logging
import requests

from src.config import (
    ZAPI_ID,
    ZAPI_TOKEN
)
# Enviará a mensagem ao numero de contato, utilizando o url do Z-API.
def enviar_mensagem(telefone: str, nome: str) -> bool:
    #
    url = (
        f"https://api.z-api.io/instances/{ZAPI_ID}/token/{ZAPI_TOKEN}/send-text"
    )
    texto = f"Olá, {nome} tudo bem com você?"

    mensagem = {"phone": telefone,
                "message": texto}

    payload = {"phone": telefone,
                "message": texto
    }
    try:
        response = requests.post(url,json=payload,timeout= 10)
        response.raise_for_status()

        logging.info(f"Mensagem enviada para o contato, {nome}")
        return True

    except requests.exceptions.RequestException as error:
        logging.error(f"Falha ao enviar mensagem para o contato {nome}: {error}")
        return False
