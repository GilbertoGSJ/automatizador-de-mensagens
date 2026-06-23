import logging

from src.supabase_db import obter_contatos
from src.whatsapp_bot import enviar_mensagem

logging.basicConfig(level=logging.INFO,format="%(asctime)s - %(levelname)s - %(message)s")
logging.getLogger("httpx").setLevel(logging.WARNING)

def main():
    logging.info("Iniciando aplicação!")
    contatos = obter_contatos()

    if not contatos:
        logging.warning("Não existem contatos no seu banco de dados!")
        return

    logging.info(f"foram encontrados: {len(contatos)} contatos")
    mensagens_enviadas = 0
    for contato in contatos:
        nome = contato.get("nome")
        telefone = contato.get("telefone")

        if not nome or not telefone:
            logging.warning(f"Contato não encontrado: {contato}")
            continue

        mensagem = enviar_mensagem(telefone, nome)
        
        if mensagem:
            mensagens_enviadas += 1

    logging.info(
        f"{mensagens_enviadas} mensagem(ns) enviada(s) com sucesso!"
    )

if __name__ == '__main__':
    main()
