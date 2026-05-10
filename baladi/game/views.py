from django.shortcuts import render
from django.views.generic import View
import requests

# Create your views here.
class PlayGameView(View):
    template_name = "game/play.html"
    
    def get(self, request,*args, **kwargs):
        
        # URL de la API de la NASA
        api_url = "https://api.nasa.gov/planetary/apod"
        API_KEY = "Y0JI1iNj9sjQGAd6TX25RAf2utKGCsI4yBHUp3xK"
        parametros = {
        "api_key": API_KEY,
        "thumbs": True,
        # "date": "2006-03-03",  # Puedes cambiar esta fecha para probar con diferentes días
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
            
        context = {
            "img_url": url_imagen,
            "title_target": titulo,
            "date":fecha,
            "explanation": explicacion,
        }
    
        return render(request, self.template_name, context)  