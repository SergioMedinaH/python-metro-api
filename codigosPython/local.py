import networkx as nx
import matplotlib.pyplot as plt
import math
from pprint import pprint

paradas = [
    # Línea A
    { "value": "alberti", "label": "Alberti", "lat": -34.6098887, "lng": -58.4008674, "linea": "A" },
    { "value": "pasco", "label": "Pasco", "lat": -34.6095527, "lng": -58.3983828, "linea": "A" },
    { "value": "congreso", "label": "Congreso", "lat": -34.6092415, "lng": -58.3926706, "linea": "A" },
    { "value": "saenzpena", "label": "Sáenz Peña", "lat": -34.6094200, "lng": -58.3866700, "linea": "A" },
    { "value": "lima", "label": "Lima", "lat": -34.6091054, "lng": -58.3825208, "linea": "A" },
    { "value": "piedras", "label": "Piedras", "lat": -34.608837932068, "lng": -58.378502407734, "linea": "A" },
    { "value": "peru", "label": "Perú", "lat": -34.6085633, "lng": -58.3744662, "linea": "A" },
    { "value": "plzmayo", "label": "Plaza de Mayo Casa Rosada", "lat": -34.6086997, "lng": -58.3714911, "linea": "A" },

    # Línea B
    { "value": "pasteur", "label": "Pasteur AMIA", "lat": -34.604623105662, "lng": -58.399357348627, "linea": "B" },
    { "value": "callaomaestro", "label": "Callao Maestro A. Bravo", "lat": -34.6045542, "lng": -58.3931682, "linea": "B" },
    { "value": "uruguay", "label": "Uruguay", "lat": -34.604046341872, "lng": -58.392845615810, "linea": "B" },
    { "value": "carlospellegrini", "label": "Carlos Pellegrini", "lat": -34.6034877, "lng": -58.3807319, "linea": "B" },
    { "value": "florida", "label": "Florida", "lat": -34.6033000, "lng": -58.3745300, "linea": "B" },
    { "value": "leandro", "label": "Leandro N. Alem", "lat": -34.6030011, "lng": -58.3706754, "linea": "B" },

    # Línea C
    { "value": "constitucion", "label": "Constitución", "lat": -34.6275021, "lng": -58.3824531, "linea": "C" },
    { "value": "sanjuan", "label": "San Juan", "lat": -34.622676270600, "lng": -58.379951566484, "linea": "C" },
    { "value": "independencia", "label": "Independencia", "lat": -34.6200717, "lng": -58.3837130, "linea": "C" },
    { "value": "moreno", "label": "Moreno", "lat": -34.612434686061, "lng": -58.380517847867, "linea": "C" },
    { "value": "avdemayo", "label": "Avenida de Mayo", "lat": -34.60899098, "lng": -58.38068279, "linea": "C" },
    { "value": "diagonal", "label": "Diagonal Norte", "lat": -34.6048383, "lng": -58.3794651, "linea": "C" },
    { "value": "lavalle", "label": "Lavalle", "lat": -34.594872221186, "lng": -58.378115594396, "linea": "C" },
    { "value": "sanmartin", "label": "General San Martín", "lat": -34.6008090, "lng": -58.3848683, "linea": "C" },
    { "value": "retiroc", "label": "Retiro", "lat": -34.5916364, "lng": -58.3748868, "linea": "C" },

    # Línea D
    { "value": "facultadmedicina", "label": "Facultad de Medicina", "lat": -34.5997270, "lng": -58.3972006, "linea": "D" },
    { "value": "callao", "label": "Callao", "lat": -34.5996286, "lng": -58.3925590, "linea": "D" },
    { "value": "tribunales", "label": "Tribunales Teatro Colon", "lat": -34.6015524, "lng": -58.3850202, "linea": "D" },
    { "value": "9dejulio", "label": "9 de Julio", "lat": -34.6044707, "lng": -58.3801163, "linea": "D" },
    { "value": "catedral", "label": "Catedral", "lat": -34.6076198, "lng": -58.3742565, "linea": "D" },

    # Línea E
    { "value": "pichincha", "label": "Pichincha", "lat": -34.6232753, "lng": -58.3995216, "linea": "E" },
    { "value": "entrerios-rodolfowalsh", "label": "Entre Ríos - Rodolfo Walsh", "lat": -34.6229760, "lng": -58.3938755, "linea": "E" },
    { "value": "sanjose", "label": "San José", "lat": -34.6222576, "lng": -58.3877218, "linea": "E" },
    { "value": "independenciae", "label": "Independencia", "lat": -34.6180704, "lng": -58.3834729, "linea": "E" },
    { "value": "belgrano", "label": "Belgrano", "lat": -34.6124483, "lng": -58.3810317, "linea": "E" },
    { "value": "bolivar", "label": "Bolívar", "lat": -34.6094245, "lng": -58.3762727, "linea": "E" },
    { "value": "correocentral", "label": "Correo Central", "lat": -34.6031305, "lng": -58.3729475, "linea": "E" },
    { "value": "catalinas", "label": "Catalinas", "lat": -34.5965586, "lng": -58.3745719, "linea": "E" },
    { "value": "retiroe", "label": "Retiro", "lat": -34.5916364, "lng": -58.3748868, "linea": "E" }
]



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
    return distancia


def heuristica(paradaActual: str, paradaDestino: str) -> float:
    """Calcula la distancia en línea recta entre la parada actual y la parada destino."""
    return calcular_distancia(paradaActual, paradaDestino)


def calcularRuta(origen: str, destino: str):
    # Realizar la suma
    ruta = nx.astar_path(G1, origen, destino, heuristic=heuristica, weight="weight")
    tiempos = [G1[ruta[i]][ruta[i+1]]["weight"] for i in range(len(ruta) - 1)]
    return (ruta, tiempos)


def hora_salida(hora_ini:int , hora_empiece_linea: int, hora_cierre_linea: int, intervalo_frecuencia: int) -> int:
    hora = hora_empiece_linea
    while hora_ini > hora:
        hora += intervalo_frecuencia
    if hora > hora_cierre_linea:
        return -1
    return hora

def get_trayectos(resultado):
    # Desempaquetar la tupla resultado
    paradas_ruta_valores, tiempos = resultado
    
    # Convertir los valores de las paradas a objetos parada completos
    paradas_ruta = [encontrar_parada(valor) for valor in paradas_ruta_valores]
    
    if paradas_ruta and len(paradas_ruta) > 0:
        trayectos = []
        trayecto_actual = {
            "linea": paradas_ruta[0]["linea"],
            "paradas": [paradas_ruta[0]],
            "tiempos": []
        }
        
        for index, parada in enumerate(paradas_ruta):
            if index == 0:
                continue
            
            parada_anterior = paradas_ruta[index - 1]
            
            if parada["linea"] == parada_anterior["linea"]:
                trayecto_actual["paradas"].append(parada)
                trayecto_actual["tiempos"].append(tiempos[index - 1])
            else:
                trayectos.append(trayecto_actual)
                trayectos.append({
                    "linea": "Transbordo",
                    "paradas": [parada_anterior, parada],
                    "tiempos": [tiempos[index - 1]]
                })
                trayecto_actual = {
                    "linea": parada["linea"],
                    "paradas": [parada],
                    "tiempos": []
                }
        
        trayectos.append(trayecto_actual)
    
    return trayectos

pprint(get_trayectos(calcularRuta("alberti", "retiroc")))



