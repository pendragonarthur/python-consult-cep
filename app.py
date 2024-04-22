import requests


def get_cep():
    try:

        cep = input("Insira o CEP: ")

        response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")

        if response.status_code == 200:
            data = response.json()
            print(data)
        else: 
            print(f"Falha na request. Código do erro: {response.status_code}")

    except Exception as e:
        print(f"Error: {e}")

get_cep()