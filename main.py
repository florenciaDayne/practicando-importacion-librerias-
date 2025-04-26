import os

import requests

from dotenv import load_dotenv



# Cargar las variables de entorno desde el archivo .env

load_dotenv()



# Obtener API Key y Search Engine ID desde las variables de entorno

API_KEY = os.getenv("API_KEY_SEARCH_GOOGLE")

SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")



# Validar que las claves existen

if not API_KEY or not SEARCH_ENGINE_ID:

  print("ERROR: Faltan API_KEY_SEARCH_GOOGLE o SEARCH_ENGINE_ID en el archivo .env")

  exit(1)



# Parámetros de búsqueda

query = 'filetype:sql "MySQL dump" (pass|password|passwd|pwd)'

lang = 'lang_es'

start_index = 1



# Construcción de la URL

url = (

  "https://www.googleapis.com/customsearch/v1"

  f"?key={API_KEY}"

  f"&cx={SEARCH_ENGINE_ID}"

  f"&q={query}"

  f"&start={start_index}"

  f"&lr={lang}"

)



try:

  # Hacer la solicitud a la API

  response = requests.get(url)

  response.raise_for_status() # Lanza excepción si hubo error HTTP

  data = response.json()



  # Obtener los resultados

  items = data.get("items", [])

  if not items:

    print("No se encontraron resultados.")

  else:

    for item in items:

      title = item.get("title", "Sin título")

      link = item.get("link", "Sin enlace")

      snippet = item.get("snippet", "Sin descripción")



      print(f"Title: {title}")

      print(f"Link: {link}")

      print(f"Snippet: {snippet}")

      print("-" * 80)



except requests.exceptions.RequestException as e:

  print(f"Error al realizar la solicitud: {e}")

except ValueError:

  print("Error al interpretar la respuesta JSON.")