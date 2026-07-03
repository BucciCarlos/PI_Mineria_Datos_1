# 🎬 Trabajo Final Integrador - Minería de Datos
> **Materia:** Minería de Datos | **Comisión:** Nodo Tecnológico | **Entrega Final:** 8 de Julio de 2026

---

### 🌐 Aplicación y Recursos
* **Dashboard Interactivo:** [🔗 Ver Aplicación en Streamlit Cloud](https://buccicarlos-pi-mineria-datos-1.streamlit.app/)
* **Repositorio GitHub:** [🐙 Ver Repositorio en GitHub](https://github.com/BucciCarlos/PI_Mineria_Datos_1)

---

## 🎯 Objetivo del Proyecto
Este proyecto de minería de datos realiza un análisis exploratorio (EDA) y una reducción dimensional (PCA) sobre una base de usuarios de streaming en Latinoamérica. El objetivo comercial es comprender los patrones de consumo (tiempo de visualización mensual), estimar la carga operativa de soporte técnico y evaluar el impacto del modelo de suscripción sobre el engagement. Se proponen estrategias comerciales de up-selling dirigidas, optimizaciones operativas y una transición hacia una segmentación avanzada.

---

## 📊 Dataset
La base de datos original contiene registros correspondientes a **8,000 usuarios** en Latinoamérica tras su depuración (inicialmente 8,160 registros en el dataset dirty). Las variables de estudio son:
* `user_id`: Identificador único de usuario (clave primaria).
* `age`: Edad de los usuarios (rango 18-80 años).
* `subscription_plan`: Plan activo (Básico, Estándar, Premium).
* `country`: País de residencia (Chile, Brasil, México, Uruguay, Colombia, Perú, Argentina).
* `favorite_genre`: Género favorito del usuario.
* `last_login_date`: Fecha del último inicio de sesión.
* `monthly_watch_time_mins`: Minutos de visualización mensual.
* `customer_support_tickets`: Tickets de soporte técnico en el mes.

---

## 🧹 Preparación y Calidad de Datos
El dataset crudo presentaba inconsistencias severas corregidas mediante el siguiente pipeline:
1. **Edades ilógicas (<18 o >100):** Convertidas a NaN e imputadas con la mediana (35 años).
2. **Normalización geográfica:** Remoción de espacios y mapeo de abreviaturas/errores ortográficos de países.
3. **Géneros favoritos nulos:** Reemplazo por la etiqueta *"Desconocido"* para no inyectar sesgos arbitrarios.
4. **Formateo de fechas:** Conversión a datetime (errors='coerce') marcando fechas ilegibles como NaT.
5. **Corrección de métricas:** Conversión de valores negativos a positivos (`abs()`) e imputación con 0.
6. **Duplicados:** Eliminación de duplicados absolutos y resolución de IDs duplicados mediante un ranking de calidad.
7. **Outliers temporales:** Identificación de 15 registros con fecha futura *"2029-01-01"* tomados como error de backend.

El dataset limpio final fue exportado con **8,000 registros** estables.

---

## 📈 Resumen del Análisis Exploratorio (EDA)
Los hallazgos clave derivados de las 5 visualizaciones del EDA son:
* **Distribución demográfica:** Uniforme en Latinoamérica con edad centrada en 35 años y balance de género favorito.
* **Distribución de planes:** El **45%** de los usuarios está en el plan Básico, representando un gran pool para campañas de up-selling.
* **Correlaciones lineales:** No hay correlación lineal entre la edad, el consumo y la generación de tickets de soporte técnico ($r \approx 0$).
* **Soporte regional:** La estabilidad operativa de soporte es homogénea en la región (promedio de 0.77 a 0.82 tickets/usuario).
* **Consumo por planes:** Los planes Premium impulsan el engagement, aumentando el tiempo de visualización un **72.4%** respecto al Básico.
* **Fricción en cuentas Premium:** En Chile y Perú, los usuarios Premium generan más tickets (0.92 y 0.89), indicando fricción en funciones avanzadas.
* **Logins mensuales:** La línea temporal es estable (65-100 logins/mes) con un pico anómalo de 451 logins en febrero de 2022.

---

## 🧬 Reducción de Dimensionalidad (PCA)
Se aplicó PCA sobre edad, tiempo de visualización y tickets de soporte, estandarizados con `StandardScaler`:
* **Varianza Explicada:** PC1 (33.74%), PC2 (33.41%), PC3 (32.85%).
* **Varianza Acumulada (PC1 + PC2):** 67.15%.
* **Ineficacia de la reducción:** Dado que las variables son independientes (correlación $\approx 0$), la varianza se reparte por igual en cada componente. Reducir a dos componentes pierde un **32.85%** de la información (casi el equivalente de descartar una variable completa).
* **Proyección PC1 vs PC2:** Muestra una nube única de datos con solapamiento masivo de los planes. La clasificación por planes comerciales no describe grupos conductuales aislados, justificando una segmentación avanzada.

---

## 🏆 Conclusiones
* **Engagement por planes:** El plan de suscripción contratado es el principal diferenciador del tiempo de consumo mensual, no la edad.
* **Soporte regional:** La carga de soporte es uniforme continentalmente, pero requiere especialización premium en Chile y Perú.
* **Outliers Temporales:** Se documenta una limitación en la calidad de datos de origen debido a 15 registros futuros (2029-01-01) anómalos.
* **Mejoras del Pipeline:** Se propone como mejora implementar una validación temporal dinámica en el pipeline de limpieza para imputar a NaT.
* **Segmentación Avanzada:** La segmentación comercial por planes se solapa en su comportamiento, sugiriendo el uso de clustering **K-Means**.

---

## ⚙️ Instrucciones de Ejecución Local

1. **Instalar dependencias en el entorno virtual:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Ejecutar la aplicación interactiva Streamlit:**
   ```bash
   streamlit run app/Home.py
   ```
3. **Explorar los notebooks en Jupyter Notebook:**
   ```bash
   jupyter notebook notebooks/
   ```

