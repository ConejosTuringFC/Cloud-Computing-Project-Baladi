# Cloud-Computing-Project-Baladi
Our cloud computing project at National Autonomous University of México. 

## Members
- Bialy Calderon - bialycalderonm@gmail.com
- Christian Morales - chrisimg06@gmail.com
- Jesus Almaguer - correodefinitivo97@gmail.com


This project pretends to use the NASA's API called APOD and show the astronomy picture of the day.

To better understand the project's architecture, here is a breakdown of the primary execution flow:


```python
import requests

URL = "https://api.nasa.gov/planetary/apod"
API_KEY = "Ly4WNI3SbtbqVch7GXNzn0MpJ5fzP2dfMBjdCzxL"

parametros = {
    "api_key": API_KEY,
    "thumbs": True
}

try:

    respuesta = requests.get(URL, params = parametros)
    respuesta.raise_for_status()

    datos = respuesta.json()

    titulo = datos.get("title")
    fecha = datos.get("date")
    url_imagen = datos.get("url")
    explicacion = datos.get("explanation")

    print(f"--- {titulo} ({fecha}) ---")
    print(f"Url de la imagen: {url_imagen}")
    print(f"\nDEscripcion : {explicacion}")

except requests.exceptions.RequestException as e:
    print(f"Error en la conexion: {e}")

if datos.get("media_type") == "image":
    imagen_bits = requests.get(url_imagen).content
    with open("foto_nasa_dia.jpg", "wb") as archivo:
        archivo.write(imagen_bits)
```