from http.server import BaseHTTPRequestHandler
import json
from urllib.parse import urlparse, parse_qs

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        # Parsear los parámetros de la URL
        query = urlparse(self.path).query
        params = parse_qs(query)
        
        # Verificar que se reciban los parámetros "valor1" y "valor2"
        if 'valor1' in params and 'valor2' in params:
            try:
                # Convertir los valores a enteros
                valor1 = int(params['valor1'][0])
                valor2 = int(params['valor2'][0])

                # Realizar la suma
                resultado = valor1 + valor2

                # Crear el diccionario de respuesta en JSON
                response = {'resultado': resultado}

                # Enviar la respuesta con el resultado en formato JSON
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(response).encode('utf-8'))
            except ValueError:
                # Manejar errores de conversión a entero
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': 'Los valores deben ser enteros'}).encode('utf-8'))
        else:
            # Si faltan los parámetros
            self.send_response(400)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'error': 'Faltan parámetros valor1 y valor2'}).encode('utf-8'))
