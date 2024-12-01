import streamlit as st
from modules.encuesta_methods import * 
from modules.admin_methods import *

# Configuración de la página
st.set_page_config(
    page_title="Encuesta Personal", 
    page_icon="📋"
)

# Inicialización de variables en session_state si no están definidas
if 'pagina_actual' not in st.session_state:
    st.session_state.pagina_actual = 'inicio'

if 'respuestas_guardadas' not in st.session_state:
    st.session_state.respuestas_guardadas = {}

# Función que coloca los botones en la barra lateral
def buttons():
    with st.sidebar:
        if st.button("Información Personal"):
            st.session_state.pagina_actual = 'informacion_personal'
        if st.button("Información de Contacto"):
            st.session_state.pagina_actual = 'contacto'
        if st.button("Nivel Socioeconómico"):
            st.session_state.pagina_actual = 'nivel_socioeconomico'
        if st.button("Situación Sentimental"):
            st.session_state.pagina_actual = 'situacion_sentimental'
        if st.button("Salud y Bienestar"):
            st.session_state.pagina_actual = 'salud_y_bienestar'
        if st.button("Hábitos y Estilo de Vida"):
            st.session_state.pagina_actual = 'habitos_estilo_de_vida'
        if st.button("Opiniones o Intereses"):
            st.session_state.pagina_actual = 'opiniones_o_interes'
        if st.button("Consentimientos y Comentarios"):
            st.session_state.pagina_actual = 'consentimientos_y_comentarios'

def contenido():
    if st.session_state.pagina_actual == 'inicio':
        pagina_inicio()
    elif st.session_state.pagina_actual == 'autenticacion':
        autenticar_admin()
    elif st.session_state.pagina_actual == 'descargar_csv':
        pagina_descarga()
    elif st.session_state.pagina_actual == 'informacion_personal':
        informacion_personal()
    elif st.session_state.pagina_actual == 'contacto':
        contacto()
    elif st.session_state.pagina_actual == 'nivel_socioeconomico':
        nivel_socioeconomico()
    elif st.session_state.pagina_actual == 'situacion_sentimental':
        situacion_sentimental()
    elif st.session_state.pagina_actual == 'salud_y_bienestar':
        salud_y_bienestar()
    elif st.session_state.pagina_actual == 'habitos_estilo_de_vida':
        habitos_estilo_de_vida()
    elif st.session_state.pagina_actual == 'opiniones_o_interes':
        opiniones_o_interes()
    elif st.session_state.pagina_actual == 'consentimientos_y_comentarios':
        consentimientos_y_comentarios()
    elif st.session_state.pagina_actual == 'enviar_respuestas':
        archivo = enviar_respuestas()
        st.write("### ¡Gracias por completar la encuesta!")
        st.write("Sus respuestas han sido enviadas correctamente.")
        st.write("### ¡Gracias por completar la encuesta!")

# Mostrar los botones en la barra lateral y el contenido en la sección principal
buttons()
contenido()
