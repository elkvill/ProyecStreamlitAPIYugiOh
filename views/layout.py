"""
Layout principal y configuración de diseño Premium
"""
import streamlit as st

def setup_page_config():
    """Configuración de la página de Streamlit"""
    st.set_page_config(
        page_title="Yu-Gi-Oh! Nexus - Card Database",
        page_icon="Playing Cards", 
        layout="wide"
    )

def load_css():
    """Carga el CSS Premium de Yu-Gi-Oh! Nexus (Versión No-Emoji)"""
    st.markdown("""
        <style>
        /* Estilizamos el contenedor raíz de Streamlit para forzar el tema oscuro */
        [data-testid="stAppViewContainer"] {
            background-color: #0d1117;
        }
        
        [data-testid="stHeader"] {
            background: rgba(0,0,0,0);
        }

        .main {
            background-color: #0d1117;
            color: #f1f5f9;
            font-family: 'Outfit', sans-serif;
        }
        
        /* Contenedor de la carta */
        .card-container {
            background: linear-gradient(145deg, #161b22, #1f2937);
            padding: 3rem;
            border-radius: 2rem;
            box-shadow: 0 25px 60px rgba(0, 0, 0, 0.6);
            border: 1px solid rgba(255, 255, 255, 0.05);
            margin-bottom: 3rem;
        }
        
        /* Títulos */
        h1, h2, h3 {
            color: #ffffff !important;
            font-weight: 800;
            margin-bottom: 2rem;
            letter-spacing: -0.02em;
        }
        
        /* Métrica Stats */
        .stat-label {
            font-weight: 600;
            color: #94a3b8;
            text-transform: uppercase;
            font-size: 0.7rem;
            letter-spacing: 0.15em;
            margin-bottom: 0.5rem;
        }
        
        .stat-value {
            font-size: 2.5rem;
            color: #58a6ff;
            font-weight: 800;
            text-shadow: 0 0 20px rgba(88, 166, 255, 0.3);
            margin-bottom: 0px;
        }

        /* Botones Premium */
        .stButton>button {
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            background: rgba(31, 111, 235, 0.1) !important;
            color: #58a6ff !important;
            padding: 0.5rem 1rem;
            border-radius: 0.8rem;
            font-weight: 600;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background: rgba(31, 111, 235, 0.2) !important;
            border-color: #58a6ff !important;
            box-shadow: 0 0 15px rgba(88, 166, 255, 0.2);
        }
        
        /* Primario */
        div[data-testid="stButton"] button[kind="primary"] {
            background: #1f6feb !important;
            color: white !important;
            border: none !important;
        }

        /* Badges Diseño */
        .nexus-badge {
            display: inline-block;
            padding: 0.25rem 0.8rem;
            border-radius: 0.5rem;
            font-size: 0.75rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            color: #cbd5e1;
            margin-right: 0.5rem;
            margin-bottom: 0.5rem;
        }

        .badge-attribute {
            border-left: 3px solid #58a6ff;
            background: rgba(88, 166, 255, 0.1);
        }

        .badge-type {
            border-left: 3px solid #bc8cff;
            background: rgba(188, 140, 255, 0.1);
        }

        /* Sidebar */
        [data-testid="stSidebar"] {
            background-color: #0d1117 !important;
            border-right: 1px solid #30363d;
        }
        
        /* Texto de descripción */
        .desc-text {
            color: #f1f5f9;
            line-height: 1.7;
            font-size: 1rem;
            background: rgba(255, 255, 255, 0.03);
            padding: 1.5rem;
            border-radius: 1rem;
            border: 1px solid rgba(255, 255, 255, 0.05);
        }
        </style>
    """, unsafe_allow_html=True)

def render_header():
    """Renderiza el título principal (Sin emojis)"""
    st.markdown("<h1 style='text-align: center; font-size: 3.5rem;'>YU-GI-OH! NEXUS</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.3em; font-size: 0.8rem;'>Protocolo de Acceso a Base de Datos de Cartas</p>", unsafe_allow_html=True)

def render_footer():
    """Renderiza el footer"""
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #475569; font-size: 0.75rem; letter-spacing: 0.1em;'>PROYECTO USANDO API YGOPRODECK - HECHO EN STREAMLIT</p>", unsafe_allow_html=True)
