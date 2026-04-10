"""
Vista para la gestión y visualización del mazo (Deck Builder)
"""
import streamlit as st
from controllers.deck_controller import eliminar_del_mazo, vaciar_mazo

def render_deck_section():
    """Renders the 'Mi Mazo' section according to the required design."""
    if 'mazo' not in st.session_state:
        return
    
    # Encabezado y Botón de Vaciado
    c_title, c_clear = st.columns([3, 1], vertical_alignment="center")
    with c_title:
        st.header("MI MAZO")
    with c_clear:
        if st.session_state['mazo']:
            if st.button("VACIAR MAZO", key="clear_deck_btn", width='stretch', type="primary"):
                vaciar_mazo()

    # Contador
    total_cards = len(st.session_state['mazo'])
    st.markdown(f"#### CARTAS EN EL MAZO: {total_cards}/40")
    
    if total_cards == 0:
        st.info("EL MAZO ESTÁ VACÍO. AGREGA CARTAS DESDE EL BUSCADOR.")
        return

    # Opcional: Resumen por tipo (Extra)
    render_deck_summary()

    st.markdown("<br>", unsafe_allow_html=True)

    # Listado de cartas (Grid-like)
    # Mostramos las cartas de forma compacta pero con toda la info requerida
    for i, card in enumerate(st.session_state['mazo']):
        with st.container():
            # Contamos copias para mostrar (Extra)
            copias = sum(1 for c in st.session_state['mazo'] if c.id == card.id)
            
            # Layout de fila para cada carta
            col_img, col_info, col_action = st.columns([1, 4, 1], gap="medium", vertical_alignment="center")
            
            with col_img:
                if card.image_small_url:
                    st.image(card.image_small_url, width=80)
            
            with col_info:
                st.markdown(f"**{card.name.upper()}**")
                
                # Stats y Tipo en una sola línea compacta
                stats_str = ""
                if card.atk is not None or card.defs is not None:
                    stats_str = f" | ATK: {card.atk if card.atk is not None else '0'} - DEF: {card.defs if card.defs is not None else '0'}"
                
                st.markdown(f"<small>{card.type}{stats_str}</small>", unsafe_allow_html=True)
                
            with col_action:
                if st.button("ELIMINAR", key=f"del_{i}_{card.id}", width='stretch'):
                    eliminar_del_mazo(i)
            
            st.markdown('<hr style="margin: 0.5rem 0; border: none; border-top: 1px solid #1e293b;">', unsafe_allow_html=True)

def render_deck_summary():
    """Muestra un resumen de la composición del mazo (Extra)."""
    monsters = sum(1 for c in st.session_state['mazo'] if "Monster" in c.type)
    spells = sum(1 for c in st.session_state['mazo'] if "Spell" in c.type)
    traps = sum(1 for c in st.session_state['mazo'] if "Trap" in c.type)
    
    cols = st.columns(3)
    cols[0].metric("MONSTRUOS", monsters)
    cols[1].metric("MÁGICAS", spells)
    cols[2].metric("TRAMPAS", traps)
