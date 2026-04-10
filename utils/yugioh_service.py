"""
Servicio para consumir la API de YGOPRODeck
"""
import requests
from utils.constants import API_ENDPOINT

RANDOM_ENDPOINT = "https://db.ygoprodeck.com/api/v7/randomcard.php"

def obtener_carta(nombre):
    """
    Obtiene los datos de una carta por su nombre.
    Retorna una lista de cartas si se encuentran resultados.
    """
    params = {'name': nombre}
    try:
        response = requests.get(API_ENDPOINT, params=params)
        if response.status_code == 200:
            data = response.json()
            return data.get('data', [])
        elif response.status_code == 400:
            return None
        else:
            return None
    except requests.exceptions.RequestException:
        return None

def obtener_carta_aleatoria():
    """
    Obtiene los datos de una carta aleatoria.
    """
    try:
        response = requests.get(RANDOM_ENDPOINT)
        if response.status_code == 200:
            json_res = response.json()
            # La API de azar devuelve {"data": [...]}
            if isinstance(json_res, dict) and 'data' in json_res:
                data_list = json_res['data']
                if len(data_list) > 0:
                    return data_list[0]
            # Caso de respaldo (si devuelve el objeto directo)
            return json_res
        return None
    except Exception:
        return None
