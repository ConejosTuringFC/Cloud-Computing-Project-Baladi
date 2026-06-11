from django.shortcuts import render, redirect
from django.views.generic import View
import requests
import re

# Create your views here.
def get_target_word(raw_title: str):
    ignored_words = {"THE", "A", "AN", "OF", "IN", "ON"}
    aim_words = ["GALAXY", "NEBULA", "PLANET", "STAR", "COMET", "ASTEROID", "BLACKHOLE", "SUPERNOVA","AURORA","SUN"]
    words = [
        re.sub(r'[^A-Z]', '', word)
        for word in raw_title.strip().upper().split()
    ]
    for word in words:
        if word in aim_words:
            return word
        
    target = words[0] if words else "NASA"
    if target in ignored_words and len(words) > 1:
        target = words[1]
    return target

def show_clues(target_word: str, description: str):
    clue = ""
    for word in description.split():
        clean_word = re.sub(r'[^a-zA-Z]', '', word)
        
        if clean_word.lower() != target_word.lower():
            clue += word + " "  
        else:
            clue += " [???] "
    return clue

class PlayGameView(View):
    template_name = "game/play.html"
    
    def get(self, request,*args, **kwargs):
        
        # URL de la API de la NASA
        api_url = "https://api.nasa.gov/planetary/apod"
        API_KEY = "Y0JI1iNj9sjQGAd6TX25RAf2utKGCsI4yBHUp3xK"
        parametros = {
        "api_key": API_KEY,
        "thumbs": True,
         #"date": "2026-05-16",  #CAMBIAMOS LA FECHA PARA PRUEBAS
        }
        
        # VARIABLES POR DEFECTO EN CASO DE QUE LA PETICIÓN LLEGUE A FALLAR (sugerencia de IA)
        titulo = "NASA"
        fecha = ""
        url_imagen = "https://images-assets.nasa.gov/image/PIA08653/PIA08653~medium.jpg"  # IMAGEN DE RESPALDO
        explicacion = ""

        try:

            respuesta = requests.get(api_url, params = parametros)
            respuesta.raise_for_status()

            datos = respuesta.json()

            titulo = datos.get("title")
            fecha = datos.get("date")
            url_imagen = datos.get("url")
            explicacion = datos.get("explanation")
            
            # SI EN VEZ DE UNA FOTO NOS RETORNA UN VIDEO
            if datos.get("media_type") == "video" and "thumbnail_url" in datos:
                url_imagen = datos.get("thumbnail_url")
            else: 
                url_imagen = datos.get("hdurl") or datos.get("url")
            

            print(f"--- {titulo} ({fecha}) ---")
            print(f"Url de la imagen: {url_imagen}")
            print(f"\nDescripcion : {explicacion}")

        except requests.exceptions.RequestException as e:
            print(f"Error en la conexion: {e}")
        
        target_word = get_target_word(titulo)
        clues = show_clues(target_word=target_word, description=explicacion)
        word_length = len(target_word)
            
        context = {
            "img_url": url_imagen,
            "title_target": target_word,
            "date":fecha,
            # "explanation": explicacion,
            "clues": clues,
            "word_length": word_length,
        }
    
        return render(request, self.template_name, context)  
