import requests
import json

# URL do arquivo JSON
url = "https://fgvqqqgcyujztipjpsta.supabase.co/storage/v1/object/public/base_dados/bairros.json?t=2024-09-29T18%3A24%3A01.550Z"

# Fazendo a requisição
response = requests.get(url)

# Verificando se a requisição foi bem-sucedida
if response.status_code == 200:
    # Carregando o conteúdo JSON
    data = response.json()
    
    # Processando e formatando os dados
    bairros_formatados = []
    for bairro in data:
        bairro_formatado = {
            "geometria": bairro.get("geometria"),  # Mantém a geometria como está
            "nome_vizinhanca": bairro.get("nome_vizinhanca"),
            "id_vizinhanca": bairro.get("id_vizinhanca"),
            "id_municipio": bairro.get("id_municipio")
        }
        bairros_formatados.append(bairro_formatado)

    # Convertendo para JSON
    json_output = json.dumps(bairros_formatados, indent=2)
    print(json_output)

else:
    print(f"Erro ao acessar o link: {response.status_code}")
