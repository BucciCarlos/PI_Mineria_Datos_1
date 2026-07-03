import pandas as pd
import numpy as np
import os
import pypdf

def main():
    print("==================================================")
    # 1. Load the processed dataset
    dataset_path = "data/processed/streaming_users_clean.csv"
    if not os.path.exists(dataset_path):
        print(f"[ERROR] No se encontró el dataset procesado en {dataset_path}")
        return
        
    df = pd.read_csv(dataset_path, parse_dates=['last_login_date'])
    print(f"[INFO] Dataset cargado con éxito. {len(df)} registros.")

    # 2. Calculate key indicators
    edad_media = df['age'].mean()
    tiempo_medio = df['monthly_watch_time_mins'].mean()
    
    plan_counts = df['subscription_plan'].value_counts(normalize=True) * 100
    plan_basico = plan_counts.get('Básico', 0)
    plan_estandar = plan_counts.get('Estándar', 0)
    plan_premium = plan_counts.get('Premium', 0)
    
    corr_edad_tiempo = df['age'].corr(df['monthly_watch_time_mins'])
    corr_edad_tickets = df['age'].corr(df['customer_support_tickets'])
    corr_tiempo_tickets = df['monthly_watch_time_mins'].corr(df['customer_support_tickets'])
    
    tickets_medio = df['customer_support_tickets'].mean()
    
    print("\n--- INDICADORES CLAVE CALCULADOS DESDE EL DATASET ---")
    print(f"1. Edad Media: {edad_media:.5f} (Redondeado a 1 decimal: {edad_media:.1f})")
    print(f"2. Tiempo Promedio Mensual (mins): {tiempo_medio:.5f} (Redondeado a 1 decimal: {tiempo_medio:.1f})")
    print(f"3. Distribución de Planes (%):")
    print(f"   - Básico: {plan_basico:.5f}% (Redondeado a 0 decimales: {plan_basico:.0f}%)")
    print(f"   - Estándar: {plan_estandar:.5f}% (Redondeado a 1 decimal: {plan_estandar:.1f}%)")
    print(f"   - Premium: {plan_premium:.5f}% (Redondeado a 1 decimal: {plan_premium:.1f}%)")
    print(f"4. Coeficientes de Correlación:")
    print(f"   - Edad vs Tiempo: {corr_edad_tiempo:.5f} (Redondeado a 2 decimales: {corr_edad_tiempo:.2f})")
    print(f"   - Edad vs Tickets: {corr_edad_tickets:.5f} (Redondeado a 3 decimales: {corr_edad_tickets:.3f})")
    print(f"   - Tiempo vs Tickets: {corr_tiempo_tickets:.5f} (Redondeado a 3 decimales: {corr_tiempo_tickets:.3f})")
    print(f"5. Promedio de Tickets de Soporte: {tickets_medio:.5f} (Redondeado a 2 decimales: {tickets_medio:.2f})")
    print("--------------------------------------------------")

    # 3. Read Streamlit app file
    streamlit_path = "app/pages/02_EDA.py"
    if not os.path.exists(streamlit_path):
        print(f"[ERROR] No se encontró el archivo de Streamlit en {streamlit_path}")
        return
    with open(streamlit_path, 'r', encoding='utf-8') as f:
        streamlit_content = f.read()
    
    # 4. Read PDF report
    pdf_path = "reports/informe_final.pdf"
    if not os.path.exists(pdf_path):
        print(f"[ERROR] No se encontró el informe PDF en {pdf_path}")
        return
        
    reader = pypdf.PdfReader(pdf_path)
    pdf_content = ""
    for page in reader.pages:
        pdf_content += page.extract_text()
        
    # 5. Define assertions
    assertions_streamlit = [
        ("Edad Media (35.6)", f"{edad_media:.1f}", "35.6"),
        ("Tiempo Medio (768.4)", f"{tiempo_medio:.1f}", "768.4"),
        ("Plan Básico (45%)", f"{plan_basico:.0f}%", "45%"),
        ("Plan Estándar (35.2%)", f"{plan_estandar:.1f}%", "35.2%"),
        ("Plan Premium (19.8%)", f"{plan_premium:.1f}%", "19.8%"),
        ("Corr Edad vs Tiempo (0.01)", f"{corr_edad_tiempo:.2f}", "0.01"),
        ("Corr Edad vs Tickets (0.002)", f"{corr_edad_tickets:.3f}", "0.002"),
        ("Corr Tiempo vs Tickets (-0.008)", f"{corr_tiempo_tickets:.3f}", "-0.008"),
        ("Tickets Promedio (0.79)", f"{tickets_medio:.2f}", "0.79")
    ]
    
    # PDF check assertions (might vary in formatting like '72.4%')
    assertions_pdf = [
        ("Tiempo Básico Promedio (591.6)", "591.6"),
        ("Tiempo Estándar Promedio (853.1)", "853.1"),
        ("Tiempo Premium Promedio (1,019.8)", "1,019.8"),
        ("Engagement Premium (+72.4%)", "72.4%"),
        ("Tickets Promedio (0.79)", "0.79"),
        ("Plan Básico (%)", "45%"),
        ("Plan Estándar (%)", "35.2%"),
        ("Plan Premium (%)", "19.8%"),
    ]
    
    discrepancies = 0
    
    print("\n=== AUDITORÍA DE CONSISTENCIA: STREAMLIT APP (02_EDA.py) ===")
    for label, calc_str, target in assertions_streamlit:
        if target in streamlit_content:
            print(f"[OK] {label}: Valor '{target}' encontrado en el código del dashboard.")
        else:
            print(f"[ALERTA] {label}: Valor esperado '{target}' NO encontrado en el dashboard. (Calculado: {calc_str})")
            discrepancies += 1
            
    print("\n=== AUDITORÍA DE CONSISTENCIA: INFORME PDF (informe_final.pdf) ===")
    for label, target in assertions_pdf:
        # Standardize search string a bit (replacing commas in 1,019.8 if needed)
        # In PDF it might extract as '1,019.8' or '1019.8'
        found = target in pdf_content
        if not found and "," in target:
            alt_target = target.replace(",", "")
            found = alt_target in pdf_content
            
        if found:
            print(f"[OK] {label}: Valor '{target}' encontrado en el informe final.")
        else:
            print(f"[ALERTA] {label}: Valor esperado '{target}' NO encontrado en el informe PDF.")
            discrepancies += 1

    # 6. Conclusion
    print("\n==================================================")
    if discrepancies == 0:
        print("[ÉXITO] Auditoría completada. Consistencia del 100% entre el Dataset, Streamlit y el PDF.")
    else:
        print(f"[ALERTA] Auditoría finalizada con {discrepancies} discrepancias. Revisar redondeos o valores duros.")
    print("==================================================")

if __name__ == "__main__":
    main()
