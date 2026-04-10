"""
Controlador principal para la lógica de búsqueda de cartas de Yu-Gi-Oh
"""
import streamlit as st
from models.card_model import get_card_by_name, get_random_card
from models.history_model import add_to_history


def manejar_busqueda(nombre):
    """
    Gestiona la búsqueda de una carta, validaciones y mensajes en la interfaz.
    """
    if not nombre or not nombre.strip():
        st.warning("Especifique un término de búsqueda válido.")
        return None

    with st.spinner("Accediendo a la red central..."):
        cards = get_card_by_name(nombre)

        if cards:
            st.toast(f"Registros encontrados: {len(cards)}")
            st.session_state.search_results = cards
            st.session_state.selected_card = cards[0]
            add_to_history(cards[0])
            return cards
        else:
            st.error("Error de búsqueda: El término no existe en la base de datos.")
            return None


def manejar_aleatorio():
    """
    Gestiona la obtención de una carta aleatoria.
    """
    with st.spinner("Sincronizando ficha aleatoria..."):
        card = get_random_card()
        if card:
            st.session_state.search_results = [card]
            st.session_state.selected_card = card
            st.session_state.search_term = card.name
            add_to_history(card)
            st.toast(f"Acceso concedido: {card.name}")
            return card
        else:
            st.error("Fallo de comunicación: No se pudo obtener la ficha.")
            return None


def navigate_to_card(name):
    """Callback para navegar a una carta específica"""
    st.session_state.search_term = name
    cards = get_card_by_name(name)
    if cards:
        st.session_state.search_results = cards
        st.session_state.selected_card = cards[0]
        add_to_history(cards[0])
        st.rerun()
