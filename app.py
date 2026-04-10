"""
Yu-Gi-Oh! Nexus - Aplicación principal
Arquitectura MVC (Versión Diseño Pro / No-Emojis)
"""
import streamlit as st
from views.layout import setup_page_config, load_css, render_header, render_footer
from views.yugioh_view import render_card, render_sidebar, render_search_section
from views.deck_view import render_deck_section
from views.analysis_view import render_analisis_mazo
from models.deck_model import load_deck
from controllers.yugioh_controller import manejar_busqueda, manejar_aleatorio

def initialize_session_state():
    """Inicializa el estado de la sesión"""
    defaults = {
        'search_results': [],
        'search_term': "",
        'selected_card': None,
        'mazo': load_deck()
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

def main():
    # 1. Configuración de página y estilos
    setup_page_config()
    load_css()
    
    # 2. Inicializar estado
    initialize_session_state()
    
    # 3. Sidebar
    render_sidebar()
    
    # 4. Cabecera
    render_header()
    
    # 5. Navegación por Pestañas (Tabs)
    tab_search, tab_deck, tab_analysis = st.tabs(["BUSCADOR", "MI MAZO", "ANÁLISIS"])
    
    with tab_search:
        # 6. Sección de Búsqueda
        query, btn_search, btn_random, btn_clear = render_search_section()
        
        # Lógica de las acciones
        if btn_search:
            st.session_state.search_term = query
            cards = manejar_busqueda(query)
            if cards:
                st.rerun()

        if btn_random:
            manejar_aleatorio()
            st.rerun()
            
        if btn_clear:
            st.session_state.search_results = []
            st.session_state.search_term = ""
            st.session_state.selected_card = None
            st.rerun()
        
        st.markdown("---")
        
        # 7. Renderizado de Resultados
        if st.session_state.search_results:
            for card in st.session_state.search_results:
                render_card(card)
        elif not st.session_state.search_term:
            st.markdown("<div style='text-align: center; color: #475569; padding: 5rem;'>ACCESO PENDIENTE: INSERTE PARÁMETROS DE BÚSQUEDA</div>", unsafe_allow_html=True)

    with tab_deck:
        # 8. Sección del Mazo
        render_deck_section()

    with tab_analysis:
        # 9. Sección de Análisis
        render_analisis_mazo()

    # 10. Footer
    render_footer()

if __name__ == "__main__":
    main()
