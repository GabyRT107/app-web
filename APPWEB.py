import streamlit as st  
from streamlit_carousel import carousel  
  
# Configuración de página profesional  
st.set_page_config(  
    page_title="Plataforma de Inteligencia Artificial & Data",  
    page_icon="💻",  
    layout="wide",  
    initial_sidebar_state="expanded"  
)  
  
# Estilo CSS personalizado para apariencia moderna y pulida  
st.markdown("""  
 <style>  
 /* Estilos generales */  
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
   
/* ACCENT-COLOR PARA EL PUNTO DEL RADIO BUTTON (#231EB3) */  
 div[data-testid="stRadioButton"] input[type="radio"] {  
 accent-color: #231EB3 !important;  
 }  
   
/* CAMBIAR EL COLOR DEL TEXTO SELECCIONADO Y PUNTOS EN NAVEGADORES QUE RENDERIZAN DIVS */  
 div[data-testid="stRadioButton"] div[role="radiogroup"] label[aria-checked="true"] {  
 color: #231EB3 !important;  
 }  
   
div[data-testid="stRadioButton"] div[role="radiogroup"] label[aria-checked="true"] > div:first-child {  
 border-color: #231EB3 !important;  
 background-color: #231EB3 !important;  
 }  
  
 div[data-testid="stRadioButton"] div[role="radiogroup"] label[aria-checked="true"] svg {  
 fill: #231EB3 !important;  
 }  
  
 /* Tarjetas modernas */  
 .card {  
 background-color: #F8FAFC;  
 border: 1px solid #E2E8F0;  
 border-radius: 16px;  
 padding: 28px;  
 margin-top: 10px;  
 box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05), 0 4px 6px -2px rgba(0, 0, 0, 0.025);  
 transition: transform 0.2s ease, box-shadow 0.2s ease;  
 }  
 .card:hover {  
 transform: translateY(-2px);  
 box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.08), 0 10px 10px -5px rgba(0, 0, 0, 0.03);  
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
  
 /* Botón personalizado para enlaces externos */  
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
 transition: background-color 0.2s ease, transform 0.2s ease;  
 }  
 .link-button:hover {  
 background-color: #1A168C;  
 transform: translateY(-1px);  
 text-decoration: none;  
 }  
  
 /* ESTILO MODERNO Y CONTROL DE TAMAÑO PARA IMÁGENES */  
 stImage > img, div[data-testid="stImage"] img {  
 display: block;  
 margin-left: auto;  
 margin-right: auto;  
 max-width: 480px;  
 width: 100%;  
 border-radius: 14px;  
 box-shadow: 0 10px 20px -5px rgba(0, 0, 0, 0.1);  
 transition: transform 0.3s ease, box-shadow 0.3s ease;  
 }  
   
div[data-testid="stImage"] img:hover {  
 transform: scale(1.02);  
 box-shadow: 0 15px 30px -5px rgba(0, 0, 0, 0.15);  
 }  
  
 /* Mejora visual en Pestañas (Tabs) */  
 .stTabs [data-baseweb="tab-list"] {  
 gap: 8px;  
 }  
 .stTabs [data-baseweb="tab"] {  
 border-radius: 8px;  
 padding: 8px 16px;  
 }  
   
/* Estilización moderna de inputs y selectores */  
 div[data-baseweb="input"] > div, div[data-baseweb="select"] > div {  
 border-radius: 10px !important;  
 border-color: #E2E8F0 !important;  
 }  
 </style>  
""", unsafe_allow_html=True)  
  
# Base de datos de conceptos estructurada  
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
        "descripcion": "Subcampo de la IA que permite a los sistemas aprender y mejorar automáticamente a partir de la experiencia y los datos, sin ser programados explícitamente."  
    },  
    "Big Data": {  
        "categoria": "Datos e Infraestructura",  
        "descripcion": "Conjunto de datos masivos y complejos que superan las capacidades del software tradicional para su procesamiento, caracterizados por su volumen, velocidad y variedad."  
    },  
    "Sistemas adaptativos de autoaprendizaje": {  
        "categoria": "Sistemas Inteligentes",  
        "descripcion": "Sistemas diseñados para modificar automáticamente sus algoritmos o comportamientos en tiempo real según los cambios en su entorno o entradas."  
    },  
    "Aprendizaje profundo": {  
        "categoria": "Fundamentos de IA",  
        "descripcion": "Subconjunto del Aprendizaje Automático basado en redes neuronales artificiales de múltiples capas que imitan la estructura del cerebro humano."  
    },  
    "Procesamiento de lenguaje natural (PLN)": {  
        "categoria": "Aplicaciones de IA",  
        "descripcion": "Disciplina que permite a las computadoras comprender, interpretar, manipular y generar lenguaje humano hablado o escrito."  
    },  
    "Disciplina Tecnológica": {  
        "categoria": "Fundamentos",  
        "descripcion": "Campo metódico de estudio e ingeniería dedicado al desarrollo, aplicación y gestión responsable de soluciones tecnológicas."  
    },  
    "Ciencia de Datos": {  
        "categoria": "Datos e Infraestructura",  
        "descripcion": "Campo interdisciplinario que combina estadística, matemáticas y programación para extraer conocimientos significativos a partir de datos estructurados y no estructurados."  
    },  
    "Máquina Virtual": {  
        "categoria": "Datos e Infraestructura",  
        "descripcion": "Entorno informático de software que emula un sistema físico completo, permitiendo ejecutar sistemas operativos y aplicaciones de forma aislada."  
    },  
    "Sistema de Expertos": {  
        "categoria": "Inteligencia Artificial",  
        "descripcion": "Sistema informático que emula la capacidad de toma de decisiones de un experto humano en un dominio específico utilizando reglas de conocimiento."  
    },  
    "Internet de las cosas (IoT)": {  
        "categoria": "Hardware & Redes",  
        "descripcion": "Red de objetos físicos interconectados provistos de sensores y software que recopilan y comparten datos a través de Internet."  
    },  
    "Tecnología operativa (OT)": {  
        "categoria": "Hardware & Redes",  
        "descripcion": "Hardware y software utilizado para monitorear y controlar dispositivos físicos, procesos e infraestructura en entornos industriales."  
    },  
    "Visión Artificial": {  
        "categoria": "Aplicaciones de IA",  
        "descripcion": "Campo de la IA que entrena a las computadoras para interpretar, procesar y comprender el mundo visual a través de imágenes y video."  
    },  
    "Computación Cognitiva": {  
        "categoria": "Sistemas Inteligentes",  
        "descripcion": "Uso de modelos computadorizados para simular el proceso de pensamiento humano en situaciones complejas e ambiguas."  
    },  
    "Ingeniería de Prompts": {  
        "categoria": "IA Generativa",  
        "descripcion": "Práctica de estructurar, refinar y optimizar las instrucciones de texto de entrada para obtener las mejores respuestas de modelos de IA."  
    },  
    "Modelos de lenguajes grandes (LLM)": {  
        "categoria": "IA Generativa",  
        "descripcion": "Modelos de aprendizaje profundo entrenados con enormes cantidades de texto para comprender, resumir y generar contenido en lenguaje natural."  
    },  
    "Redes Neuronales Convolucionales (CNN)": {  
        "categoria": "Aprendizaje Profundo",  
        "descripcion": "Arquitectura de red neuronal diseñada principalmente para procesar datos con estructura de cuadrícula, como imágenes y video."  
    },  
    "IA Multimodal": {  
        "categoria": "IA Avanzada",  
        "descripcion": "Sistemas de IA capaces de procesar, comprender y combinar múltiples tipos de datos de entrada (texto, imágenes, audio, video) simultáneamente."  
    },  
    "IA Responsable": {  
        "categoria": "Gobernanza & Ética",  
        "descripcion": "Enfoque metódico para el diseño, desarrollo y despliegue de sistemas de IA seguros, transparentes, éticos y libres de sesgos."  
    }  
}  
  
# Función auxiliar para centrar imágenes con layout de columnas  
def mostrar_imagen_centrada(ruta):  
    col1, col2, col3 = st.columns([1, 2, 1])  
    with col2:  
        st.image(ruta)  
  
# --- NAVEGACIÓN Y MENÚ PRINCIPAL ---  
st.sidebar.title("Navegación")  
seccion = st.sidebar.radio(  
    "Selecciona una sección:",  
    ["Inteligencia Artificial", "Antecedentes", "Clasificación Clásica", "Disciplinas", "Herramientas", "Glosario"]  
)  
  
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
            "**IA débil o estrecha (Narrow AI):** Está diseñada para resolver tareas específicas: traducción, recomendación, reconocimiento de imágenes, reconocimiento de voz, generación de texto, recomendaciones de productos. Impulsa la mayor parte de la IA que nos rodea hoy, no tiene nada de débil."  
        )  
        mostrar_imagen_centrada("img/4.png")  
   
    with tab02:  
        st.write(  
            "**IA fuerte o general (AGI- General Artificial Intelligence):** Busca crear máquinas con inteligencia humana completa, capaces de realizar cualquier tarea intelectual que un humano pueda hacer. Es teórica y no existe de manera práctica. Es una categoría hipotética."  
        )  
        mostrar_imagen_centrada("img/5.png")  
   
    with tab03:  
        st.write(  
            "**IA superinteligente:** Hace referencia a un sistema que superaría a los humanos en absolutamente todas las áreas cognitivas, sería autoconsciente y tendría la capacidad de resolver problemas, aprender y planificar para el futuro. Es una categoría especulativa."  
        )  
        mostrar_imagen_centrada("img/6.png")  
  
# --- SECCIÓN: DISCIPLINAS ---  
elif seccion == "Disciplinas":  
    st.markdown('<div class="main-header">Disciplinas Relacionadas</div>', unsafe_allow_html=True)  
    st.markdown('<div class="sub-header">Áreas de estudio que convergen en el ecosistema de IA y Datos.</div>', unsafe_allow_html=True)  
  
    pestanas = [  
        "Filosofía",  
        "Matemáticas",  
        "Psicología",  
        "Computación",  
        "Lingüística",  
        "Economía",  
        "Neurociencia",  
    ]  
    t1, t2, t3, t4, t5, t6, t7 = st.tabs(pestanas)  
  
    with t1:  
        st.write(  
            "**Filosofía:** Aristóteles (300 AC) Describe de forma"  
            " estructurada la forma como el ser humano produce conclusiones"  
            " racionales a partir de un grupo de premisas. (Silogismos)"  
        )  
        mostrar_imagen_centrada("img/Filosofia.jpg")  
  
    with t2:  
        st.write(  
            "**Matemáticas:** Razonamiento con algoritmos. Cálculo: brindó las"  
            " herramientas que nos permiten la modelación de diferentes tipos"  
            " de fenómenos."  
        )  
        mostrar_imagen_centrada("img/Matematicas.jpg")  
  
    with t3:  
        st.write(  
            "**Psicología:** Refuerza la idea de que los humanos y otros"  
            " animales pueden ser considerados como máquinas para el"  
            " procesamiento de información."  
        )  
        mostrar_imagen_centrada("img/Psicologia.jpg")  
  
    with t4:  
        st.write(  
            "**Computación:** Las teorías de la IA encuentran un medio para su"  
            " implementación de artefactos y modelado cognitivo."  
        )  
        mostrar_imagen_centrada("img/Computacion.jpg")  
  
    with t5:  
        st.write(  
            "**Lingüística:** Aporta un área híbrida conocida como lingüística"  
            " computacional o procesamiento del lenguaje natural."  
        )  
        mostrar_imagen_centrada("img/Linguistica.jpg")  
  
    with t6:  
        st.write(  
            "**Economía:** Área experta en la toma de decisiones (Teoría de la"  
            " decisión, Juegos, Procesos de decisión de Markov)."  
        )  
        mostrar_imagen_centrada("img/Economia.jpeg")  
  
    with t7:  
        st.write(  
            "**Neurociencia:** Ha contribuido a la IA con los conocimientos sobre"  
            " la forma como el cerebro procesa la información."  
        )  
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
                Google Gemini es un modelo conversacional multimodal desarrollado por Google, capaz de comprender y procesar texto, código, imágenes, audio y video.  
            </div>  
            <a href="https://gemini.google.com/app?hl=es-MX" target="_blank" class="link-button">  
                🚀 Abrir Google Gemini  
            </a>  
        </div>  
        ''', unsafe_allow_html=True)  
  
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
            st.markdown(f'''  
            <div class="card">  
                <span class="category-tag">{item["categoria"]}</span>  
                <div class="term-title">{seleccion}</div>  
                <div class="term-desc">{item["descripcion"]}</div>  
            </div>  
            ''', unsafe_allow_html=True)