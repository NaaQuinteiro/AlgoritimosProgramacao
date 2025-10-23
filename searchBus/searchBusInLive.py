import os
from folium import Map, Marker
import requests
from dotenv import load_dotenv

load_dotenv("C:/Users/thayna_quinteiro/Desktop/AlgoritimosProgramação/.env")

s = requests.Session()
x = s.post(
    f"http://api.olhovivo.sptrans.com.br/v2.1/Login/Autenticar?token={os.getenv('SPTRANS_TOKEN')}"
)

position = s.get(
    "http://api.olhovivo.sptrans.com.br/v2.1/Posicao/Linha?codigoLinha=2506"
)
teste = position.json()

print(teste)

teste = teste["vs"]

print(teste)


m = Map(location=[teste[0]["py"], teste[0]["px"]], zoom_start=14)

for i in teste:
    Marker(location=[i["py"], i["px"]], popup=i["p"]).add_to(m)
m.show_in_browser()

