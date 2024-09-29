import folium
import requests
import os

# Certifique-se de que a pasta "mapas" exista
if not os.path.exists('mapas'):
    os.makedirs('mapas')

# URL do JSON de perímetros das cidades
url = "https://ceabpwveoyteuobjpmbg.supabase.co/storage/v1/object/sign/JSON/cidades.json?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJKU09OL2NpZGFkZXMuanNvbiIsImlhdCI6MTcyNzYzMTk1NCwiZXhwIjoxNzU5MTY3OTU0fQ.lYRvRAaM8N7lKlfV0n0LiszhZb8_d48Bt56_cHjX8FA&t=2024-09-29T17%3A45%3A54.079Z"

# Fazendo o download do JSON
response = requests.get(url)
data = response.json()

# Cria um mapa centralizado em uma coordenada específica (ex: região das cidades)
mapa = folium.Map(location=[-22.7594, -43.4511], zoom_start=12)

# Adiciona o GeoJson com os perímetros das cidades ao mapa
folium.GeoJson(data).add_to(mapa)

# Define o caminho para salvar o mapa
caminho_mapa = 'mapas/mapa_cidades.html'

# Salva o mapa como um arquivo HTML na pasta "mapas"
mapa.save(caminho_mapa)

print(f"Mapa salvo em: {caminho_mapa}")
