"""
Vista para el análisis de sinergia y diagnóstico del mazo
"""
import streamlit as st
from controllers.deck_controller import analizar_mazo

def render_analisis_mazo():
    """Renderiza la sección de análisis del mazo."""
    st.header("ANÁLISIS DE MAZO")
    
    if st.button("EJECUTAR DIAGNÓSTICO", use_container_width=True, type="primary"):
        resultado = analizar_mazo()
        
        if isinstance(resultado, str):
            st.warning(resultado)
            return
            
        stats = resultado['stats']
        diag = resultado['diagnostico']
        
        # 1. Resumen Estadístico (Métricas)
        st.subheader("COMPOSICIÓN")
        c1, c2, c3 = st.columns(3)
        c1.metric("Monstruos", f"{stats['monstruos']}", f"{stats['p_monstruos']:.1f}%")
        c2.metric("Mágicas", f"{stats['magias']}", f"{stats['p_magias']:.1f}%")
        c3.metric("Trampas", f"{stats['trampas']}", f"{stats['p_trampas']:.1f}%")
        
        st.markdown("---")
        
        # 2. Diagnóstico Detallado
        st.subheader("DIAGNÓSTICO DEL SISTEMA")
        
        # Balance
        render_diagnostic_item("BALANCE Y ESTRUCTURA", diag['balance'], diag['recomendacion'])
        
        # Ofensiva
        st.markdown(f"**POTENCIA OFENSIVA (Promedio: {stats['avg_atk']:.0f} ATK)**")
        st.info(f"{diag['ofensiva']}: {diag['desc_ofensiva']}")
        
        # Defensa
        st.markdown(f"**CAPACIDAD DEFENSIVA (Promedio: {stats['avg_def']:.0f} DEF)**")
        st.info(f"{diag['defensa']}: {diag['desc_defensa']}")
        
        st.markdown("---")
        
        # 3. Estrategia Detectada
        st.subheader("ESTRATEGIA IDENTIFICADA")
        st.success(diag['estrategia'])
        
        st.caption("Nota: Este análisis se basa en el ATK/DEF base y la distribución de tipos. No considera efectos de cartas.")

def render_diagnostic_item(title, status, detail):
    """Renderiza un item de diagnóstico con formato consistente."""
    st.markdown(f"**{title}**")
    if "Desequilibrado" in status or "Déficit" in status or "débil" in status.lower():
        st.error(f"{status}")
    elif "balanceado" in status.lower() or "equilibrada" in status.lower():
        st.success(f"{status}")
    else:
        st.warning(f"{status}")
    st.write(detail)
    st.markdown("<br>", unsafe_allow_html=True)
