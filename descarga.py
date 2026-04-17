import requests
import os
import glob

URL = "https://api.nasa.gov/planetary/apod"
API_KEY = "Ly4WNI3SbtbqVch7GXNzn0MpJ5fzP2dfMBjdCzxL"

def descarga_multimedia(url_api, key_api):
    NOMBRE_BASE="archivo_descargado"
    headers ={
        'User-agent': 'Mozilla/5.0',
        'Authorization': f'Bearer {key_api}'
    }
    
    try:
        with requests.get(url_api, headers=headers, stream=True) as respuesta:
            respuesta.raise_for_status()
            
            contenido = respuesta.headers.get('Content-Type', '')
            extension = ".mp4" if "video" in contenido else ".jpg"
            nombre_archivo_final = f"{NOMBRE_BASE}{extension}"

            for archivo_viejo in glob.glob(f"{NOMBRE_BASE}*"):
                os.remove(archivo_viejo)

            with open(nombre_archivo_final, 'wb') as archivo_guardado:
                for bloque in respuesta.iter_content(chunk_size=1024*1024):
                    if bloque:
                        archivo_guardado.write(bloque)

            print(f"Archivo descargado: {nombre_archivo_final}")

    except requests.exceptions.RequestException as e:
        print(f"Error en la conexion: {e}")

descarga_multimedia(URL, API_KEY)