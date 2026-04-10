"""
Modelo de datos y acceso a datos para cartas de Yu-Gi-Oh!
"""
from utils.yugioh_service import obtener_carta, obtener_carta_aleatoria

class Card:
    def __init__(self, data):
        self.id = data.get('id')
        self.name = data.get('name', 'Desconocido')
        self.type = data.get('type', 'N/A')
        self.desc = data.get('desc', 'Sin descripción.')
        self.atk = data.get('atk')
        self.defs = data.get('def')
        self.level = data.get('level')
        self.race = data.get('race')
        self.attribute = data.get('attribute')
        
        # Imágenes
        images = data.get('card_images', [{}])
        self.image_url = images[0].get('image_url') if images else None
        self.image_small_url = images[0].get('image_url_small') if images else None
        
        # Precios
        prices = data.get('card_prices', [{}])
        self.cardmarket_price = prices[0].get('cardmarket_price') if prices else None

    @property
    def has_stats(self):
        """Retorna True si la carta tiene ATK o DEF"""
        return self.atk is not None or self.defs is not None

def get_card_by_name(name):
    """Obtiene una instancia de Card por nombre"""
    data_list = obtener_carta(name)
    if data_list:
        # Retornamos una lista de objetos Card
        return [Card(item) for item in data_list]
    return []

def get_random_card():
    """Obtiene una instancia de Card aleatoria"""
    data = obtener_carta_aleatoria()
    if data:
        return Card(data)
    return None
