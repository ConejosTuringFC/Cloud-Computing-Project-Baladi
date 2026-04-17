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

def consultar_nasa_apod(params=None):
    url = "https://api.nasa.gov/planetary/apod"
    query_params = {
        "api_key": "Key personal..."
    }

    if params:
        query_params.update(params)

    try:
        response = requests.get(url, params=query_params)

        if response.status_code == 200:
            return response.json() 

        else:
            return f"Error: {response.status_code} - {response.text}"   
            
    except Exception as e: 
        return f"Ocurrió un error en la conexión: {e}"
```

Where a code request would look like this:

```python
#PRUEBA CON LOS DATOS DE HOY
datos_hoy = consultar_nasa_apod()
print(f"Título de hoy: {datos_hoy.get('title')}")
print(f"URL de la imagen: {datos_hoy.get('url')}\n")
```