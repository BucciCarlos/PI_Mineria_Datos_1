import streamlit as st

# Configuración de página
st.set_page_config(
    page_title="Conclusiones - Streaming Users",
    page_icon="🏆",
    layout="wide"
)

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
    .conclusion-card {
        background-color: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 25px;
        margin-bottom: 25px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.15);
    }
    .card-header {
        font-size: 1.3rem;
        color: #f1c40f;
        font-weight: 600;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .alert-box {
        background-color: rgba(231, 76, 60, 0.1);
        border: 1px solid rgba(231, 76, 60, 0.25);
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 20px;
        color: #ecf0f1;
    }
    .alert-title {
        font-weight: 600;
        color: #e74c3c;
        margin-bottom: 8px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="section-title">🏆 Conclusiones y Recomendaciones Estratégicas</h1>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown("""
    <div class="conclusion-card">
        <div class="card-header">📊 1. Hallazgos Principales (EDA)</div>
        <ul style="line-height: 1.7; font-size: 0.95rem; color: #ecf0f1;">
            <li><b>Perfil de Consumo Estable:</b> El usuario promedio es un adulto joven de <b>35.6 años</b> que consume <b>768.4 minutos mensuales</b> (~25 mins diarios). Un pequeño grupo de superusuarios (outliers) consume más de 70 horas mensuales.</li>
            <li><b>Carga de Soporte Homogénea:</b> La plataforma es sumamente estable, con una media de <b>0.79 tickets</b> por usuario. No existen disparidades locales de infraestructura, lo que permite unificar los procesos continentales de soporte.</li>
            <li><b>Eficiencia Comercial de Planes:</b> Los planes superiores actúan como catalizadores de engagement; la visualización en el plan Premium es un <b>72.4% más alta</b> que en el plan Básico, lo que reduce el riesgo de cancelación.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="conclusion-card">
        <div class="card-header">🧬 2. Diagnóstico Técnico del PCA</div>
        <ul style="line-height: 1.7; font-size: 0.95rem; color: #ecf0f1;">
            <li><b>Reducción Dimensional Ineficaz:</b> La correlación lineal entre edad, visualización y tickets es casi nula ($r \\approx 0$). Reducir las variables de 3 a 2 componentes principales (PC1 y PC2) pierde un <b>32.85% de la información</b> original, demostrando que el PCA no comprime de forma eficiente este dataset.</li>
            <li><b>Solapamiento de Segmentación Comercial:</b> La proyección PC1 vs. PC2 muestra que las coordenadas de los usuarios Básicos, Estándares y Premium se solapan de manera total. El tipo de plan contratado no define un perfil conductual homogéneo.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="conclusion-card">
        <div class="card-header">🎯 3. Recomendaciones de Negocio</div>
        <ul style="line-height: 1.7; font-size: 0.95rem; color: #ecf0f1;">
            <li><b>Campañas de Upselling Dirigidas:</b> Aprovechar que el <b>45%</b> de los usuarios posee el plan Básico para lanzar campañas de incentivo a migrar de plan, dirigidas específicamente a aquellos clientes Básicos cuyo consumo exceda la media de su grupo.</li>
            <li><b>Soporte Premium en Chile y Perú:</b> El promedio de tickets de clientes Premium en Chile (0.92) y Perú (0.89) es más elevado. Se recomienda capacitar a los equipos locales en configuraciones avanzadas UHD/4K y multi-pantalla para evitar el churn.</li>
            <li><b>Segmentación Conductual (Clustering):</b> Abandonar la segmentación puramente comercial de planes en favor de una metodología no supervisada de <b>K-Means</b> que identifique agrupaciones por afinidad a géneros y horarios de uso.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<h2 style="font-family: Outfit, sans-serif; font-size: 1.6rem; font-weight: 600; color: #ecf0f1; margin-top: 10px; margin-bottom: 15px;">🔍 Limitaciones y Mejoras Futuras</h2>', unsafe_allow_html=True)

st.markdown("""
<div class="alert-box">
    <div class="alert-title">⚠️ Anomalía de Calidad en Origen: Outliers Temporales (2029-01-01)</div>
    <p style="text-align: justify; font-size: 0.95rem; line-height: 1.6; margin-bottom: 10px;">
        Durante la revisión de las fechas de inicio de sesión se detectó que exactamente <b>15 registros (0.18% de la muestra)</b> 
        contienen la fecha futura idéntica <b>"2029-01-01"</b>. 
    </p>
    <p style="text-align: justify; font-size: 0.95rem; line-height: 1.6; margin-bottom: 0px;">
        Al tratarse de una fecha futura coincidente, se concluye empíricamente que responde a un <b>error de registro de sistema</b> 
        (un valor por defecto inyectado por el backend ante datos faltantes, corruptos o fallos en las migraciones de base de datos). 
        Si bien por su baja representatividad no altera las conclusiones del EDA ni el modelo del PCA, se registra como una limitación 
        formal en la calidad de la información cruda recopilada.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="conclusion-card">
    <div class="card-header">🚀 4. Propuestas de Mejora y Siguientes Pasos</div>
    <ul style="line-height: 1.7; font-size: 0.95rem; color: #ecf0f1;">
        <li><b>Validación Temporal Dinámica:</b> Incorporar una regla de control en el script de limpieza (<code>02_calidad_y_limpieza.ipynb</code>) que evalúe si la fecha de último inicio de sesión es posterior al tiempo actual (<code>last_login_date > datetime.now()</code>).</li>
        <li><b>Tratamiento Automatizado de Fechas Futuras:</b> En caso de detectar fechas futuras, aislarlas automáticamente para auditoría técnica de ingeniería de datos, e imputar el campo temporal con el nulo lógico de fechas <code>NaT</code> en Pandas para no alterar análisis de cohortes o tendencias.</li>
        <li><b>Integración de Variables Adicionales:</b> Añadir al dataset variables de interacción como el tipo de dispositivo de reproducción, nivel de satisfacción (NPS) y ratio de cancelación para enriquecer los modelos predictivos de churn.</li>
    </ul>
</div>
""", unsafe_allow_html=True)
