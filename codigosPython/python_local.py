import networkx as nx
import matplotlib.pyplot as plt
import math
from pprint import pprint 
import pandas as pd
import os

paradas022494 = [

    # Línea A
    { "ID":0, "value": "alberti", "label": "Alberti", "lat": -34.6098887, "lng": -58.4008674, "linea": "A", "iniDer": 530, "iniIzq": 10, "frecuencia":4} ,
    { "ID":1, "value": "pasco", "label": "Pasco", "lat": -34.6095527, "lng": -58.3983828, "linea": "A", "iniDer": 533, "iniIzq": 10, "frecuencia":4  },
    { "ID":2, "value": "congreso", "label": "Congreso", "lat": -34.6092415, "lng": -58.3926706, "linea": "A", "iniDer": 536, "iniIzq": 10, "frecuencia":4  },
    { "ID":3, "value": "saenzpena", "label": "Sáenz Peña", "lat": -34.6094200, "lng": -58.3866700, "linea": "A", "iniDer": 539, "iniIzq": 10, "frecuencia":4  },
    { "ID":4, "value": "lima", "label": "Lima", "lat": -34.6091054, "lng": -58.3825208, "linea": "A", "iniDer": 542, "iniIzq": 10, "frecuencia":4  },
    { "ID":5, "value": "piedras", "label": "Piedras", "lat": -34.6092446, "lng": -58.3784204, "linea": "A", "iniDer": 545, "iniIzq": 10, "frecuencia":4  },
    { "ID":6, "value": "peru", "label": "Perú", "lat": -34.6085633, "lng": -58.3744662, "linea": "A", "iniDer": 548, "iniIzq": 10, "frecuencia":4  },
    { "ID":7, "value": "plzmayo", "label": "Plaza de Mayo Casa Rosada", "lat": -34.6086997, "lng": -58.3714911, "linea": "A", "iniDer": 551, "iniIzq": 10, "frecuencia":4  },

    # Línea B
    { "ID": 0, "value": "pasteur", "label": "Pasteur AMIA", "lat": -34.6054673, "lng": -58.4031439, "linea": "B", "iniDer": 520, "iniIzq": 540, "frecuencia": 4 },
    { "ID": 1, "value": "callaomaestro", "label": "Callao Maestro A. Bravo", "lat": -34.6045542, "lng": -58.3931682, "linea": "B", "iniDer": 525, "iniIzq": 545, "frecuencia": 4 },
    { "ID": 2, "value": "uruguay", "label": "Uruguay", "lat": -34.6051435, "lng": -58.3889597, "linea": "B", "iniDer": 530, "iniIzq": 550, "frecuencia": 4 },
    { "ID": 3, "value": "carlospellegrini", "label": "Carlos Pellegrini", "lat": -34.6034877, "lng": -58.3807319, "linea": "B", "iniDer": 535, "iniIzq": 555, "frecuencia": 4 },
    { "ID": 4, "value": "florida", "label": "Florida", "lat": -34.6033000, "lng": -58.3745300, "linea": "B", "iniDer": 540, "iniIzq": 560, "frecuencia": 4 },
    { "ID": 5, "value": "leandro", "label": "Leandro N. Alem", "lat": -34.6030011, "lng": -58.3706754, "linea": "B", "iniDer": 545, "iniIzq": 565, "frecuencia": 4 },


    # Línea C
    { "value": "constitucion", "label": "Constitución", "lat": -34.6275021, "lng": -58.3824531, "linea": "C" },
    { "value": "sanjuan", "label": "San Juan", "lat": -34.6242829, "lng": -58.3874077, "linea": "C" },
    { "value": "independencia", "label": "Independencia", "lat": -34.6200717, "lng": -58.3837130, "linea": "C" },
    { "value": "moreno", "label": "Moreno", "lat": -34.6103445, "lng": -58.3828383, "linea": "C" },
    { "value": "avdemayo", "label": "Avenida de Mayo", "lat": -34.60899098, "lng": -58.38068279, "linea": "C" },
    { "value": "diagonal", "label": "Diagonal Norte", "lat": -34.6048383, "lng": -58.3794651, "linea": "C" },
    { "value": "lavalle", "label": "Lavalle", "lat": -34.6020564, "lng": -58.3781247, "linea": "C" },
    { "value": "sanmartin", "label": "General San Martín", "lat": -34.6008090, "lng": -58.3848683, "linea": "C" },
    { "value": "retiroc", "label": "Retiro", "lat": -34.5916364, "lng": -58.3748868, "linea": "C" },

    # Línea D
    { "ID": 0, "value": "facultadmedicina", "label": "Facultad de Medicina", "lat": -34.5997270, "lng": -58.3972006, "linea": "D", "iniDer": 510, "iniIzq": 530, "frecuencia": 4 },
    { "ID": 1, "value": "callao", "label": "Callao", "lat": -34.5996286, "lng": -58.3925590, "linea": "D", "iniDer": 515, "iniIzq": 535, "frecuencia": 4 },
    { "ID": 2, "value": "tribunales", "label": "Tribunales Teatro Colon", "lat": -34.6015524, "lng": -58.3850202, "linea": "D", "iniDer": 520, "iniIzq": 540, "frecuencia": 4 },
    { "ID": 3, "value": "9dejulio", "label": "9 de Julio", "lat": -34.6044707, "lng": -58.3801163, "linea": "D", "iniDer": 525, "iniIzq": 545, "frecuencia": 4 },
    { "ID": 4, "value": "catedral", "label": "Catedral", "lat": -34.6076198, "lng": -58.3742565, "linea": "D", "iniDer": 530, "iniIzq": 550, "frecuencia": 4 },


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

ruta_csv = "C:\\Users\\marti\\OneDrive\\Documents\\VisualStudio\\IA\\paradas.csv"

paradas = []

'''
# Ruta al archivo CSV
base_dir = os.path.dirname(os.path.abspath(_file_))
csv_path = os.path.join(base_dir, '..', 'data', 'paradas.csv')
'''

# Cargar el CSV en un DataFrame y convertirlo a lista de diccionarios
df = pd.read_csv(ruta_csv)
paradas = df.to_dict(orient='records')


def hora_a_segundos(hora):
    horas, minutos = map(int, hora.split(":"))
    return horas * 3600 + minutos * 60


def segundos_a_hora(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    return f"{horas:02}:{minutos:02}"


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

pprint(calcularRuta("pasteur", "constitucion", "5:36", False))

