import requests
from datetime import datetime, timedelta

def cotar(data):
  url = fr"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='{data}'&$format=json"
  res = requests.get(url)
  res = res.json()
  if not res['value']: 
    dia_anterior = datetime.strptime(data, "%m%d%Y") - timedelta(1) #strptime transforma string em data, timedelta retorna um dia
    dia_anterior = datetime.strftime(dia_anterior, "%m%d%Y") #strftime transforma data em string
    return cotar(dia_anterior)
  else:
    return res["value"][0]["cotacaoVenda"]

print([cotar(i) for i in ["09022024", "09012024", "08312024", "08302024", "08292024"]])