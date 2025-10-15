import os
from folium import Map, Marker
import requests
from dotenv import load_dotenv

load_dotenv("C:/Users/thayna_quinteiro/Desktop/AlgoritimosProgramação/searchBus/.env")

s = requests.Session()
x = s.post(
    f"http://api.olhovivo.sptrans.com.br/v2.1/Login/Autenticar?token={os.getenv('SPTRANS_TOKEN')}"
)

print(x.text)

linhas_lapa = s.get(
    "http://api.olhovivo.sptrans.com.br/v2.1/Linha/Buscar?termosBusca=Guilherme"
)
linhas_lapa = linhas_lapa.json()
linhas_lapa[:3]

print(linhas_lapa[:3])


res = s.get(
    "http://api.olhovivo.sptrans.com.br/v2.1/Parada/BuscarParadasPorLinha?codigoLinha=2506"
)
paradas = res.json()
paradas[:3]

print(paradas[:3])
print(paradas)

m = Map(location=[paradas[3]["py"], paradas[3]["px"]], zoom_start=14)

for i in paradas:
    Marker(location=[i["py"], i["px"]], popup=i["np"]).add_to(m)
m.show_in_browser()