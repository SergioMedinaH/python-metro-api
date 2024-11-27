import networkx as nx
import matplotlib.pyplot as plt
import math
from pprint import pprint 
import pandas as pd
import os


ruta_csv = "C:\\Users\\nieve\\Desktop\\Inteligencia artificial\\TrabajoMetroBuenosAires\\paradas.csv"

paradas = []

'''
# Ruta al archivo CSV
base_dir = os.path.dirname(os.path.abspath(_file_))
csv_path = os.path.join(base_dir, '..', 'data', 'paradas.csv')
'''

# Cargar el CSV en un DataFrame y convertirlo a lista de diccionarios
df = pd.read_csv(ruta_csv)
paradas = df.to_dict(orient='records')

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

G1 = nx.Graph()
# linea A
G1.add_edge("alberti", "pasco", weight=calcular_distancia("alberti", "pasco"))
G1.add_edge("pasco", "congreso", weight=calcular_distancia("pasco", "congreso"))
G1.add_edge("congreso", "saenzpena", weight=calcular_distancia("congreso", "saenzpena"))
G1.add_edge("saenzpena", "lima", weight=calcular_distancia("saenzpena", "lima"))
G1.add_edge("lima", "piedras", weight=calcular_distancia("lima", "piedras"))
G1.add_edge("piedras", "peru", weight=calcular_distancia("piedras", "peru"))
G1.add_edge("peru", "plzmayo", weight=calcular_distancia("peru", "plzmayo"))

# linea B
G1.add_edge("pasteur", "callaomaestro", weight=calcular_distancia("pasteur", "callaomaestro"))
G1.add_edge("callaomaestro", "uruguay", weight=calcular_distancia("callaomaestro", "uruguay"))
G1.add_edge("uruguay", "carlospellegrini", weight=calcular_distancia("uruguay", "carlospellegrini"))
G1.add_edge("carlospellegrini", "florida", weight=calcular_distancia("carlospellegrini", "florida"))
G1.add_edge("florida", "leandro", weight=calcular_distancia("florida", "leandro"))

# linea C
G1.add_edge("constitucion", "sanjuan", weight=calcular_distancia("constitucion", "sanjuan"))
G1.add_edge("sanjuan", "independencia", weight=calcular_distancia("sanjuan", "independencia"))
G1.add_edge("independencia", "moreno", weight=calcular_distancia("independencia", "moreno"))
G1.add_edge("moreno", "avdemayoc", weight=calcular_distancia("moreno", "avdemayoc"))
G1.add_edge("avdemayoc", "diagonal", weight=calcular_distancia("avdemayoc", "diagonal"))
G1.add_edge("diagonal", "lavalle", weight=calcular_distancia("diagonal", "lavalle"))
G1.add_edge("lavalle", "sanmartin", weight=calcular_distancia("lavalle", "sanmartin"))
G1.add_edge("sanmartin", "reitroc", weight=calcular_distancia("sanmartin", "reitroc"))

# linea D 
G1.add_edge("facultadmedicina", "callao", weight=calcular_distancia("facultadmedicina", "callao"))
G1.add_edge("callao", "tribunales", weight=calcular_distancia("callao", "tribunales"))
G1.add_edge("tribunales", "9dejulio", weight=calcular_distancia("tribunales", "9dejulio"))
G1.add_edge("9dejulio", "catedral", weight=calcular_distancia("9dejulio", "catedral"))

# linea E
G1.add_edge("pichincha", "entrerio-rodolfowalsh", weight=calcular_distancia("pichincha", "entrerio-rodolfowalsh"))
G1.add_edge("entrerio-rodolfowalsh", "sanjose", weight=calcular_distancia("entrerio-rodolfowalsh", "sanjose"))
G1.add_edge("sanjose", "independenciae", weight=calcular_distancia("sanjose", "independenciae"))
G1.add_edge("independenciae", "belgrano", weight=calcular_distancia("independenciae", "belgrano"))
G1.add_edge("belgrano", "bolivar", weight=calcular_distancia("belgrano", "bolivar"))
G1.add_edge("bolivar", "correocentral", weight=calcular_distancia("bolivar", "correocentral"))
G1.add_edge("correocentral", "catalinas", weight=calcular_distancia("correocentral", "catalinas"))
G1.add_edge("catalinas", "retiroe", weight=calcular_distancia("catalinas", "retiroe"))


def hora_a_segundos(hora):
    horas, minutos = map(int, hora.split(":"))
    return horas * 3600 + minutos * 60


def segundos_a_hora(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    return f"{horas:02}:{minutos:02}"


def heuristica(paradaActual: str, paradaDestino: str) -> float:
    """Calcula la distancia en línea recta entre la parada actual y la parada destino."""
    return calcular_distancia(paradaActual, paradaDestino)


def separar_por_lineas(paradas):
    lineas = {}

    for parada in paradas:
        parada1 = encontrar_parada(parada)
        if parada1:
            linea = parada1["linea"]
        if linea not in lineas:
            lineas[linea] = []
        lineas[linea].append(parada)

    return lineas


def tiempo_espera(paradaActual: str, direccion: str, hora_actual_segundos: int):
    parada = encontrar_parada(paradaActual)
    hora_inicio_parada = hora_a_segundos(parada[direccion])
    tiempo_espera = 0
    while hora_inicio_parada < hora_actual_segundos:
        #CAMBIAR A SEGUNDOS EN CSV ------------------------------------------------------------------------------------------
        hora_inicio_parada += parada["frecuencia"]*60
    tiempo_espera = abs(hora_actual_segundos - hora_inicio_parada)
    return tiempo_espera, segundos_a_hora(hora_inicio_parada)

def obtenerTiempoTransbordo(parada1, parada2):
    nombre = f"{parada1["value"]}-{parada2["value"]}"
    transbordos = { 
    "independencia-independenciae" : 170,
    "independenciae-independencia" : 170,

    "peru-bolivar": 170,
    "bolivar-peru": 170,

    "peru-catedral": 170,
    "catedral-peru": 170,

    "lima-avdemayo": 170,
    "avdemayo-lima": 170,

    "diagonal-9dejulio": 170,
    "9dejulio-diagonal": 170,

    "9dejulio-carlospellegrini": 170,
    "carlospellegrini-9dejulio": 170,

    "retiroc-retiroe": 170,
    "retiroe-retiroc": 170
    }
    return transbordos[nombre]


def get_trayectos(ruta):
    
    # Convertir los valores de las paradas a objetos parada completos
    paradas_ruta = [encontrar_parada(valor) for valor in ruta]
    
    if paradas_ruta and len(paradas_ruta) > 0:
        trayectos = []
        trayecto_actual = {
            "linea": paradas_ruta[0]["linea"],
            "paradas": [paradas_ruta[0]],
            "tiempos": [],
            "tiempoEspera": 0,
            "horaSalida": "00:00",
            "tiempoEsperaSalida" : 0,
            "horaFin": "00:00",
            "direccion": ""
        }
        
        for index, parada in enumerate(paradas_ruta):
            if index == 0:
                continue
            
            parada_anterior = paradas_ruta[index - 1]
            
            if parada["linea"] == parada_anterior["linea"]:
                trayecto_actual["paradas"].append(parada)
                if parada_anterior["IDs"] < parada["IDs"]:
                    #hacia derecha
                    trayecto_actual["tiempos"].append(parada_anterior["tiempoASiguiente"])
                    trayecto_actual["direccion"] = "hacia_derecha"
                else:
                    trayecto_actual["tiempos"].append(parada_anterior["tiempoAAnterior"])
                    trayecto_actual["direccion"] = "hacia_izquierda"
                
            else:
                trayectos.append(trayecto_actual)
                trayectos.append({
                    "linea": "Transbordo",
                    "paradas": [parada_anterior, parada],
                    "tiempos": [obtenerTiempoTransbordo(parada_anterior, parada)]
                })
                trayecto_actual = {
                    "linea": parada["linea"],
                    "paradas": [parada],
                    "tiempos": [],
                    "tiempoEspera": 0,
                    "horaSalida": "00:00",
                    "tiempoEsperaSalida" : 0,
                    "horaFin": "00:00",
                    "direccion": ""
                }
        
        trayectos.append(trayecto_actual)
    
    return trayectos


def calcularRuta(origen: str, destino: str, hora_actual, priorizarTransbordos: bool):

    if priorizarTransbordos:
        G1.add_edge("independencia", "independenciae", weight=99999)
        G1.add_edge("peru", "bolivar", weight=99999)
        G1.add_edge("peru", "catedral", weight=99999)
        G1.add_edge("lima", "avdemayo", weight=99999)
        G1.add_edge("diagonal", "9dejulio", weight=99999)
        G1.add_edge("9dejulio", "carlospellegrini", weight=99999)
        G1.add_edge("retiroc", "retiroe", weight=99999)
    else:
        G1.add_edge("independencia", "independenciae", weight=1)
        G1.add_edge("peru", "bolivar", weight=2)
        G1.add_edge("peru", "catedral", weight=2)
        G1.add_edge("lima", "avdemayo", weight=2)
        G1.add_edge("diagonal", "9dejulio", weight=2)
        G1.add_edge("9dejulio", "carlospellegrini", weight=2)
        G1.add_edge("retiroc", "retiroe", weight=2)

    ruta = nx.astar_path(G1, origen, destino, heuristic=heuristica, weight="weight")

    trayectos = get_trayectos(ruta)

    hora_actual_segundos_inicio = hora_a_segundos(hora_actual)
    hora_actual_segundos = hora_actual_segundos_inicio

    for linea in trayectos:
        if linea["linea"] != "Transbordo":
            if len(linea["paradas"]) >1:
                linea["tiempoEspera"], linea["horaSalida"] = tiempo_espera(linea["paradas"][0]["value"], linea["direccion"], hora_actual_segundos)


                #ACTUALIZAR SI UTILIZAMOS SEGUNDOS (CVS MAKAR)---------------------------------------------------------------------------------------------------------------------
            
                duracion_linea_segundos = sum(list(map(lambda x: hora_a_segundos(x) ,linea["tiempos"])))
                hora_actual_segundos += linea["tiempoEspera"]
                hora_actual_segundos += duracion_linea_segundos

                linea["tiempoEsperaSalida"] = linea["tiempoEspera"] + duracion_linea_segundos
                linea["horaFin"] = segundos_a_hora(hora_actual_segundos)

        else:
            hora_actual_segundos += sum(linea["tiempos"])

    return trayectos

pprint(calcularRuta("alberti", "pasco", "5:36", False))

