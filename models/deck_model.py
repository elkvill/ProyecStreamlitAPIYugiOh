"""
Modelo de datos para la persistencia del mazo de cartas
"""
from typing import List
from utils.helpers import load_json_file, save_json_file
from models.card_model import Card

DECK_FILE = "data/deck.json"

def save_deck(cards: List[Card]) -> bool:
    """
    Guarda la lista de objetos Card en un archivo JSON.
    """
    deck_data = []
    for card in cards:
        # Reconstruir el diccionario original para que Card(item) funcione al cargar
        item = {
            'id': card.id,
            'name': card.name,
            'type': card.type,
            'desc': card.desc,
            'atk': card.atk,
            'def': card.defs,
            'level': card.level,
            'race': card.race,
            'attribute': card.attribute,
            'card_images': [
                {
                    'image_url': card.image_url,
                    'image_url_small': card.image_small_url
                }
            ],
            'card_prices': [
                {
                    'cardmarket_price': card.cardmarket_price
                }
            ]
        }
        deck_data.append(item)
    
    data = {'mazo': deck_data}
    return save_json_file(DECK_FILE, data)

def load_deck() -> List[Card]:
    """
    Carga el mazo desde el archivo JSON y reconstruye los objetos Card.
    """
    data = load_json_file(DECK_FILE)
    deck_list = data.get('mazo', [])
    return [Card(item) for item in deck_list]
