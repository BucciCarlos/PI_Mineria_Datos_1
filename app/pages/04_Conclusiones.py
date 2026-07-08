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
    .custom-help-box {
        background-color: rgba(155, 89, 182, 0.08);
        border: 1px solid rgba(155, 89, 182, 0.2);
        border-left: 5px solid rgb(155, 89, 182);
        border-radius: 8px;
        padding: 20px;
        margin-top: 15px;
        margin-bottom: 25px;
        color: var(--text-color);
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="section-title">🏆 Conclusiones y Recomendaciones Estratégicas</h1>', unsafe_allow_html=True)

# Bloque 1: Hallazgos Principales (Análisis de Negocio y EDA) -> Success
st.success("""
### 📊 1. Hallazgos Principales (Análisis de Negocio y EDA)
* **Perfil de Consumo Estable:** El usuario promedio es un adulto joven de **35.6 años** que consume **768.4 minutos mensuales** (~25 mins diarios). Un pequeño grupo de superusuarios (outliers) consume más de 70 horas mensuales.
* **Carga de Soporte Homogénea:** La plataforma es sumamente estable, con una media de **0.79 tickets** por usuario. No existen disparidades locales de infraestructura, lo que permite unificar los procesos continentales de soporte.
* **Eficiencia Comercial de Planes:** Los planes superiores actúan como catalizadores de engagement; la visualización en el plan Premium es un **72.4% más alta** que en el plan Básico, lo que reduce el riesgo de cancelación.
* **Campañas de Upselling Dirigidas:** Aprovechar que el **45%** de los usuarios posee el plan Básico para lanzar campañas de incentivo a migrar de plan, dirigidas específicamente a aquellos clientes Básicos cuyo consumo exceda la media de su grupo.
* **Soporte Premium en Chile y Perú:** El promedio de tickets de clientes Premium en Chile (0.92) y Perú (0.89) es más elevado. Se recomienda capacitar a los equipos locales en configuraciones avanzadas UHD/4K y multi-pantalla para evitar el churn.
""")

# Bloque 2: Conclusiones Técnicas (Fallo del PCA y Dimensionalidad) -> Info
st.info("""
### 🧬 2. Conclusiones Técnicas (Fallo del PCA y Dimensionalidad)
* **Reducción Dimensional Ineficaz:** La correlación lineal entre edad, visualización y tickets es casi nula ($r \\approx 0$). Reducir las variables de 3 a 2 componentes principales (PC1 y PC2) pierde un **32.85% de la información** original, demostrando que el PCA no comprime de forma eficiente este dataset.
* **Solapamiento de Segmentación Comercial:** La proyección PC1 vs. PC2 muestra que las coordenadas de los usuarios Básicos, Estándares y Premium se solapan de manera total. El tipo de plan contratado no define un perfil conductual homogéneo.
""")

# Bloque 3: Limitaciones del Dataset (Los 15 registros anómalos de 2029) -> Warning
st.warning("""
### 🔍 3. Limitaciones del Dataset (Outliers Temporales de 2029)
* **Anomalía de Calidad en Origen:** Durante la revisión de las fechas de inicio de sesión se detectó que exactamente **15 registros (0.18% de la muestra)** contienen la fecha futura idéntica **"2029-01-01"**.
* **Diagnóstico del Error:** Al tratarse de una fecha futura coincidente, se concluye empíricamente que responde a un **error de registro de sistema** (un valor por defecto inyectado por el backend ante datos faltantes, corruptos o fallos en las migraciones de base de datos). Si bien por su baja representatividad no altera las conclusiones del EDA ni el modelo del PCA, se registra como una limitación formal en la calidad de la información cruda recopilada.
""")

# Bloque 4: Siguientes Pasos (Propuesta de K-Means y Validación Temporal) -> Custom highlighted markdown
st.markdown("""
<div class="custom-help-box">
    <h3 style="color: #9b59b6; margin-top: 0; font-weight: 600;">🚀 4. Siguientes Pasos (Mejora Metodológica y Validación)</h3>
    <ul style="line-height: 1.6; font-size: 0.95rem; margin-bottom: 0; padding-left: 20px;">
        <li style="margin-bottom: 8px;"><b>Segmentación Conductual (Clustering K-Means):</b> Abandonar la segmentación puramente comercial de planes en favor de una metodología no supervisada de <b>K-Means</b> que identifique agrupaciones por afinidad a géneros y horarios de uso.</li>
        <li style="margin-bottom: 8px;"><b>Validación Temporal Dinámica:</b> Incorporar una regla de control en el script de limpieza (<i>02_calidad_y_limpieza.ipynb</i>) que evalúe si la fecha de último inicio de sesión es posterior al tiempo actual (<i>last_login_date > datetime.now()</i>).</li>
        <li style="margin-bottom: 8px;"><b>Tratamiento Automatizado de Fechas Futuras:</b> En caso de detectar fechas futuras, aislarlas automáticamente para auditoría técnica de ingeniería de datos, e imputar el campo temporal con el nulo lógico de fechas <i>NaT</i> en Pandas para no alterar análisis de cohortes o tendencias.</li>
        <li style="margin-bottom: 0;"><b>Integración de Variables Adicionales:</b> Añadir al dataset variables de interacción como el tipo de dispositivo de reproducción, nivel de satisfacción (NPS) y ratio de cancelación para enriquecer los modelos predictivos de churn.</li>
    </ul>
</div>
""", unsafe_allow_html=True)
