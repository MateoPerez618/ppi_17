import requests
import googlemaps

# importar GOOGLE_MAPS_API_KEY de settings.py
from django.conf import settings


def get_lat_long_from_address(address, api_key):
    """
    Obtiene las coordenadas de latitud y longitud de una dirección utilizando la API de geocodificación de Google.

    Args:
        address (str): La dirección para la cual se desean obtener las coordenadas.
        api_key (str): La clave de la API de Google Maps para la autenticación.

    Returns:
        tuple: Una tupla con las coordenadas de latitud y longitud en formato (latitud, longitud).
               Si la geocodificación no es exitosa, devuelve (None, None).
    """
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        'address': address,
        'key': api_key,
        "country": "CO"
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if data['status'] == 'OK':
        location = data['results'][0]['geometry']['location']
        lat, lng = location['lat'], location['lng']
        return lat, lng
    else:
        # Handle errors gracefully
        print(f"Geocoding failed with status: {data['status']}")
        return None, None


def calcular_distancia_tiempo(coord_user, coord_temp):
    """
    Calcula la distancia y el tiempo de viaje entre dos coordenadas utilizando la API de direcciones de Google Maps.

    Args:
        coord_user (tuple): Una tupla con las coordenadas de latitud y longitud del usuario.
        coord_temp (tuple): Una tupla con las coordenadas de latitud y longitud del destino.

    Returns:
        dict: Un diccionario con las claves 'distancia' y 'tiempo_viaje' que contienen
              la distancia y el tiempo de viaje respectivamente.

    """
    gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)

    # Convierte las coordenadas a formato 'latitud,longitud'
    coord_user_str = f"{coord_user[0]},{coord_user[1]}"
    coord_temp_str = f"{coord_temp[0]},{coord_temp[1]}"

    # Realiza la solicitud a la API de Google Maps para obtener la distancia y el tiempo de viaje
    result = gmaps.distance_matrix(coord_user_str, coord_temp_str, mode='driving')

    # Extrae la distancia y el tiempo de viaje desde la respuesta de la API
    distancia = result['rows'][0]['elements'][0]['distance']['text']
    tiempo_viaje = result['rows'][0]['elements'][0]['duration']['text']

    return {'distancia': distancia, 'tiempo_viaje': tiempo_viaje}


