import yaml
import asyncpraw
import pandas as pd
from datetime import datetime
from langdetect import detect, LangDetectException
import asyncio

def carregar_config_yaml(caminho_arquivo='config.yaml'):
    """
    Lê o arquivo YAML especificado e retorna seu conteúdo como um dicionário.
    
    :param caminho_arquivo: Caminho para o arquivo YAML.
    :return: Dicionário com os dados do arquivo.
    """
    with open(caminho_arquivo, 'r') as arquivo:
        config = yaml.safe_load(arquivo)
    return config

config = carregar_config_yaml('config.yaml')

#Função que converte o período desejado para o formato UNIX
def period(data, hora):
  periodo_p_conversao = data+'T'+hora+'+00:00'
  periodo=datetime.fromisoformat(periodo_p_conversao).timestamp()
  return str(int(periodo))

#Aplicação da função para os parâmetros AFTER e BEFORE
after=period(config['period']['data_inicial'],config['period']['hora_inicial'])
before=period(config['period']['data_final'],config['period']['hora_final'])

async def scrape_random_users_posts(start_timestamp, end_timestamp, idioma_alvo='en',
                                     subreddit_name='all', post_limit=50, user_posts_limit=1000):
    posts_data = []

    async with asyncpraw.Reddit(
        client_id=config['user_settings']['client_id'],
        client_secret=config['user_settings']['client_secret'],
        user_agent=config['user_settings']['user_agent']
    ) as reddit:

        subreddit = await reddit.subreddit(subreddit_name)

        async for submission in subreddit.new(limit=post_limit):
            username = submission.author.name if submission.author else None
            if not username:
                continue

            try:
                redditor = await reddit.redditor(username)
                async for user_submission in redditor.submissions.new(limit=user_posts_limit):
                    if after <= user_submission.created_utc <= before:
                        texto = user_submission.selftext or user_submission.title
                        try:
                            idioma = detect(texto)
                            if idioma != idioma_alvo:
                                continue
                        except LangDetectException:
                            continue

                        posts_data.append({
                            'Username': username,
                            'Date': datetime.utcfromtimestamp(user_submission.created_utc),
                            'Title': user_submission.title,
                            'Body': user_submission.selftext,
                            'URL': user_submission.url
                        })
            except Exception as e:
                print(f"Erro ao coletar posts do usuário {username}: {e}")
                continue

    return posts_data


def save_to_excel(posts_data, filename):
    df = pd.DataFrame(posts_data)
    df.to_excel(filename, index=False, engine='openpyxl')

if __name__ == '__main__':
    # Defina o intervalo desejado
    start = after # 31 de maio de 2021
    end = before    # 31 de agosto de 2022

    # Rodar o scraper e salvar o Excel
    posts = await scrape_random_users_posts(start, end, idioma_alvo='en') # Selecione o idioma alvo
    save_to_excel(posts, 'reddit_posts_filtrados.xlsx')
    print("Raspagem finalizada e arquivo salvo com sucesso!")
