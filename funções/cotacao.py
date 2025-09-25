import requests

def cotar(data):
    url = f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?%40dataCotacao='{data}'&%24format=json"
    res = requests.get(url)
    res = res.json()

    values = {}
    

    values["Venda"] = res['value'][0]['cotacaoVenda']
    values["Compra"] = res['value'][0]['cotacaoCompra']

    return values

print(cotar("08282024"))