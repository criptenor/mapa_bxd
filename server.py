import folium
import os

# Certifique-se de que a pasta "mapas" exista
if not os.path.exists('mapas'):
    os.makedirs('mapas')

# Cria um mapa centralizado em uma coordenada específica (ex: Baixada Fluminense)
mapa = folium.Map(location=[-22.7594, -43.4511], zoom_start=12)

# Adiciona um marcador ao mapa (opcional)
folium.Marker(location=[-22.7594, -43.4511], popup='Baixada Fluminense').add_to(mapa)

# Define o caminho para salvar o mapa
caminho_mapa = 'mapas/mapa_baixada.html'

# Salva o mapa como um arquivo HTML na pasta "mapas"
mapa.save(caminho_mapa)

print(f"Mapa salvo em: {caminho_mapa}")
