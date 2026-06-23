# Desafio 2b2flow - Automação de contatos
<img src= "images/Python.png" height = 100>
<img src= "images/supabase.png" height = 100>
<img src= "images/zapi.png" height = 80>

![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Sobre
Um projeto de automação utilizando [Python](https://www.python.org), [Supabase](https://supabase.com) e [Z-API](https://z-api.io) que envia mensagens automáticas aos números dos contatos no banco de dados do Supabase, via Whatsapp. As mensagens são enviadas para cada contato da seguinte forma:
```
Olá, <nome_contato> tudo bem com você?
```
## Seções
Aqui estão ordenadas todas as seções do projeto:
- [Tecnologias e bibliotecas](#tecnologias-e-bibliotecas)
- [Diretórios](#diretórios)
- [Tabela do Supabase](#tabela-do-supabase)
- [Variáveis de ambiente](#variáveis-de-ambiente-env)
- [Instruções de Instalação](#instruções-de-instalação)

## Tecnologias e Bibliotecas
Aqui estão algumas das tecnologias e principais bibliotecas utilizadas no projeto:
- Python 3.14.0
- Supabase 2.31.0
- dotenv 0.9.9
- requests 2.34.2
- Z-API

## Diretórios
O diretório foi estruturado da seguinte forma:
```
Automatizador_de_mensagens/
├── main.py                 -> Script principal de execução
├── .env                    -> arquivo de variáveis de ambiente
├── README.md               -> Documentação explicativa do projeto
├── requirements.txt        -> Bibliotecas/Dependências necessárias para execução
└── src
    ├── config.py           -> Obtem as variáveis de ambiente do arquivo .env
    ├── database_db.py      -> Interage com o banco de dados do Supabase
    └── whatsapp_bot.py     -> Se com a Z-API para o envio de mensagens  
```
## Tabela do Supabase


Setup da tabela escrita no SQL editor do Supabase.
```sql
--Cria a tabela de contatos contendo o ID, nome, data de criação do contato e telefone.

create table Contatos (
  id bigint generated always as identity primary key,
  criado_em timestamp with time zone not null default now(),
  nome text not null,
  telefone text not null unique
);

--Insere os contatos ao table do banco de dados.

insert into contatos (nome, telefone) values
    ('Carlos Alvarez', '5561999998831'),
    ('Chico Santos', '5561999998822'),
    ('Leila Torres', '5561999998813');
```
## Variáveis de ambiente (.env)
Crie um arquivo `.env` na pasta raiz do projeto contendo as seguintes váriaveis.
| Variável      | Descrição             |
| ------------- | -------------         |
| SUPABASE_URL  | Seu url do Supabase   |
| SUPABASE_KEY  | Sua chave do Supabase |
| ZAPI_ID       | Seu ID do Z-API       |
| ZAPI_TOKEN    | Seu token do Z-API    |

## Instruções de Instalação
Após fazer o download do repositório, é necessário criar e rodar um ambiente virtual.

```bash
# Cria um ambiente virtual(venv) para o projeto com nome de ".venv".
python -m venv .venv

#Ativar o ambiente virtual
source .venv/bin/activate # Linux/Mac

.venv\Scripts\activate #Windows - Caso não o diretório não ative, use: .venv\bin\activate
```

```python
# Irá instalar todas as bibliotecas/dependências necessárias para o projeto. 
pip install -r requirements.txt

# Irá rodar o projeto.
python -m main
```
## License
O projeto é licenciado por [MIT License]().