import streamlit as st
import pandas as pd
import os

# Configuración de página
st.set_page_config(
    page_title="Dataset - Streaming Users",
    page_icon="📊",
    layout="wide"
)

# Estilos CSS personalizados
st.markdown("""
<style>
    .section-title {
        font-family: 'Outfit', sans-serif;
        font-size: 2.2rem;
        font-weight: 700;
        color: #e74c3c;
        border-bottom: 2px solid rgba(231, 76, 60, 0.2);
        padding-bottom: 8px;
        margin-bottom: 20px;
    }
    .card {
        background-color: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
    }
    .card-title {
        font-size: 1.2rem;
        color: #f1c40f;
        font-weight: 600;
        margin-bottom: 12px;
    }
    .metric-box {
        background: linear-gradient(135deg, rgba(231, 76, 60, 0.1), rgba(241, 196, 15, 0.05));
        border: 1px solid rgba(231, 76, 60, 0.2);
        border-radius: 8px;
        padding: 15px;
        text-align: center;
    }
    .metric-value {
        font-size: 1.8rem;
        font-weight: 700;
        color: #e74c3c;
    }
    .metric-label {
        font-size: 0.9rem;
        color: #bdc3c7;
    }
</style>
""", unsafe_allow_html=True)

# Carga de datos robusta
@st.cache_data
def load_clean_data():
    paths = [
        "data/processed/streaming_users_clean.csv",
        "../data/processed/streaming_users_clean.csv",
        "../../data/processed/streaming_users_clean.csv"
    ]
    for p in paths:
        if os.path.exists(p):
            try:
                return pd.read_csv(p, parse_dates=['last_login_date'])
            except Exception as e:
                st.error(f"Error al leer el archivo {p}: {str(e)}")
    st.error("No se pudo encontrar el archivo de datos procesados.")
    return None

df = load_clean_data()

st.markdown('<h1 class="section-title">🎬 Descripción General del Dataset</h1>', unsafe_allow_html=True)

if df is not None:
    # Métricas clave en la parte superior
    col_m1, col_m2, col_m3, col_m4 = st.columns(4)
    with col_m1:
        st.markdown('<div class="metric-box"><div class="metric-value">8,000</div><div class="metric-label">Registros Totales</div></div>', unsafe_allow_html=True)
    with col_m2:
        st.markdown('<div class="metric-box"><div class="metric-value">8</div><div class="metric-label">Variables Limpias</div></div>', unsafe_allow_html=True)
    with col_m3:
        st.markdown('<div class="metric-box"><div class="metric-value">7</div><div class="metric-label">Países Cubiertos</div></div>', unsafe_allow_html=True)
    with col_m4:
        st.markdown('<div class="metric-box"><div class="metric-value">3</div><div class="metric-label">Planes de Suscripción</div></div>', unsafe_allow_html=True)

    st.write("")

    col_info, col_desc = st.columns([1, 1])

    with col_info:
        st.markdown("""
        <div class="card">
            <div class="card-title">Estructura del Dataset Procesado</div>
            <p style="text-align: justify; font-size: 0.95rem; line-height: 1.6; color: #ecf0f1;">
                El dataset final contiene información depurada sobre el perfil de uso, variables demográficas 
                y métricas de fricción técnica de los suscriptores de streaming. Las variables disponibles son:
            </p>
            <ul style="font-size: 0.95rem; color: #ecf0f1; line-height: 1.6;">
                <li><b>user_id:</b> Identificador único del usuario (clave primaria).</li>
                <li><b>age:</b> Edad del usuario (valores corregidos entre 18 y 80 años).</li>
                <li><b>subscription_plan:</b> Plan activo (Básico, Estándar, Premium).</li>
                <li><b>country:</b> País de residencia (estandarizado para América Latina).</li>
                <li><b>favorite_genre:</b> Género de contenido preferido (imputado sin sesgos).</li>
                <li><b>last_login_date:</b> Fecha de la última sesión (datetime).</li>
                <li><b>monthly_watch_time_mins:</b> Minutos consumidos en el último mes (valores absolutos).</li>
                <li><b>customer_support_tickets:</b> Reclamaciones generadas en el mes (valores absolutos).</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col_desc:
        st.markdown("""
        <div class="card">
            <div class="card-title">Resumen de Calidad y Limpieza</div>
            <p style="text-align: justify; font-size: 0.95rem; line-height: 1.6; color: #ecf0f1;">
                El dataset original (<code>streaming_users_dirty.json</code>) presentaba severos problemas de 
                calidad que hubieran sesgado cualquier análisis. Las transformaciones principales aplicadas en 
                el notebook de limpieza fueron:
            </p>
            <ol style="font-size: 0.95rem; color: #ecf0f1; line-height: 1.6; padding-left: 20px;">
                <li><b>Tratamiento de Edades:</b> Conversión de valores ilógicos (<18 o >100 años) a nulos, imputándolos con la mediana del dataset para conservar el tamaño muestral.</li>
                <li><b>Normalización Geográfica:</b> Limpieza de espacios en blanco y mapeo de abreviaturas/variaciones (ej. <i>CHL, Chile, chile</i> se estandarizaron a <i>Chile</i>).</li>
                <li><b>Imputación de Preferencias:</b> Los géneros nulos se reemplazaron por la etiqueta <i>"Desconocido"</i> para no inyectar sesgos arbitrarios en las tendencias de contenido.</li>
                <li><b>Corrección de Métricas Negativas:</b> Los minutos de visualización y tickets de soporte con signo negativo se corrigieron mediante el valor absoluto (<code>abs()</code>) y los nulos se imputaron con 0.</li>
                <li><b>Depuración de Duplicados:</b> Eliminación de registros idénticos y resolución de duplicados parciales de ID seleccionando el registro más íntegro de cada usuario.</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)

    # Vista previa del Dataframe
    st.markdown('<h2 style="font-family: Outfit, sans-serif; font-size: 1.5rem; font-weight: 600; color: #ecf0f1; margin-bottom: 12px;">Vista Previa del Dataset Procesado</h2>', unsafe_allow_html=True)
    
    # Buscador interactivo
    filtro_pais = st.multiselect("Filtrar por País de Residencia:", options=sorted(df['country'].unique()))
    filtro_plan = st.multiselect("Filtrar por Plan de Suscripción:", options=df['subscription_plan'].unique())

    df_filtrado = df.copy()
    if filtro_pais:
        df_filtrado = df_filtrado[df_filtrado['country'].isin(filtro_pais)]
    if filtro_plan:
        df_filtrado = df_filtrado[df_filtrado['subscription_plan'].isin(filtro_plan)]

    st.dataframe(df_filtrado, use_container_width=True)
    st.caption(f"Mostrando {len(df_filtrado)} registros filtrados de un total de {len(df)}.")

else:
    st.info("Por favor, asegúrate de haber ejecutado los scripts de limpieza previos para generar el dataset procesado.")
