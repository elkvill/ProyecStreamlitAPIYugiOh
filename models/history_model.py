"""
Modelo de datos para gestión de historial de búsquedas de cartas
"""
from typing import List, Dict
from datetime import datetime
from utils.helpers import load_json_file, save_json_file

HISTORY_FILE = "data/history.json"
MAX_HISTORY = 10

def add_to_history(card) -> bool:
    """
    Añade una carta al historial.
    """
    history = load_history()
    
    # Crear entrada de historial
    entry = {
        'name': card.name,
        'timestamp': datetime.now().isoformat(),
        'type': card.type,
        'image_small': card.image_small_url
    }
    
    # Evitar duplicados consecutivos por nombre
    if history and history[0].get('name') == card.name:
        return True
    
    # Añadir al principio de la lista
    history.insert(0, entry)
    
    # Mantener solo los últimos N registros
    history = history[:MAX_HISTORY]
    
    data = {'history': history}
    return save_json_file(HISTORY_FILE, data)

def load_history() -> List[Dict]:
    """
    Carga el historial de búsquedas.
    """
    data = load_json_file(HISTORY_FILE)
    return data.get('history', [])

def clear_history() -> bool:
    """
    Limpia todo el historial.
    """
    data = {'history': []}
    return save_json_file(HISTORY_FILE, data)
