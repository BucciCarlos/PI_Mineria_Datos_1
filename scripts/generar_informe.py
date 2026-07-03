import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def draw_header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica', 8)
    canvas.setFillColor(colors.HexColor('#7f8c8d'))
    
    # Header text
    canvas.drawString(36, 755, "TRABAJO FINAL INTEGRADOR — MINERÍA DE DATOS I")
    canvas.drawRightString(576, 755, "Comisión: Nodo Tecnológico")
    
    # Header line
    canvas.setStrokeColor(colors.HexColor('#bdc3c7'))
    canvas.setLineWidth(0.5)
    canvas.line(36, 748, 576, 748)
    
    # Footer line
    canvas.line(36, 48, 576, 48)
    
    # Footer text (Left: Links, Right: Page)
    canvas.drawString(36, 36, "Repositorio GitHub: https://github.com/BucciCarlos/PI_Mineria_Datos_1")
    canvas.drawString(36, 24, "Dashboard Streamlit: https://buccicarlos-pi-mineria-datos-1.streamlit.app/")
    canvas.drawRightString(576, 36, f"Página {doc.page} de 2")
    canvas.restoreState()

def generate_pdf():
    pdf_dir = os.path.join(os.getcwd(), 'reports')
    os.makedirs(pdf_dir, exist_ok=True)
    pdf_path = os.path.join(pdf_dir, "informe_final.pdf")
    
    # Margins adjusted to 54 points top/bottom to cleanly accommodate header/footer
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=54,
        bottomMargin=54
    )
    
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor('#e74c3c'),
        alignment=1, # Center
        spaceAfter=6
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15,
        textColor=colors.HexColor('#2c3e50'),
        alignment=1, # Center
        spaceAfter=8
    )
    
    meta_style = ParagraphStyle(
        'DocMeta',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=11,
        textColor=colors.HexColor('#7f8c8d'),
        alignment=1, # Center
        spaceAfter=12
    )
    
    h1_style = ParagraphStyle(
        'SectionH1',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=14,
        textColor=colors.HexColor('#2c3e50'),
        spaceBefore=10,
        spaceAfter=6,
        keepWithNext=True
    )
    
    body_style = ParagraphStyle(
        'SectionBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12,
        textColor=colors.HexColor('#2c3e50'),
        spaceAfter=6
    )
    
    bullet_style = ParagraphStyle(
        'SectionBullet',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12,
        textColor=colors.HexColor('#2c3e50'),
        leftIndent=15,
        firstLineIndent=-10,
        spaceAfter=4
    )
    
    table_text_style = ParagraphStyle(
        'TableText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=10,
        textColor=colors.HexColor('#2c3e50')
    )
    
    table_header_style = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=colors.white
    )
    
    story = []
    
    # ------------------ PAGE 1 ------------------
    # Title
    story.append(Paragraph("TRABAJO FINAL INTEGRADOR", title_style))
    story.append(Paragraph("Minería de Datos - Comportamiento de Usuarios de Streaming en Latinoamérica", subtitle_style))
    story.append(Paragraph(
        "<b>Materia:</b> Minería de Datos | <b>Comisión:</b> 1 | <b>Fecha:</b> 8 de Julio de 2026<br/>"
        "<b>Integrantes:</b> Bucci, Carlos Matias y Carabajal, Elba Julieta<br/>"
        "<b>GitHub:</b> <a href='https://github.com/BucciCarlos/PI_Mineria_Datos_1'><font color='#2980b9'><u>https://github.com/BucciCarlos/PI_Mineria_Datos_1</u></font></a> | "
        "<b>Streamlit:</b> <a href='https://buccicarlos-pi-mineria-datos-1.streamlit.app/'><font color='#2980b9'><u>https://buccicarlos-pi-mineria-datos-1.streamlit.app/</u></font></a>",
        meta_style
    ))
    
    # Divider line
    divider = Table([[""]], colWidths=[540], rowHeights=[2])
    divider.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#e74c3c')),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(divider)
    story.append(Spacer(1, 10))
    
    # 1. Contexto y objetivo
    story.append(Paragraph("1. Contexto y Objetivo", h1_style))
    story.append(Paragraph(
        "El presente informe consolida el análisis de comportamiento y consumo de una base de 8,000 usuarios de streaming en Latinoamérica. "
        "El objetivo principal es extraer patrones de uso del servicio, dimensionar la carga del soporte técnico regional, evaluar la "
        "relación directa de la oferta de planes con el engagement del cliente, y verificar la efectividad de la reducción dimensional "
        "para modelar estas conductas, facilitando decisiones estratégicas orientadas a maximizar la retención y el ARPU.",
        body_style
    ))
    
    # 2. Dataset y calidad inicial
    story.append(Paragraph("2. Dataset y Calidad Inicial", h1_style))
    story.append(Paragraph(
        "El dataset original (8,160 registros) presentaba múltiples deficiencias de calidad ("
        "valores nulos distribuidos en visualizaciones, géneros y fechas; registros duplicados parciales y absolutos; e inconsistencias "
        "numéricas como valores negativos en tiempos y tickets). La auditoría determinó la necesidad de aplicar un riguroso proceso de "
        "limpieza y curación de datos en origen antes de proceder con el modelado o análisis exploratorio.",
        body_style
    ))
    
    # 3. Decisiones de limpieza
    story.append(Paragraph("3. Decisiones de Limpieza y ETL", h1_style))
    story.append(Paragraph(
        "Para subsanar las inconsistencias, se diseñó un pipeline de ETL con las siguientes reglas operativas:",
        body_style
    ))
    
    decisions = [
        "<b>Edades Ilógicas:</b> Los registros fuera del rango [18-100] se consideraron errores y se imputaron con la mediana (35 años).",
        "<b>Normalización Geográfica:</b> Se estandarizaron nombres mal escritos o abreviados de países (ej. 'BRA', 'CHL' -> 'Brasil', 'Chile').",
        "<b>Datos Faltantes:</b> En <i>favorite_genre</i> los nulos se marcaron como 'Desconocido'. En métricas cuantitativas, se aplicó valor absoluto (abs()) para corregir negativos, e imputación con 0 ante valores nulos.",
        "<b>Duplicados:</b> Se eliminaron duplicados absolutos y se resolvieron duplicados parciales de ID seleccionando el registro más íntegro."
    ]
    for dec in decisions:
        story.append(Paragraph(f"• {dec}", bullet_style))
        
    story.append(Spacer(1, 5))
    story.append(Paragraph("<b>Métricas del Pipeline de Calidad de Datos (ETL):</b>", body_style))
    
    # Compact table of ETL pipeline
    data_etl = [
        [Paragraph("Paso / Proceso", table_header_style), 
         Paragraph("Descripción resumida", table_header_style), 
         Paragraph("Filas", table_header_style), 
         Paragraph("Nulos", table_header_style), 
         Paragraph("Retención (%)", table_header_style)],
        [Paragraph("1. Carga Inicial", table_text_style), Paragraph("Datos crudos de streaming_users_dirty.json", table_text_style), Paragraph("8,160", table_text_style), Paragraph("753", table_text_style), Paragraph("100.00%", table_text_style)],
        [Paragraph("2. Curación Variables", table_text_style), Paragraph("Imputación edad y normalización países/géneros", table_text_style), Paragraph("8,160", table_text_style), Paragraph("513", table_text_style), Paragraph("100.00%", table_text_style)],
        [Paragraph("3. Corrección Métricas", table_text_style), Paragraph("Fechas a datetime, valor absoluto en negativos", table_text_style), Paragraph("8,160", table_text_style), Paragraph("769", table_text_style), Paragraph("100.00%", table_text_style)],
        [Paragraph("4. Depuración Final", table_text_style), Paragraph("Eliminación de duplicados y resolución de IDs", table_text_style), Paragraph("8,000", table_text_style), Paragraph("759*", table_text_style), Paragraph("98.04%", table_text_style)]
    ]
    
    t1 = Table(data_etl, colWidths=[90, 240, 60, 70, 80])
    t1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#2c3e50')),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#bdc3c7')),
        ('BACKGROUND', (0,1), (-1,-1), colors.HexColor('#f8f9fa')),
    ]))
    story.append(t1)
    story.append(Paragraph("<font size=7 color='#7f8c8d'>*Nota: Los nulos remanentes corresponden a valores NaT legítimos tras convertir fechas no interpretables.</font>", body_style))
    
    # Force PageBreak
    story.append(PageBreak())
    
    # ------------------ PAGE 2 ------------------
    # 4. Hallazgos del EDA
    story.append(Paragraph("4. Hallazgos Clave del Análisis Exploratorio de Datos (EDA)", h1_style))
    story.append(Paragraph(
        "A través de los análisis univariado, bivariado y multivariado, se obtuvieron las siguientes conclusiones empíricas:",
        body_style
    ))
    
    eda_findings = [
        "<b>Consumo e Ingresos:</b> El 45% de los usuarios contrata el plan Básico (consumo medio de 591.6 mins/mes), el 35.2% el Estándar (853.1 mins/mes) y el 19.8% el Premium (1,019.8 mins/mes). Premium representa un engagement 72.4% superior, validando la escala comercial.",
        "<b>Estabilidad Regional de Soporte:</b> Las reclamaciones promedio por usuario se mantienen estables entre 0.77 (Brasil/Colombia) y 0.82 (Argentina), con un promedio global de 0.79 tickets. La homogeneidad geográfica demuestra la consistencia del soporte en Latinoamérica.",
        "<b>Fricción Específica en Cuentas Premium:</b> En Chile (0.92) y Perú (0.89) el promedio de tickets de clientes Premium excede la media básica (0.76), indicando fallos o complejidad en funciones avanzadas (como UHD/4K o multi-pantallas).",
        "<b>Independencia de Consumo:</b> Los coeficientes de correlación entre edad, minutos y tickets son casi nulos (r < 0.01). El consumo de contenidos y las quejas técnicas son transversales e independientes de la edad del usuario."
    ]
    for find in eda_findings:
        story.append(Paragraph(f"• {find}", bullet_style))
        
    story.append(Spacer(1, 4))
    
    # 5. PCA
    story.append(Paragraph("5. Análisis de Componentes Principales (PCA)", h1_style))
    story.append(Paragraph(
        "Se corrió un PCA con <i>StandardScaler</i> sobre edad, minutos de visualización y tickets de soporte. "
        "Los resultados de varianza explicada se muestran a continuación:",
        body_style
    ))
    
    data_pca = [
        [Paragraph("Componente", table_header_style), 
         Paragraph("Varianza Explicada (%)", table_header_style), 
         Paragraph("Varianza Acumulada (%)", table_header_style), 
         Paragraph("Variables Dominantes (Loadings)", table_header_style)],
        [Paragraph("PC1", table_text_style), Paragraph("33.74%", table_text_style), Paragraph("33.74%", table_text_style), Paragraph("Watch Time (0.735) / Edad (0.564) [Consumo de Alto Valor]", table_text_style)],
        [Paragraph("PC2", table_text_style), Paragraph("33.41%", table_text_style), Paragraph("67.15%", table_text_style), Paragraph("Support Tickets (0.800) / Edad (0.597) [Fricción en Edad Avanzada]", table_text_style)],
        [Paragraph("PC3", table_text_style), Paragraph("32.85%", table_text_style), Paragraph("100.00%", table_text_style), Paragraph("Watch Time (0.675) / Edad (-0.569) [Consumo Joven]", table_text_style)]
    ]
    t2 = Table(data_pca, colWidths=[80, 110, 110, 240])
    t2.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#2c3e50')),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#bdc3c7')),
        ('BACKGROUND', (0,1), (-1,-1), colors.HexColor('#f8f9fa')),
    ]))
    story.append(t2)
    
    story.append(Spacer(1, 4))
    story.append(Paragraph(
        "<b>Inefectividad de la Reducción y Superposición:</b> Debido a que las variables de origen no tienen correlación lineal ($r \\approx 0$), "
        "cada componente explica casi un tercio de la varianza. PCA no comprime la información de forma efectiva (perder una componente implica "
        "perder el 32.85% de la información). La proyección PC1 vs. PC2 muestra un solapamiento total de las nubes de puntos de los tres planes "
        "de suscripción. Esto concluye que el plan comercial contratado no segrega perfiles demográficos o conductuales diferenciados.",
        body_style
    ))
    
    # 6. Conclusiones y limitaciones
    story.append(Paragraph("6. Conclusiones y Limitaciones del Dataset", h1_style))
    
    conclusions = [
        "<b>Campañas de Upselling:</b> Se recomienda incentivar la migración de plan al 45% de clientes Básicos con consumos superiores a la media.",
        "<b>Auditoría Operativa Regional:</b> Capacitar en soporte técnico avanzado en Chile y Perú para solventar las quejas en cuentas Premium.",
        "<b>Segmentación por Clustering:</b> Implementar algoritmos no supervisados (K-Means) para obtener una segmentación conductual real.",
        "<b>Outliers Temporales (Limitación):</b> Se identificaron 15 registros futuros anómalos con fecha <i>2029-01-01</i> (0.18% de la muestra). Se infiere que es un error del sistema (valor por defecto ante datos corruptos). Su baja presencia no sesga los análisis de este reporte, pero representa una limitación de origen.",
        "<b>Mejora Propuesta:</b> Programar una regla de validación temporal en el pipeline (<i>last_login_date > datetime.now()</i>) para aislar o imputar con <i>NaT</i>."
    ]
    for conc in conclusions:
        story.append(Paragraph(f"• {conc}", bullet_style))
        
    doc.build(story, onFirstPage=draw_header_footer, onLaterPages=draw_header_footer)
    print("PDF generated successfully!")

if __name__ == '__main__':
    generate_pdf()
