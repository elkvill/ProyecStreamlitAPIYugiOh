"""
Funciones auxiliares y utilidades para Yu-Gi-Oh! Nexus
"""
import json
from pathlib import Path
from typing import Dict, Any

def load_json_file(filepath: str) -> Dict[str, Any]:
    """
    Carga un archivo JSON de forma segura.
    """
    try:
        path = Path(filepath)
        if path.exists():
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
    except Exception as e:
        print(f"Error al cargar {filepath}: {e}")
    return {}

def save_json_file(filepath: str, data: Dict[str, Any]) -> bool:
    """
    Guarda datos en un archivo JSON de forma segura.
    """
    try:
        path = Path(filepath)
        # Crear directorio padre si no existe
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"Error al guardar {filepath}: {e}")
        return False
