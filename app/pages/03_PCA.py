import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import os

# Configuración de página
st.set_page_config(
    page_title="PCA - Streaming Users",
    page_icon="🧬",
    layout="wide"
)

# Estilo estético para los gráficos de Seaborn
sns.set_theme(style="whitegrid")

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
    .viz-card {
        background-color: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 30px;
    }
    .viz-header {
        font-size: 1.4rem;
        color: #f1c40f;
        font-weight: 600;
        margin-bottom: 15px;
        border-left: 4px solid #e74c3c;
        padding-left: 10px;
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
    return None

df = load_clean_data()

st.markdown('<h1 class="section-title">🧬 Análisis de Componentes Principales (PCA)</h1>', unsafe_allow_html=True)

if df is not None:
    # ------------------ PREPROCESAMIENTO Y PCA ------------------
    columnas_num = ['age', 'monthly_watch_time_mins', 'customer_support_tickets']
    X = df[columnas_num]
    
    # Estandarización
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # PCA
    pca = PCA()
    pca.fit(X_scaled)
    X_pca = pca.transform(X_scaled)
    
    varianza_explicada = pca.explained_variance_ratio_
    varianza_acumulada = np.cumsum(varianza_explicada)

    # ------------------ DOCUMENTACIÓN DE VARIABLES Y ESCALAMIENTO ------------------
    st.markdown("""
    <div class="card" style="background-color: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; padding: 20px; margin-bottom: 25px;">
        <div style="font-size: 1.2rem; color: #f1c40f; font-weight: 600; margin-bottom: 12px;">Variables Seleccionadas y Justificación del Escalamiento</div>
        <p style="text-align: justify; font-size: 0.95rem; line-height: 1.6; color: #ecf0f1;">
            Para la realización del PCA, se utilizaron las 3 variables cuantitativas del comportamiento del usuario: 
            <b>Edad (age)</b>, <b>Tiempo de Visualización Mensual (monthly_watch_time_mins)</b> y 
            <b>Tickets de Soporte Técnico (customer_support_tickets)</b>.
        </p>
        <p style="text-align: justify; font-size: 0.95rem; line-height: 1.6; color: #ecf0f1;">
            <b>Justificación del Escalamiento (StandardScaler):</b> Las tres variables presentan rangos físicos y desviaciones estándar abismalmente diferentes (el tiempo de visualización mensual tiene una desviación de ~507.85 minutos, la edad de ~9.68 años y los tickets de ~0.90 unidades). Si ejecutáramos el PCA sin estandarizar, la variable con la varianza absoluta más alta (tiempo de visualización) dominaría por completo los autovalores y autovectores de la matriz de covarianza, alineando el primer componente principal con esa única variable. La aplicación de <code>StandardScaler</code> resta la media y divide por la desviación estándar a cada variable, asignándoles una media de 0 y varianza de 1 para garantizar que todas aporten en igualdad de condiciones a la varianza explicada del modelo.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ------------------ GRÁFICO 1: SCREE PLOT ------------------
    st.markdown('<div class="viz-card">', unsafe_allow_html=True)
    st.markdown('<div class="viz-header">1. Gráfico de Sedimentación (Scree Plot) - Varianza Explicada</div>', unsafe_allow_html=True)
    
    fig1, ax1 = plt.subplots(figsize=(10, 5))
    fig1.patch.set_facecolor('#0e1117')
    
    ax1.bar(range(1, len(varianza_explicada) + 1), varianza_explicada, alpha=0.6, color='steelblue', label='Varianza Individual')
    ax1.plot(range(1, len(varianza_acumulada) + 1), varianza_acumulada, marker='o', color='crimson', label='Varianza Acumulada')
    
    ax1.set_title('Varianza Explicada por Componente Principal', color='white', fontsize=13, pad=15)
    ax1.set_xlabel('Componente Principal', color='white')
    ax1.set_ylabel('Proporción de Varianza Explicada', color='white')
    ax1.set_xticks([1, 2, 3])
    ax1.tick_params(colors='white')
    ax1.legend(facecolor='#0e1117', edgecolor='none', labelcolor='white')
    ax1.grid(True, alpha=0.15)
    
    st.pyplot(fig1)
    plt.close(fig1)
    
    st.markdown(f"""
    **Análisis de la Varianza Explicada:**
    El gráfico de sedimentación (*Scree Plot*) muestra que la varianza explicada se distribuye casi equitativamente:
    * **Componente Principal 1 (PC1):** Explica el **{varianza_explicada[0]*100:.2f}%** de la varianza total.
    * **Componente Principal 2 (PC2):** Explica el **{varianza_explicada[1]*100:.2f}%** de la varianza total.
    * **Componente Principal 3 (PC3):** Explica el **{varianza_explicada[2]*100:.2f}%** de la varianza total.
    * **Varianza Acumulada (PC1 + PC2):** Representa el **{varianza_acumulada[1]*100:.2f}%** de la variabilidad del dataset.

    **Evaluación de la Efectividad:**
    A partir de estos resultados, se concluye que **la reducción dimensional mediante PCA en este dataset NO es efectiva**. 
    Un proceso de reducción dimensional es exitoso cuando un número reducido de componentes principales (por ejemplo, 1 o 2 componentes de un espacio mayor) logra capturar la gran mayoría de la variabilidad original (típicamente >80%), demostrando que existen variables correlacionadas y redundantes que pueden ser resumidas. 
    En este caso, la varianza se distribuye de manera casi equitativa en tres partes iguales (~33% cada una). Esto ocurre porque, como se demostró en el EDA, la correlación lineal entre las variables de entrada es prácticamente nula ($r \approx 0$). Cuando las variables son independientes, el espacio multidimensional es esférico y no elíptico, impidiendo que el PCA encuentre direcciones preferenciales de varianza. Reducir las dimensiones a 2 componentes principales (PC1 y PC2) implica **perder un 32.85% de la información original**, lo cual equivale casi exactamente a descartar una de las tres variables por completo (1 de 3 variables representa el 33.3% del total). Por ende, el PCA no aporta una simplificación informativa eficiente en este caso.
    """)
    st.markdown('</div>', unsafe_allow_html=True)


    # ------------------ GRÁFICO 2: PROYECCIÓN PCA ------------------
    st.markdown('<div class="viz-card">', unsafe_allow_html=True)
    st.markdown('<div class="viz-header">2. Proyección PCA (PC1 vs. PC2) segmentada por Plan de Suscripción</div>', unsafe_allow_html=True)
    
    # Agregamos temporalmente los componentes al dataframe para graficar
    df_temp = df.copy()
    df_temp['PC1'] = X_pca[:, 0]
    df_temp['PC2'] = X_pca[:, 1]
    
    orden_planes = ['Básico', 'Estándar', 'Premium']
    colores_semaforo = ['#e74c3c', '#f1c40f', '#2ecc71']
    
    fig2, ax2 = plt.subplots(figsize=(11, 6))
    fig2.patch.set_facecolor('#0e1117')
    
    sns.scatterplot(
        data=df_temp, x='PC1', y='PC2', 
        hue='subscription_plan', hue_order=orden_planes, palette=colores_semaforo, 
        alpha=0.6, edgecolor=None, ax=ax2
    )
    
    ax2.set_title('Proyección PCA (PC1 vs PC2) segmentada por Plan de Suscripción', color='white', fontsize=13, pad=15)
    ax2.set_xlabel(f'Componente Principal 1 ({varianza_explicada[0]*100:.2f}% de varianza)', color='white')
    ax2.set_ylabel(f'Componente Principal 2 ({varianza_explicada[1]*100:.2f}% de varianza)', color='white')
    ax2.axhline(0, color='grey', linestyle='--', alpha=0.5)
    ax2.axvline(0, color='grey', linestyle='--', alpha=0.5)
    ax2.tick_params(colors='white')
    ax2.legend(facecolor='#0e1117', edgecolor='none', labelcolor='white')
    ax2.grid(True, alpha=0.15)
    
    st.pyplot(fig2)
    plt.close(fig2)
    
    st.markdown("""
    **Interpretación de la Proyección PCA:**
    Para comprender la estructura de los datos proyectados en el plano bidimensional definido por PC1 (eje X) y PC2 (eje Y), analizamos los pesos (*loadings*) que definen a cada componente:
    * **PC1 (33.74% de varianza):** Presenta un peso positivo fuerte en `monthly_watch_time_mins` (**0.735**) y en `age` (**0.564**), combinado con un peso negativo moderado en `customer_support_tickets` (**-0.375**). Define a usuarios con **alto volumen de consumo, mayor edad y baja fricción operativa** (pocas reclamaciones).
    * **PC2 (33.41% de varianza):** Presenta un peso positivo fuerte en `customer_support_tickets` (**0.800**) y en `age` (**0.597**), con una influencia casi nula del consumo mensual (**-0.050**). Define a usuarios de **mayor edad y alta fricción con soporte**, independientemente de lo mucho o poco que consuman en la plataforma.

    **Comportamiento y Agrupamiento según el Plan de Suscripción:**
    Al proyectar a los usuarios y segmentarlos por su plan de suscripción en el gráfico de dispersión, se desprenden las siguientes conclusiones analíticas:
    1. **Desplazamiento de los Centroides (Medias):**
       * *Plan Básico:* Centroide promedio en PC1 = **-0.261**, PC2 = **0.018**. Tiende a posicionarse más hacia la izquierda en el eje PC1, lo cual está alineado con su menor promedio de consumo mensual de minutos (~592 mins).
       * *Plan Estándar:* Centroide promedio en PC1 = **0.135**, PC2 = **-0.008**. Ocupa una posición intermedia cercana al origen de coordenadas.
       * *Plan Premium:* Centroide promedio en PC1 = **0.355**, PC2 = **-0.027**. Se desplaza ligeramente hacia la derecha en el eje PC1, impulsado por el alto consumo promedio de minutos mensual (~1,020 mins).
    2. **Solapamiento Visual y Diagnóstico Comercial:**
       A pesar de las sutiles diferencias en los promedios de PC1 descritos anteriormente, **las nubes de puntos de los tres planes de suscripción se superponen (solapan) de manera casi total en la proyección**. Los rangos de dispersión de PC1 y PC2 son prácticamente idénticos para el plan Básico, Estándar y Premium (todos cubren de -3.2 a 6.4 en PC1 y de -2.1 a 4.8 en PC2). No existe una separación visual ni formación de agrupaciones (*clusters*) independientes.
       **Conclusión de Negocio:** La segmentación actual basada exclusivamente en la jerarquía del plan contratado (Básico, Estándar o Premium) es **insuficiente** para definir perfiles demográficos o conductuales diferenciados de soporte y consumo. Un gran número de clientes del plan Básico comparte el mismo espacio de consumo y comportamiento que los clientes Premium. Para campañas efectivas de retención o personalización de contenido, el negocio no debe basarse en el tipo de plan, sino que requiere la implementación de algoritmos de agrupamiento no supervisado (como K-Means) que aglutinen a los usuarios según sus hábitos reales de consumo y patrones de interacción técnica.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

else:
    st.info("Por favor, asegúrate de haber ejecutado los scripts de limpieza previos para generar el dataset procesado.")
