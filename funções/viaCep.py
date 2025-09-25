import requests

# Função que fará requisição à API
def consulta_cep(cep):
  url = f"https://viacep.com.br/ws/{cep}/json/"
  res = requests.get(url)
  res = res.json()
  return (res['logradouro'], res['uf'])

# Lista de CEPs para consulta
lista_cep = ["13186642",
             "13178574",
             "13188020",
             "13184321",
             "20720293"]

[consulta_cep(cep)[0] for cep in lista_cep if consulta_cep(cep)[1] == "SP"]