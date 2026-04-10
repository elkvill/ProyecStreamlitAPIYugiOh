"""
Controlador para la gestión del mazo de cartas (Deck Builder)
"""
import streamlit as st
from models.deck_model import load_deck, save_deck

def initialize_deck():
    """Inicializa el mazo cargando datos persistentes si existen"""
    if 'mazo' not in st.session_state:
        st.session_state['mazo'] = load_deck()

def contar_copias(carta_id):
    """Retorna cuántas veces se repite una carta en el mazo por su ID"""
    if 'mazo' not in st.session_state:
        return 0
    return sum(1 for c in st.session_state['mazo'] if c.id == carta_id)

def agregar_al_mazo(carta):
    """
    Agrega una carta al mazo con validaciones de reglas.
    """
    initialize_deck()
    
    # Validación: Máximo 40 cartas
    if len(st.session_state['mazo']) >= 40:
        st.warning("Límite alcanzado: El mazo no puede tener más de 40 cartas.")
        return False
    
    # Validación: Máximo 3 copias de la misma carta
    copias = contar_copias(carta.id)
    if copias >= 3:
        st.warning(f"Restricción de reglas: Ya tienes 3 copias de '{carta.name}' en el mazo.")
        return False
    
    # Si cumple las validaciones, agregar
    st.session_state['mazo'].append(carta)
    save_deck(st.session_state['mazo']) # Persistir
    st.success(f"Carta '{carta.name}' añadida al mazo correctamente.")
    return True

def eliminar_del_mazo(index):
    """
    Elimina una carta del mazo por su índice.
    """
    if 'mazo' in st.session_state and 0 <= index < len(st.session_state['mazo']):
        carta_eliminada = st.session_state['mazo'].pop(index)
        save_deck(st.session_state['mazo']) # Persistir
        st.toast(f"Carta '{carta_eliminada.name}' eliminada del mazo.")
        st.rerun()
    else:
        st.error("Error al intentar eliminar la carta: Índice no válido.")

def vaciar_mazo():
    """
    Limpia completamente la lista del mazo y el archivo persistente.
    """
    st.session_state['mazo'] = []
    save_deck([]) # Persistir vacío
    st.toast("El mazo ha sido vaciado completamente.")
    st.rerun()

def analizar_mazo():
    """
    Analiza el mazo y retorna un diagnóstico detallado.
    """
    mazo = st.session_state.get('mazo', [])
    
    if not mazo:
        return "El mazo está vacío"
        
    total = len(mazo)
    monstruos = sum(1 for c in mazo if "Monster" in c.type)
    magias = sum(1 for c in mazo if "Spell" in c.type)
    trampas = sum(1 for c in mazo if "Trap" in c.type)
    
    # ATK y DEF promedios
    cartas_con_atk = [c.atk for c in mazo if c.atk is not None]
    cartas_con_def = [c.defs for c in mazo if c.defs is not None]
    
    avg_atk = sum(cartas_con_atk) / len(cartas_con_atk) if cartas_con_atk else 0
    avg_def = sum(cartas_con_def) / len(cartas_con_def) if cartas_con_def else 0
    
    # Porcentajes
    p_monstruos = (monstruos / total) * 100
    p_soporte = ((magias + trampas) / total) * 100
    
    # 1. Balance
    if p_monstruos > 70:
        balance = "Desequilibrado: Demasiados monstruos"
        recomendacion_balance = "Considera añadir más cartas de soporte (mágicas/trampas)."
    elif p_soporte < 30:
        balance = "Déficit de Soporte: Falta protección"
        recomendacion_balance = "Añade cartas que protejan a tus monstruos."
    else:
        balance = "Mazo balanceado"
        recomendacion_balance = "La distribución de cartas es óptima."
        
    # 2. Ofensiva
    if avg_atk > 2500:
        ofensiva = "Alta ofensiva"
        desc_ofensiva = "Tus monstruos tienen un poder de ataque devastador."
    elif 1500 <= avg_atk <= 2500:
        ofensiva = "Ofensiva media"
        desc_ofensiva = "Capacidad de ataque moderada, ideal para estrategias rítmicas."
    else:
        ofensiva = "Ofensiva baja"
        desc_ofensiva = "Poder de ataque limitado. Riesgo alto en combate directo."
        
    # 3. Defensa
    if avg_def > avg_atk:
        defensa = "Enfoque defensivo"
        desc_defensa = "Tu mazo brilla protegiendo puntos de vida."
    elif avg_def < 1000:
        defensa = "Defensa débil"
        desc_defensa = "Vulnerable a efectos de posición y ataques directos."
    else:
        defensa = "Defensa equilibrada"
        desc_defensa = "Resistencia adecuada ante ataques enemigos."
        
    # 4. Estrategia
    if avg_atk > 2000 and p_monstruos > 60:
        estrategia = "Estrategia agresiva (Beatdown)"
    elif 40 <= p_monstruos <= 60:
        estrategia = "Estrategia de control (Equilibrada)"
    elif avg_atk < 1500:
        estrategia = "Estrategia defensiva / Combo"
    else:
        estrategia = "Estrategia indefinida"
        
    return {
        "stats": {
            "total": total,
            "monstruos": monstruos,
            "magias": magias,
            "trampas": trampas,
            "avg_atk": avg_atk,
            "avg_def": avg_def,
            "p_monstruos": p_monstruos,
            "p_magias": (magias / total) * 100,
            "p_trampas": (trampas / total) * 100
        },
        "diagnostico": {
            "balance": balance,
            "ofensiva": ofensiva,
            "defensa": defensa,
            "estrategia": estrategia,
            "recomendacion": recomendacion_balance,
            "desc_ofensiva": desc_ofensiva,
            "desc_defensa": desc_defensa
        }
    }
