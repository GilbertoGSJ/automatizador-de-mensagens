import logging
from supabase import create_client

from src.config import SUPABASE_URL,SUPABASE_KEY

#Busca por contatos no banco de dados do Supabase, com base no max_contatos, 3 por padrão.
def obter_contatos(max_contatos: int = 3) -> list:
    try:
        supabase_client = create_client(str(SUPABASE_URL),str(SUPABASE_KEY))

        response = (supabase_client.table("contatos").select("*").limit(max_contatos).execute())

        return response.data

    except Exception as error:
        logging.error(f"Erro ao buscar contatos: {error}")
        return []