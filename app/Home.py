import streamlit as st

# Configuración de página
st.set_page_config(
    page_title="Minería de Datos - Streaming Users",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos personalizados para diseño premium
st.markdown("""
<style>
    .main-title {
        font-family: 'Outfit', 'Inter', sans-serif;
        font-weight: 800;
        font-size: 3.5rem;
        background: linear-gradient(135deg, #e74c3c, #f1c40f, #2ecc71);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        padding-bottom: 0px;
        margin-bottom: 10px;
    }
    .subtitle {
        font-family: 'Inter', sans-serif;
        font-size: 1.5rem;
        color: #bdc3c7;
        text-align: center;
        margin-bottom: 40px;
        font-weight: 300;
    }
    .card {
        background-color: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 25px;
        margin-bottom: 25px;
        backdrop-filter: blur(10px);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.2);
        transition: transform 0.3s ease;
    }
    .card:hover {
        transform: translateY(-5px);
        border-color: rgba(231, 76, 60, 0.5);
    }
    .card-title {
        font-size: 1.3rem;
        color: #e74c3c;
        margin-bottom: 15px;
        font-weight: 600;
    }
    .member-name {
        font-size: 1.1rem;
        font-weight: 500;
        color: #ecf0f1;
        margin-bottom: 8px;
    }
    .github-btn {
        display: inline-block;
        background: linear-gradient(135deg, #24292e, #2b3137);
        color: white !important;
        padding: 12px 24px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: 600;
        border: 1px solid rgba(255, 255, 255, 0.15);
        transition: background 0.3s ease;
        text-align: center;
    }
    .github-btn:hover {
        background: linear-gradient(135deg, #2b3137, #444d56);
        border-color: rgba(231, 76, 60, 0.5);
    }
</style>
""", unsafe_allow_html=True)

# Contenido principal
st.markdown('<h1 class="main-title">Trabajo Final Integrador</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Análisis Avanzado y Minería de Datos sobre Usuarios de Streaming</p>', unsafe_allow_html=True)

# Grid Layout con columnas
col1, col2 = st.columns([3, 2], gap="large")

with col1:
    st.markdown("""
    <div class="card">
        <div class="card-title">Contexto del Proyecto</div>
        <p style="text-align: justify; line-height: 1.6; color: #ecf0f1;">
            Este proyecto de Minería de Datos realiza un análisis profundo sobre el comportamiento y consumo de una base de 
            <b>8,000 usuarios de streaming</b> en América Latina. A través de un pipeline estructurado de calidad y limpieza, 
            análisis exploratorio (EDA) y técnicas de reducción de dimensionalidad mediante Análisis de Componentes Principales (PCA), 
            buscamos identificar patrones ocultos de interacción, evaluar la carga operativa del soporte técnico, y estimar 
            el impacto del modelo de suscripción en el engagement de la plataforma.
        </p>
        <p style="text-align: justify; line-height: 1.6; color: #ecf0f1;">
            Los resultados obtenidos permiten delinear estrategias comerciales de up-selling dirigidas, mitigar cuellos de botella 
            operativos locales, y proponer un cambio metodológico desde la segmentación comercial clásica hacia modelos conductuales 
            más precisos para maximizar la retención de usuarios.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card" style="text-align: center; padding: 30px;">
        <div class="card-title" style="margin-bottom: 20px;">Código Fuente y Repositorio</div>
        <a href="https://github.com/BucciCarlos/PI_Mineria_Datos_1" target="_blank" class="github-btn">
            🐙 Visitar Repositorio en GitHub
        </a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <div class="card-title">Información del Grupo</div>
        <div style="margin-bottom: 15px;">
            <span style="color: #95a5a6; font-size: 0.9rem; display: block;">Materia</span>
            <span style="font-weight: 600; font-size: 1.1rem; color: #ecf0f1;">Minería de Datos</span>
        </div>
        <div style="margin-bottom: 15px;">
            <span style="color: #95a5a6; font-size: 0.9rem; display: block;">Comisión</span>
            <span style="font-weight: 600; font-size: 1.1rem; color: #ecf0f1;">Comisión 1</span>
        </div>
        <div style="margin-bottom: 15px;">
            <span style="color: #95a5a6; font-size: 0.9rem; display: block;">Fecha de Entrega</span>
            <span style="font-weight: 600; font-size: 1.1rem; color: #ecf0f1;">28 de Junio de 2026</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <div class="card-title">Integrantes</div>
        <div class="member-name">👤 Bucci, Carlos Matias</div>

    </div>
    """, unsafe_allow_html=True)
