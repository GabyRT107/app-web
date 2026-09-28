import streamlit as st  
import pdfplumber
from pathlib import Path

# ==========================================
# 1. CONFIGURACIÓN DE LA PÁGINA
# ==========================================
st.set_page_config(  
    page_title="Plataforma de Inteligencia Artificial & Data",  
    page_icon="💻",  
    layout="wide",  
    initial_sidebar_state="expanded"  
)  

# ==========================================
# 2. GESTIÓN DEL ESTADO DE SESIÓN (SESSION STATE)
# ==========================================
if "seccion_activa" not in st.session_state:
    st.session_state.seccion_activa = "Inteligencia Artificial"

# ==========================================
# 3. ESTILOS CSS PERSONALIZADOS
# ==========================================
st.markdown("""  
<style>  
/* Encabezados principales */
.main-header {  
    font-size: 2.2rem;  
    font-weight: 700;  
    color: #1E293B;  
    margin-bottom: 0.2rem;  
}  
.sub-header {  
    font-size: 1rem;  
    color: #64748B;  
    margin-bottom: 2rem;  
}  

/* Estilo para los botones del menú lateral */
div[data-testid="stSidebar"] div.stButton > button {
    width: 100% !important;
    height: 50px !important;            
    border-radius: 10px !important;
    display: flex !important;
    align-items: center !important;     
    justify-content: center !important;
    text-align: center !important;
    padding: 8px 12px !important;
    font-size: 0.95rem !important;
    font-weight: 600 !important;
    border: 1px solid #E2E8F0 !important;
    margin-bottom: 6px !important;
    transition: all 0.2s ease !important;
}

div[data-testid="stSidebar"] div.stButton > button p {
    text-align: center !important;
    width: 100% !important;
    margin: 0 !important;
}

div[data-testid="stSidebar"] div.stButton > button[kind="primary"] {
    background-color: #E63946 !important; 
    color: #FFFFFF !important;
    border-color: #E63946 !important;
    font-weight: 700 !important;
}

div[data-testid="stSidebar"] div.stButton > button[kind="primary"] p {
    color: #FFFFFF !important;
}

/* Tarjetas y contenedores */  
.card {  
    background-color: #F8FAFC;  
    border: 1px solid #E2E8F0;  
    border-radius: 16px;  
    padding: 28px;  
    margin-top: 10px;  
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05), 0 4px 6px -2px rgba(0, 0, 0, 0.025);  
    transition: transform 0.2s ease, box-shadow 0.2s ease;  
}  
.category-tag {  
    background-color: #E0F2FE;  
    color: #0369A1;  
    font-size: 0.85rem;  
    font-weight: 600;  
    padding: 4px 12px;  
    border-radius: 16px;  
    display: inline-block;  
    margin-bottom: 12px;  
}  
.term-title {  
    color: #0F172A;  
    font-size: 1.8rem;  
    font-weight: 700;  
    margin-bottom: 12px;  
}  
.term-desc {  
    color: #334155;  
    font-size: 1.05rem;  
    line-height: 1.6;  
}  

.link-button {  
    display: inline-block;  
    background-color: #231EB3;  
    color: white !important;  
    padding: 12px 24px;  
    border-radius: 10px;  
    text-decoration: none;  
    font-weight: 600;  
    font-size: 1rem;  
    margin-top: 15px;  
}  

div[data-testid="stImage"] img {  
    display: block;  
    margin-left: auto;  
    margin-right: auto;  
    border-radius: 10px;  
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);  
}  
</style>  
""", unsafe_allow_html=True)  

# ==========================================
# 4. BASE DE DATOS DEL GLOSARIO
# ==========================================
GLOSARIO = {  
    "IA Simbólica": {  
        "categoria": "Inteligencia Artificial",  
        "descripcion": "Enfoque tradicional de la IA basado en lógica formal, reglas explícitas y representación del conocimiento humano mediante símbolos manipulables."  
    },  
    "IA Generativa": {  
        "categoria": "Inteligencia Artificial",  
        "descripcion": "Rama de la IA capaz de crear nuevo contenido original (texto, imágenes, audio, código) a partir de patrones aprendidos de datos existentes."  
    },  
    "Aprendizaje Automático": {
        "categoria": "Fundamentos de IA",
        "descripcion": "Subcampo de la IA que permite a los sistemas aprender y mejorar automáticamente a partir de la experiencia y los datos, sin ser programados explícitamente.",
        "ejemplo": "Las plataformas de streaming musical necesitan atraer y retener usuarios recomendándoles canciones que se adapten a sus preferencias individuales en un catálogo masivo de lanzamientos. Para lograrlo, implementan modelos de Machine Learning entrenados con patrones de escucha y características de audio.\n\nDatos de Entrada:\n- Características del audio: La estructura física y acústica de la canción.\n- Historial de comportamiento del usuario: El registro de secuencias de reproducción.\n\nProcesamiento:\nAlgoritmos de filtrado colaborativo y procesamiento de señal analizan la relación entre la estructura musical y los patrones de reproducción guardados.\n\nDatos de Salida:\nSugerencia personalizada de canciones."
    },
    "Big Data": {  
        "categoria": "Datos e Infraestructura",  
        "descripcion": "Conjunto de datos masivos y complejos que superan las capacidades del software tradicional para su procesamiento."  
    },  
    "Sistemas adaptativos de autoaprendizaje": {  
        "categoria": "Sistemas Inteligentes",  
        "descripcion": "Sistemas diseñados para modificar automáticamente sus algoritmos en tiempo real según los cambios en su entorno."  
    },  
    "Aprendizaje profundo": {  
        "categoria": "Fundamentos de IA",  
        "descripcion": "Subconjunto del Aprendizaje Automático basado en redes neuronales artificiales de múltiples capas."  
    },  
    "Procesamiento de lenguaje natural (PLN)": {  
        "categoria": "Aplicaciones de IA",  
        "descripcion": "Disciplina que permite a las computadoras comprender e interpretar lenguaje humano hablado o escrito."  
    },  
    "Disciplina Tecnológica": {  
        "categoria": "Fundamentos",  
        "descripcion": "Campo metódico dedicado al desarrollo, aplicación y gestión responsable de soluciones tecnológicas."  
    },  
    "Ciencia de Datos": {  
        "categoria": "Datos e Infraestructura",  
        "descripcion": "Campo interdisciplinario que combina estadística y programación para extraer conocimientos a partir de datos."  
    },  
    "Máquina Virtual": {  
        "categoria": "Datos e Infraestructura",  
        "descripcion": "Entorno informático de software que emula un sistema físico completo."  
    },  
    "Sistema de Expertos": {  
        "categoria": "Inteligencia Artificial",  
        "descripcion": "Sistema informático que emula la capacidad de toma de decisiones de un experto humano."  
    },  
    "Internet de las cosas (IoT)": {  
        "categoria": "Hardware & Redes",  
        "descripcion": "Red de objetos físicos interconectados provistos de sensores y software."  
    },  
    "Tecnología operativa (OT)": {  
        "categoria": "Hardware & Redes",  
        "descripcion": "Hardware y software utilizado para monitorear y controlar dispositivos físicos e infraestructura industrial."  
    },  
    "Visión Artificial": {  
        "categoria": "Aplicaciones de IA",  
        "descripcion": "Campo de la IA que entrena a las computadoras para interpretar el mundo visual mediante imágenes y video."  
    },  
    "Computación Cognitiva": {  
        "categoria": "Sistemas Inteligentes",  
        "descripcion": "Uso de modelos computadorizados para simular el proceso de pensamiento humano."  
    },  
    "Ingeniería de Prompts": {  
        "categoria": "IA Generativa",  
        "descripcion": "Práctica de estructurar instrucciones para obtener las mejores respuestas de modelos de IA."  
    },  
    "Modelos de lenguajes grandes (LLM)": {  
        "categoria": "IA Generativa",  
        "descripcion": "Modelos de aprendizaje profundo entrenados con enormes cantidades de texto."  
    },  
    "Redes Neuronales Convolucionales (CNN)": {  
        "categoria": "Aprendizaje Profundo",  
        "descripcion": "Arquitectura de red neuronal diseñada para procesar datos como imágenes y video."  
    },  
    "IA Multimodal": {  
        "categoria": "IA Avanzada",  
        "descripcion": "Sistemas capaces de procesar múltiples tipos de datos de entrada simultáneamente."  
    },  
    "IA Responsable": {  
        "categoria": "Gobernanza & Ética",  
        "descripcion": "Enfoque metódico para el desarrollo de sistemas de IA seguros, transparentes y éticos."  
    }  
}  

# ==========================================
# 5. FUNCIONES AUXILIARES OPTIMIZADAS
# ==========================================

def mostrar_imagen_centrada(ruta):  
    col1, col2, col3 = st.columns([1, 2, 1])  
    with col2:  
        st.image(ruta)  

# Extrae páginas como imágenes con caché
@st.cache_data
def obtener_paginas_pdf(ruta_pdf):
    pdf_path = Path(ruta_pdf)
    if not pdf_path.is_file():
        return None, None, "Archivo no encontrado en el sistema."
    
    try:
        imagenes = []
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                pil_image = page.to_image(resolution=150).original
                imagenes.append(pil_image)
        
        with open(pdf_path, "rb") as f:
            bytes_data = f.read()
            
        return imagenes, bytes_data, None
    except Exception as e:
        return None, None, str(e)

# Visor flexible y centrado para PDF
def mostrar_pdf_integrado(ruta_pdf):
    imagenes, bytes_data, error = obtener_paginas_pdf(ruta_pdf)
    
    if imagenes:
        # Barra de control superior para el usuario
        ctrl_col1, ctrl_col2 = st.columns([2, 1])
        
        with ctrl_col1:
            st.download_button(
                label="📥 Descargar archivo PDF",
                data=bytes_data,
                file_name=Path(ruta_pdf).name,
                mime="application/pdf"
            )
        
        with ctrl_col2:
            # Control de tamaño para el usuario
            ancho_slider = st.select_slider(
                "🔍 Tamaño de lectura:",
                options=["Pequeño", "Cómodo", "Grande", "Ancho completo"],
                value="Cómodo"
            )
        
        st.markdown("---")
        
        # Mapeo de proporciones de columnas para el centrado
        márgenes = {
            "Pequeño": [2, 3, 2],
            "Cómodo": [1.5, 4, 1.5],
            "Grande": [0.8, 5, 0.8],
            "Ancho completo": [0.01, 1, 0.01]
        }
        
        relacion_cols = márgenes[ancho_slider]

        # Muestra cada página centrada según el ancho elegido
        for idx, img in enumerate(imagenes):
            c_left, c_center, c_right = st.columns(relacion_cols)
            with c_center:
                st.caption(f"Página {idx + 1} de {len(imagenes)}")
                st.image(img, use_container_width=True)
                st.markdown("<br>", unsafe_allow_html=True)
    else:
        st.warning(
            f"⚠️ **Archivo no detectado:** `{ruta_pdf}`\n\n"
            f"Detalle: {error}\n\n"
            "Asegúrate de que el archivo se encuentre en `documentos/Actividad_Desarrollo_Subproducto_No_5_Ensayo.pdf`."
        )

# ==========================================
# 6. MENÚ LATERAL DE NAVEGACIÓN
# ==========================================
st.sidebar.title("Navegación")  

opciones_menu = [
    "Inteligencia Artificial", 
    "Antecedentes", 
    "Clasificación Clásica", 
    "Disciplinas", 
    "Herramientas", 
    "Ensayo",
    "Glosario"
]

for opcion in opciones_menu:
    es_activo = (st.session_state.seccion_activa == opcion)
    tipo_boton = "primary" if es_activo else "secondary"
    
    if st.sidebar.button(
        opcion, 
        key=f"btn_{opcion}", 
        type=tipo_boton, 
        use_container_width=True
    ):
        st.session_state.seccion_activa = opcion
        st.rerun()

seccion = st.session_state.seccion_activa

# ==========================================
# 7. CONTENIDOS Y VISTAS PRINCIPALES
# ==========================================

# --- SECCIÓN: INTELIGENCIA ARTIFICIAL ---
if seccion == "Inteligencia Artificial":  
    st.markdown('<div class="main-header">¿Qué es la inteligencia artificial (IA)?</div>', unsafe_allow_html=True)  
    st.write(  
        "**Inteligencia Artificial** es un campo interdisciplinario dedicado al "   
        "diseño de sistemas capaces de realizar tareas asociadas con la inteligencia"  
        " humana, como aprender, razonar, reconocer patrones, comprender lenguaje, resolver problemas y tomar decisiones."  
    )  
    mostrar_imagen_centrada("img/IA.jpg")  

# --- SECCIÓN: ANTECEDENTES ---
elif seccion == "Antecedentes":  
    st.markdown('<div class="main-header">Antecedentes de la IA</div>', unsafe_allow_html=True)  
    st.markdown('<div class="sub-header">Evolución histórica y momentos clave en el desarrollo de la IA.</div>', unsafe_allow_html=True)  

    tab1, tab2, tab3 = st.tabs(["Parte de 1950 a 1966", "Parte de 1979 a 2002", "Parte de 2011 a 2021"])  

    with tab1:  
        mostrar_imagen_centrada("img/1.jpg")  

    with tab2:  
        mostrar_imagen_centrada("img/2.jpg")  

    with tab3:  
        mostrar_imagen_centrada("img/3.jpg")  

# --- SECCIÓN: CLASIFICACIÓN CLÁSICA ---
elif seccion == "Clasificación Clásica":  
    st.markdown('<div class="main-header">Clasificación Clásica de la IA</div>', unsafe_allow_html=True)  
    
    tab01, tab02, tab03 = st.tabs(["IA Débil", "IA fuerte", "Superinteligencia artificial"])  
    
    with tab01:  
        st.write(  
            "**IA débil o estrecha (Narrow AI):** Está diseñada para resolver tareas específicas: traducción, recomendación, reconocimiento de imágenes, reconocimiento de voz, generación de texto, recomendaciones de productos."  
        )  
        mostrar_imagen_centrada("img/4.png")  
    
    with tab02:  
        st.write(  
            "**IA fuerte o general (AGI- General Artificial Intelligence):** Busca crear máquinas con inteligencia humana completa. Es una categoría hipotética."  
        )  
        mostrar_imagen_centrada("img/5.png")  
    
    with tab03:  
        st.write(  
            "**IA superinteligente:** Hace referencia a un sistema que superaría a los humanos en absolutamente todas las áreas cognitivas."  
        )  
        mostrar_imagen_centrada("img/6.png")  

# --- SECCIÓN: DISCIPLINAS ---
elif seccion == "Disciplinas":  
    st.markdown('<div class="main-header">Disciplinas Relacionadas</div>', unsafe_allow_html=True)  
    st.markdown('<div class="sub-header">Áreas de estudio que convergen en el ecosistema de IA y Datos.</div>', unsafe_allow_html=True)  

    pestanas = ["Filosofía", "Matemáticas", "Psicología", "Computación", "Lingüística", "Economía", "Neurociencia"]  
    t1, t2, t3, t4, t5, t6, t7 = st.tabs(pestanas)  

    with t1:  
        st.write("**Filosofía:** Aristóteles (300 AC) Describe los silogismos y conclusiones racionales.")  
        mostrar_imagen_centrada("img/Filosofia.jpg")  

    with t2:  
        st.write("**Matemáticas:** Razonamiento con algoritmos y modelación de fenómenos.")  
        mostrar_imagen_centrada("img/Matematicas.jpg")  

    with t3:  
        st.write("**Psicología:** Considera a los seres vivos como procesadores de información.")  
        mostrar_imagen_centrada("img/Psicologia.jpg")  

    with t4:  
        st.write("**Computación:** Implementación en artefactos y modelado cognitivo.")  
        mostrar_imagen_centrada("img/Computacion.jpg")  

    with t5:  
        st.write("**Lingüística:** Procesamiento del lenguaje natural.")  
        mostrar_imagen_centrada("img/Linguistica.jpg")  

    with t6:  
        st.write("**Economía:** Toma de decisiones y Teoría de juegos.")  
        mostrar_imagen_centrada("img/Economia.jpeg")  

    with t7:  
        st.write("**Neurociencia:** Procesamiento cerebral de la información.")  
        mostrar_imagen_centrada("img/Neurociencia.jpg")  

# --- SECCIÓN: HERRAMIENTAS ---
elif seccion == "Herramientas":  
    st.markdown('<div class="main-header">Herramientas de Inteligencia Artificial</div>', unsafe_allow_html=True)  
    st.markdown('<div class="sub-header">Accede a las principales plataformas e instrumentos de IA.</div>', unsafe_allow_html=True)  

    col1, col2 = st.columns([1, 1])  

    with col1:  
        st.markdown('''  
        <div class="card">  
            <span class="category-tag">Asistente IA</span>  
            <div class="term-title">Google Gemini</div>  
            <div class="term-desc">  
                Modelo conversacional multimodal desarrollado por Google, capaz de comprender texto, código, imágenes, audio y video.  
            </div>  
            <a href="https://gemini.google.com/app?hl=es-MX" target="_blank" class="link-button">  
                🚀 Abrir Google Gemini  
            </a>  
        </div>  
        ''', unsafe_allow_html=True)  

# --- SECCIÓN: ENSAYO (CENTRADO Y FLEXIBLE) ---
elif seccion == "Ensayo":  
    st.markdown('<div class="main-header">Documentos y Ensayos</div>', unsafe_allow_html=True)  
    st.markdown('<div class="sub-header">Selecciona un archivo para leerlo cómodamente en pantalla.</div>', unsafe_allow_html=True)  

    ensayos_disponibles = {
        "📄 Ensayo de IA (Subproducto No. 5)": "documentos/Actividad_Desarrollo_Subproducto_No_5_Ensayo.pdf"
    }

    col_seleccion, col_vacio = st.columns([2, 1])
    with col_seleccion:
        documento_seleccionado = st.selectbox(
            "📁 Selecciona el documento que deseas consultar:",
            options=list(ensayos_disponibles.keys())
        )

    st.markdown("---")

    ruta_archivo = ensayos_disponibles[documento_seleccionado]
    mostrar_pdf_integrado(ruta_archivo)

# --- SECCIÓN: GLOSARIO ---
elif seccion == "Glosario":  
    st.markdown('<div class="main-header">Directorio de Tecnologías e Inteligencia Artificial</div>', unsafe_allow_html=True)  
    st.markdown('<div class="sub-header">Plataforma de consulta para términos clave de arquitectura, IA y ciencia de datos.</div>', unsafe_allow_html=True)  

    col_busqueda, col_categoria = st.columns([2, 1])  

    with col_busqueda:  
        busqueda = st.text_input("🔍 Buscar término...", "", placeholder="Escribe un concepto o palabra clave...")  

    with col_categoria:  
        categorias = ["Todas"] + sorted(list(set(info["categoria"] for info in GLOSARIO.values())))  
        categoria_sel = st.selectbox("📁 Categoría", categorias)  

    st.markdown("---")  

    terminos_filtrados = {  
        term: info for term, info in GLOSARIO.items()  
        if (busqueda.lower() in term.lower() or busqueda.lower() in info["descripcion"].lower())  
        and (categoria_sel == "Todas" or info["categoria"] == categoria_sel)  
    }  

    col_lista, col_detalle = st.columns([1, 2])  

    with col_lista:  
        st.subheader("Términos disponibles")  
        if terminos_filtrados:  
            seleccion = st.radio(  
                label="Selecciona un concepto:",  
                options=list(terminos_filtrados.keys()),  
                label_visibility="collapsed"  
            )  
        else:  
            st.info("No se encontraron términos coincidentes.")  
            seleccion = None  

    with col_detalle:
        if seleccion:
            item = GLOSARIO[seleccion]
            
            ejemplo_html = ""
            if "ejemplo" in item:
                texto_ejemplo = item["ejemplo"].replace("\n", "<br>")
                ejemplo_html = f'<div style="margin-top:15px; padding-top:15px; border-top:1px solid #E2E8F0;"><strong style="color:#0F172A;">Ejemplo práctico:</strong><p style="color:#475569; font-size:0.95rem; margin-top:8px;">{texto_ejemplo}</p></div>'

            card_html = f'<div class="card"><span class="category-tag">{item["categoria"]}</span><div class="term-title">{seleccion}</div><div class="term-desc">{item["descripcion"]}</div>{ejemplo_html}</div>'
            
            st.markdown(card_html, unsafe_allow_html=True)
