import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Configuración de página
st.set_page_config(
    page_title="EDA - Streaming Users",
    page_icon="📈",
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
        padding: 25px;
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

st.markdown('<h1 class="section-title">📈 Análisis Exploratorio de Datos (EDA)</h1>', unsafe_allow_html=True)

if df is not None:
    # ------------------ VISUALIZACIÓN 1: UNIVARIADA 1 (NUMÉRICA) ------------------
    st.markdown('<div class="viz-card">', unsafe_allow_html=True)
    st.markdown('<div class="viz-header">1. Distribución del Tiempo de Visualización Mensual (Univariada 1)</div>', unsafe_allow_html=True)
    
    fig1, ax1 = plt.subplots(figsize=(10, 5))
    fig1.patch.set_facecolor('#0e1117')
    ax1.set_facecolor('#0e1117')
    
    sns.histplot(df['monthly_watch_time_mins'], kde=True, ax=ax1, color='steelblue')
    
    # Línea vertical para marcar la mediana
    mediana_watch = df['monthly_watch_time_mins'].median()
    ax1.axvline(mediana_watch, color='#e74c3c', linestyle='--', linewidth=2, label=f'Mediana: {mediana_watch:.1f} mins')
    
    ax1.set_title('Distribución de Minutos de Visualización Mensuales', color='white', fontsize=12)
    ax1.set_ylabel('Frecuencia', color='white')
    ax1.set_xlabel('Minutos Mensuales', color='white')
    ax1.tick_params(colors='white')
    ax1.grid(True, alpha=0.15)
    ax1.legend(facecolor='#0e1117', edgecolor='none', labelcolor='white')
    
    plt.tight_layout()
    st.pyplot(fig1)
    plt.close(fig1)
    
    st.markdown("""
    **Interpretación del Tiempo de Visualización:**
    Muestra una distribución sesgada a la derecha con un promedio de **768.4 minutos** (~12.8 horas/mes) y una mediana de **737.1 minutos** (~12.3 horas/mes). Se detectan usuarios con consumos extremos que superan los **4,000 minutos mensuales** (~66 horas/mes). Para el negocio, este grupo de "superusuarios" representa el núcleo de retención y lealtad de la plataforma, mientras que la mediana refleja un hábito de consumo regular y saludable (unos 25 minutos diarios), lo cual indica una interacción sostenida pero no intensiva para el usuario promedio.
    """)
    st.markdown('</div>', unsafe_allow_html=True)


    # ------------------ VISUALIZACIÓN 2: UNIVARIADA 2 (CATEGÓRICA) ------------------
    st.markdown('<div class="viz-card">', unsafe_allow_html=True)
    st.markdown('<div class="viz-header">2. Distribución del Plan de Suscripción (Univariada 2)</div>', unsafe_allow_html=True)
    
    fig2, ax2 = plt.subplots(figsize=(10, 5))
    fig2.patch.set_facecolor('#0e1117')
    ax2.set_facecolor('#0e1117')
    
    orden_planes = ['Básico', 'Estándar', 'Premium']
    colores_semaforo = ['#e74c3c', '#f1c40f', '#2ecc71']
    
    sns.countplot(
        data=df, 
        x='subscription_plan', 
        ax=ax2, 
        order=orden_planes, 
        hue='subscription_plan',
        legend=False,
        palette=colores_semaforo
    )
    
    ax2.set_title('Cantidad de Usuarios por Plan de Suscripción', color='white', fontsize=12)
    ax2.set_xlabel('Plan de Suscripción', color='white')
    ax2.set_ylabel('Cantidad de Usuarios', color='white')
    ax2.tick_params(colors='white')
    ax2.grid(True, alpha=0.15)
    
    plt.tight_layout()
    st.pyplot(fig2)
    plt.close(fig2)
    
    st.markdown("""
    **Interpretación de Planes de Suscripción:**
    El **45%** de los usuarios (3,600 clientes) se encuentra en el plan **Básico**, el **35.2%** (2,817 clientes) en el **Estándar** y el **19.8%** (1,583 clientes) en el **Premium**. Esta estructura piramidal es habitual en modelos de suscripción, pero revela una gran oportunidad de negocio: casi la mitad de la base de datos está monetizada al menor nivel posible. Existe un espacio significativo para campañas de *upselling* enfocadas en migrar a usuarios del plan Básico al Estándar o Premium mediante la promoción de beneficios específicos (como resolución 4K o pantallas simultáneas).
    """)
    st.markdown('</div>', unsafe_allow_html=True)


    # ------------------ VISUALIZACIÓN 3: BIVARIADA 1 (MATRIZ) ------------------
    st.markdown('<div class="viz-card">', unsafe_allow_html=True)
    st.markdown('<div class="viz-header">3. Matriz de Correlación Numérica (Bivariada 1)</div>', unsafe_allow_html=True)
    
    columnas_num = ['age', 'monthly_watch_time_mins', 'customer_support_tickets']
    matriz_correlacion = df[columnas_num].corr()
    
    fig3, ax3 = plt.subplots(figsize=(8, 5))
    fig3.patch.set_facecolor('#0e1117')
    ax3.set_facecolor('#0e1117')
    
    sns.heatmap(
        matriz_correlacion, annot=True, cmap='RdYlGn', vmin=-1, vmax=1, 
        fmt=".2f", linewidths=0.5, ax=ax3,
        cbar_kws={'label': 'Coeficiente de Correlación'}
    )
    ax3.set_title('Matriz de Correlación de Pearson', color='white', fontsize=12, pad=15)
    ax3.tick_params(colors='white')
    for text in ax3.texts:
        text.set_color('black')
        
    plt.tight_layout()
    st.pyplot(fig3)
    plt.close(fig3)
    
    st.markdown("""
    **Interpretación de la Matriz de Correlación:**
    Los coeficientes de correlación lineal entre las variables numéricas son extraordinariamente cercanos a cero (por ejemplo, Edad vs. Tiempo de Visualización = **0.01**, Edad vs. Tickets = **0.002**, y Tiempo de Visualización vs. Tickets = **-0.008**). Esto aporta dos conclusiones estratégicas fundamentales:
    * **Independencia Demográfica del Consumo:** La edad no influye en la cantidad de minutos consumidos ni en la generación de tickets. El streaming en esta plataforma es un comportamiento intergeneracional; los jóvenes de 18 años y los adultos de 65 años consumen contenidos y experimentan problemas de soporte bajo dinámicas de frecuencia similares.
    * **Estabilidad Operativa ante Alto Consumo:** El tiempo de visualización no se correlaciona con los tickets de soporte. Esto desmiente la hipótesis de que a mayor uso de la plataforma, más incidencias se generan. Los usuarios de alto consumo (superusuarios) no experimentan mayor fricción técnica o administrativa que los usuarios esporádicos, lo que ratifica la robustez tecnológica del reproductor y la infraestructura de servidores.
    """)
    st.markdown('</div>', unsafe_allow_html=True)


    # ------------------ VISUALIZACIÓN 4: BIVARIADA 2 (BOXPLOT) ------------------
    st.markdown('<div class="viz-card">', unsafe_allow_html=True)
    st.markdown('<div class="viz-header">4. Tiempo de Visualización por Plan de Suscripción (Bivariada 2)</div>', unsafe_allow_html=True)
    
    fig4, ax4 = plt.subplots(figsize=(10, 5))
    fig4.patch.set_facecolor('#0e1117')
    ax4.set_facecolor('#0e1117')
    
    sns.boxplot(
        x='subscription_plan', y='monthly_watch_time_mins', data=df, 
        ax=ax4, hue='subscription_plan', order=orden_planes, palette='Set2', legend=False
    )
    
    ax4.set_title('Consumo de Minutos Mensuales según Plan Contratado', color='white', fontsize=12)
    ax4.set_xlabel('Plan de Suscripción', color='white')
    ax4.set_ylabel('Minutos Mensuales', color='white')
    ax4.tick_params(colors='white')
    ax4.grid(True, alpha=0.15)
    
    plt.tight_layout()
    st.pyplot(fig4)
    plt.close(fig4)
    
    st.markdown("""
    **Interpretación del Consumo por Plan:**
    Se observa una tendencia clara e incremental de consumo a medida que se escala en la categoría del plan. Mientras que los usuarios del plan Básico promedian **591.6 minutos mensuales**, los del plan Estándar suben a **853.1 minutos** y los del Premium alcanzan los **1,019.8 minutos** (una mediana de 1,081 minutos). Esto demuestra que los planes superiores no solo incrementan el ARPU de forma directa por su precio de suscripción, sino que están asociados a un **incremento del 72.4% en el engagement** (tiempo de visualización) respecto al plan básico. Esto valida que las características premium (calidad de video, ausencia de publicidad, etc.) actúan como catalizadores de consumo y de retención.
    """)
    st.markdown('</div>', unsafe_allow_html=True)


    # ------------------ VISUALIZACIÓN 5: MULTIVARIADA ------------------
    st.markdown('<div class="viz-card">', unsafe_allow_html=True)
    st.markdown('<div class="viz-header">5. Edad vs. Tiempo de Visualización segmentado por Plan (Multivariada)</div>', unsafe_allow_html=True)
    
    fig5, ax5 = plt.subplots(figsize=(11, 6))
    fig5.patch.set_facecolor('#0e1117')
    ax5.set_facecolor('#0e1117')
    
    sns.scatterplot(
        data=df, x='age', y='monthly_watch_time_mins', hue='subscription_plan', 
        hue_order=orden_planes, palette=colores_semaforo, alpha=0.6, ax=ax5
    )
    
    ax5.set_title('Relación Edad vs Tiempo de Visualización por Plan', color='white', fontsize=12)
    ax5.set_xlabel('Edad', color='white')
    ax5.set_ylabel('Minutos Mensuales', color='white')
    ax5.tick_params(colors='white')
    ax5.legend(facecolor='#0e1117', edgecolor='none', labelcolor='white')
    ax5.grid(True, alpha=0.15)
    
    plt.tight_layout()
    st.pyplot(fig5)
    plt.close(fig5)
    
    st.markdown("""
    **Interpretación del Análisis Multivariado:**
    El gráfico de dispersión confirma visualmente la nula correlación entre la edad y el consumo, mostrando una nube homogénea a lo largo del eje horizontal. Sin embargo, en el eje vertical se evidencia una nítida estratificación de colores: los puntos verdes (Premium) y amarillos (Estándar) se desplazan consistentemente hacia la parte superior en comparación con los puntos rojos (Básico). Esto ratifica que **el plan de suscripción es la variable que mejor explica e impulsa el nivel de consumo en la plataforma**, siendo independiente de los factores demográficos del usuario.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

else:
    st.info("Por favor, asegúrate de haber ejecutado los scripts de limpieza previos para generar el dataset procesado.")
