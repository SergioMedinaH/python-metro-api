from http.server import BaseHTTPRequestHandler
import json
import networkx as nx
import math
from urllib.parse import urlparse, parse_qs
import os
import pandas as pd


paradas = []

# Ruta al archivo CSV
base_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_dir, '..', 'data', 'paradas.csv')

# Cargar el CSV en un DataFrame y convertirlo a lista de diccionarios
df = pd.read_csv(csv_path)
paradas = df.to_dict(orient='records')


G1 = nx.Graph()
# linea A
G1.add_edge("alberti", "pasco", weight=2)
G1.add_edge("pasco", "congreso", weight=2)
G1.add_edge("congreso", "saenzpena", weight=2)
G1.add_edge("saenzpena", "lima", weight=2)
G1.add_edge("lima", "piedras", weight=2)
G1.add_edge("piedras", "peru", weight=2)
G1.add_edge("peru", "plzmayo", weight=2)

# linea B
G1.add_edge("pasteur", "callaomaestro", weight=1)
G1.add_edge("callaomaestro", "uruguay", weight=1)
G1.add_edge("uruguay", "carlospellegrini", weight=1)
G1.add_edge("carlospellegrini", "florida", weight=1)
G1.add_edge("florida", "leandro", weight=1)

# linea C
G1.add_edge("constitucion", "sanjuan", weight=2)
G1.add_edge("sanjuan", "independencia", weight=1)
G1.add_edge("independencia", "moreno", weight=1)
G1.add_edge("moreno", "avdemayoc", weight=1)
G1.add_edge("avdemayoc", "diagonal", weight=1)
G1.add_edge("diagonal", "lavalle", weight=1)
G1.add_edge("lavalle", "sanmartin", weight=2)
G1.add_edge("sanmartin", "reitroc", weight=1)

# linea D 
G1.add_edge("facultadmedicina", "callao", weight=1)
G1.add_edge("callao", "tribunales", weight=2)
G1.add_edge("tribunales", "9dejulio", weight=1)
G1.add_edge("9dejulio", "catedral", weight=2)

# linea E
G1.add_edge("pichincha", "entrerio-rodolfowalsh", weight=1)
G1.add_edge("entrerio-rodolfowalsh", "sanjose", weight=1)
G1.add_edge("sanjose", "independenciae", weight=2)
G1.add_edge("independenciae", "belgrano", weight=2)
G1.add_edge("belgrano", "bolivar", weight=1)
G1.add_edge("bolivar", "correocentral", weight=1)
G1.add_edge("correocentral", "catalinas", weight=1)
G1.add_edge("catalinas", "retiroe", weight=2)

# transbordos 
G1.add_edge("independencia", "independenciae", weight=1)
G1.add_edge("peru", "bolivar", weight=2)
G1.add_edge("peru", "catedral", weight=2)
G1.add_edge("lima", "avdemayo", weight=2)
G1.add_edge("diagonal", "9dejulio", weight=2)
G1.add_edge("9dejulio", "carlospellegrini", weight=2)
G1.add_edge("retiroc", "retiroe", weight=2)


def encontrar_parada(value):
    """Devuelve la parada correspondiente al valor dado."""
    for parada in paradas:
        if parada["value"] == value:
            return parada
    return None


def calcular_distancia(parada1: str, parada2: str) -> float:
    """Calcula la distancia en línea recta entre dos paradas utilizando sus latitudes y longitudes."""
    p1 = encontrar_parada(parada1)
    p2 = encontrar_parada(parada2)
    
    # Si no se encuentran ambas paradas, retornar un valor alto (para evitar un camino no válido)
    if not p1 or not p2:
        return float('inf')
    
    # Radio de la Tierra en kilómetros
    R = 6371.0

    # Convertir las coordenadas de grados a radianes
    lat1, lon1 = math.radians(p1["lat"]), math.radians(p1["lng"])
    lat2, lon2 = math.radians(p2["lat"]), math.radians(p2["lng"])

    # Diferencias
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Fórmula de Haversine
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Distancia en kilómetros
    distancia = R * c
    velocidad_promedio = 0.5
    tiempo = distancia / velocidad_promedio
    return tiempo


def heuristica(paradaActual: str, paradaDestino: str) -> float:
    """Calcula la distancia en línea recta entre la parada actual y la parada destino."""
    return calcular_distancia(paradaActual, paradaDestino)

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        # Parsear los parámetros de la URL
        query = urlparse(self.path).query
        params = parse_qs(query)
        
        # Verificar que se reciban los parámetros "paradaOrigen" y "paradaDestino"
        if 'paradaOrigen' in params and 'paradaDestino' in params and 'hora' in params and 'fecha' in params and 'prioridadTransbordos' in params:
            try:
                # Convertir los valores a enteros
                origen = params['paradaOrigen'][0]
                destino = params['paradaDestino'][0]
                hora = params['hora'][0] # formato HH:MM
                fecha = params['fecha'][0] # dia de la semana  0 - Domingo, 1 - Lunes, 2 - Martes, 3 - Miercoles, 4 - Jueves, 5 - Viernes, 6 - Sabado
                prioridadTransbordos = params['prioridadTransbordos'][0] # booleano

                # Realizar la suma
                ruta = nx.astar_path(G1, origen, destino, heuristic=heuristica, weight="weight")
                tiempos = [G1[ruta[i]][ruta[i+1]]["weight"] for i in range(len(ruta) - 1)]

                # Crear el diccionario de respuesta en JSON
                response = {'ruta': ruta, 'tiempos': tiempos}

                # Enviar la respuesta con el resultado en formato JSON
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps(response).encode('utf-8'))
            except ValueError:
                # Manejar errores de conversión a entero
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': 'Los parametros son invalidos'}).encode('utf-8'))
        else:
            # Si faltan los parámetros
            self.send_response(400)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'error': 'Falta algún parámetro como paradaOrigen, paradaDestino, hora, fecha o prioridadTransbordos'}).encode('utf-8'))
