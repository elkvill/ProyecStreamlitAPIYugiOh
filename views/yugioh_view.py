"""
Componentes de visualización para cartas de Yu-Gi-Oh! (Sin Emojis)
"""
import streamlit as st
from controllers.yugioh_controller import navigate_to_card
from controllers.deck_controller import agregar_al_mazo
from models.history_model import load_history, clear_history


def render_card(card):
    """
    Renderiza una carta en un contenedor de diseño tecnológico.
    """
    if not card:
        return

    with st.container():
        st.markdown('<div class="card-container">', unsafe_allow_html=True)

        col1, col2 = st.columns([1, 1.5], gap="large")

        with col1:
            if card.image_url:
                st.image(card.image_url, width='stretch')
            else:
                st.info("Imagen de carta no disponible")

        with col2:
            st.title(card.name.upper())

            # Badges de Tipo y Atributo
            st.markdown(f"""
                <span class="nexus-badge badge-type">{card.type}</span>
                {f'<span class="nexus-badge badge-attribute">{card.attribute}</span>' if card.attribute else ''}
                {f'<span class="nexus-badge">Nivel {card.level}</span>' if card.level else ''}
                {f'<span class="nexus-badge">Raza: {card.race}</span>' if card.race else ''}
            """, unsafe_allow_html=True)

            st.markdown("<div style='margin-bottom: 2rem;'></div>",
                        unsafe_allow_html=True)

            # ATK y DEF
            if card.has_stats:
                c1, c2 = st.columns(2)
                with c1:
                    st.markdown(
                        '<p class="stat-label">Ataque / ATK</p>', unsafe_allow_html=True)
                    st.markdown(
                        f'<p class="stat-value">{card.atk if card.atk is not None else "0"}</p>', unsafe_allow_html=True)
                with c2:
                    st.markdown(
                        '<p class="stat-label">Defensa / DEF</p>', unsafe_allow_html=True)
                    st.markdown(
                        f'<p class="stat-value">{card.defs if card.defs is not None else "0"}</p>', unsafe_allow_html=True)
                st.markdown("---")

            st.markdown("### ESPECIFICACIONES")
            st.markdown(
                f'<div class="desc-text">{card.desc}</div>', unsafe_allow_html=True)

            if card.cardmarket_price:
                st.markdown("<div style='margin-top: 1.5rem;'></div>",
                            unsafe_allow_html=True)
                st.markdown(
                    f"VALOR DE MERCADO: **${card.cardmarket_price} USD**")

            # Botón de Agregar al Mazo
            st.markdown("<div style='margin-top: 2rem;'></div>",
                        unsafe_allow_html=True)
            if st.button("AGREGAR AL MAZO", key=f"add_deck_{card.id}", use_container_width=True, type="secondary"):
                agregar_al_mazo(card)

        st.markdown('</div>', unsafe_allow_html=True)


def render_sidebar():
    """Renderiza el sidebar (Sin emojis)"""
    with st.sidebar:
        st.image(
            "https://images.ygoprodeck.com/images/assets/ygoprodeck_header_logo.png", width=200)

        st.markdown("---")
        render_history_panel()

        st.markdown("---")
        st.header("ACCESOS")
        popular_cards = [
            "SELECCIONAR...", "Dark Magician", "Blue-Eyes White Dragon",
            "Exodia the Forbidden One", "Red-Eyes Black Dragon",
            "Slifer the Sky Dragon", "Obelisk the Tormentor", "The Winged Dragon of Ra"
        ]

        selected = st.selectbox("CARTAS RELEVANTES",
                                popular_cards, key="popular_select")
        if selected != "SELECCIONAR...":
            if st.button("VISUALIZAR DATOS", width='stretch'):
                navigate_to_card(selected)


def render_history_panel():
    """Panel de historial"""
    st.header("REGISTROS")
    history = load_history()

    if not history:
        st.caption("No hay registros en el archivo actual.")
    else:
        for i, entry in enumerate(history):
            if st.button(f"{entry['name'].upper()}", key=f"hist_{i}", width='stretch'):
                navigate_to_card(entry['name'])

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("BORRAR REGISTROS", key="clear_hist", width='stretch'):
            clear_history()
            st.rerun()


def render_search_section():
    """Buscador (Sin emojis)"""
    c_input, c_btns = st.columns(
        [2.5, 1], gap="small", vertical_alignment="center")

    with c_input:
        query = st.text_input(
            "Búsqueda",
            placeholder="Introduce nombre de la carta...",
            value=st.session_state.search_term,
            key="search_input",
            label_visibility="collapsed"
        )

    with c_btns:
        btn_search = st.button("CONSULTAR", width='stretch', type="primary")

        b1, b2 = st.columns(2, gap="xsmall")
        with b1:
            btn_random = st.button(
                "AZAR", width='stretch', help="Ficha Aleatoria")
        with b2:
            btn_clear = st.button("RESET", width='stretch',
                                  help="Resetear Interfaz")

    return query, btn_search, btn_random, btn_clear
