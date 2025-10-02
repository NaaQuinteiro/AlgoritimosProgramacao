import os
import requests
from dotenv import load_dotenv

load_dotenv("C:/Users/thayna_quinteiro/Desktop/AlgoritimosProgramação/searchBus/.env")

s = requests.Session()
x = s.post(
    f"http://api.olhovivo.sptrans.com.br/v2.1/Login/Autenticar?token={os.getenv('SPTRANS_TOKEN')}"
)

print(x.text)