import requests

cep = input("Digite seu CEP: ")
url = f"https://viacep.com.br/ws/{cep}/json/"

dados = requests.get(url)
resposta = dados.json()

print(f"Voce mora na cidade de {resposta['localidade']}", "no estado de", resposta["uf"], "no bairro", resposta["bairro"], "na rua", resposta["logradouro"])

