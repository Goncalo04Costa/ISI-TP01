import os
import tweepy
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv('../secret.env')

# Pega os valores do .env
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_secret = os.getenv("ACCESS_SECRET")
bearer_token = os.getenv("BEARER_TOKEN")

# Verificar se as credenciais foram carregadas corretamente
if not (api_key and api_secret and access_token and access_secret and bearer_token):
    print("Uma ou mais credenciais não foram encontradas.")
else:
    print("Credenciais carregadas com sucesso.")

# Autenticar com as chaves
client = tweepy.Client(bearer_token=bearer_token, 
                       consumer_key=api_key, 
                       consumer_secret=api_secret, 
                       access_token=access_token, 
                       access_token_secret=access_secret)

# Teste simples para verificar a conexão
try:
    user = client.get_me()
    print(f"Usuário autenticado: {user.data.username}")
except Exception as e:
    print(f"Erro ao buscar informações do usuário: {e}")

# Definir a query
query = "#Eleições2024"

# Fazer a pesquisa
try:
    tweets = client.search_recent_tweets(query=query, max_results=10)
    
    # Verificar se tweets foram encontrados
    if tweets.data:
        # Iterar sobre os tweets e imprimi-los
        for tweet in tweets.data:
            print(f"{tweet.id} - {tweet.text}")
    else:
        print("Nenhum tweet encontrado.")
except tweepy.errors.Forbidden as e:
    print("Acesso negado: ", e)
except tweepy.errors.Unauthorized as e:
    print("Não autorizado: ", e)
except Exception as e:
    print(f"Erro ao buscar tweets: {e}")
