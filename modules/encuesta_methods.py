import csv
import streamlit as st
from modules.admin_methods import *

def informacion_personal():
    st.subheader("Información Personal")
    
    respuestas_guardadas = st.session_state.respuestas_guardadas.get('informacion_personal', {})
    
    nombres = st.text_input("Nombres", value=respuestas_guardadas.get("nombres", ""))
    apodo = st.text_input("Apodo", value=respuestas_guardadas.get("apodo", ""))
    apellido = st.text_input("Apellidos", value=respuestas_guardadas.get("apellido", ""))
    edad = st.text_input("Edad", value=respuestas_guardadas.get("edad", ""))
    genero = st.text_input("Género", value=respuestas_guardadas.get("genero", ""))
    fecha_nacimiento = st.text_input("Fecha de Nacimiento", value=respuestas_guardadas.get("fecha_nacimiento", ""))
    
    if st.button("Guardar"):
        if nombres and apodo and apellido and edad and genero and fecha_nacimiento:
            try:
                st.session_state.respuestas_guardadas['informacion_personal'] = {
                    "nombres": nombres,
                    "apodo": apodo,
                    "apellido": apellido,
                    "edad": edad,
                    "genero": genero,
                    "fecha_nacimiento": fecha_nacimiento
                }
                st.success("Información Personal Guardada")
                
                st.session_state.pagina_actual = 'contacto'
                st.rerun() 
            except ValueError:
                st.error("Error al guardar los datos.")
        else:
            st.error("Por favor, complete todos los campos.")

def contacto():
    st.subheader("Información de Contacto")
    
    respuestas_guardadas = st.session_state.respuestas_guardadas.get('contacto', {})
    
    telefono = st.text_input("Teléfono", value=respuestas_guardadas.get("telefono", ""))
    correo = st.text_input("Correo Electrónico", value=respuestas_guardadas.get("correo", ""))
    redes_sociales = st.text_input("Redes Sociales", value=respuestas_guardadas.get("redes_sociales", ""))
    direccion = st.text_input("Dirección", value=respuestas_guardadas.get("direccion", ""))
    calle_numero = st.text_input("Calle y Número", value=respuestas_guardadas.get("calle_numero", ""))
    departamento = st.text_input("Departamento", value=respuestas_guardadas.get("departamento", ""))
    provincia = st.text_input("Provincia", value=respuestas_guardadas.get("provincia", ""))

    if st.button("Guardar"):
        if telefono and correo and redes_sociales and direccion and calle_numero and departamento and provincia:
            try:
                st.session_state.respuestas_guardadas['contacto'] = {
                    "telefono": telefono,
                    "correo": correo,
                    "redes_sociales": redes_sociales,
                    "direccion": direccion,
                    "calle_numero": calle_numero,
                    "departamento": departamento,
                    "provincia": provincia
                }
                st.success("Información de Contacto Guardada")
                
                st.session_state.pagina_actual = 'nivel_socioeconomico'
                st.rerun() 
            except ValueError:
                st.error("Error al guardar los datos.")
        else:
            st.error("Por favor, complete todos los campos.")

def nivel_socioeconomico():
    st.subheader("Nivel Socioeconómico")
    
    respuestas_guardadas = st.session_state.respuestas_guardadas.get('nivel_socioeconomico', {})
    
    nivel_educativo = st.text_input("Nivel Educativo", value=respuestas_guardadas.get("nivel_educativo", ""))
    max_nivel_estudios = st.text_input("Máximo nivel de estudios alcanzado", value=respuestas_guardadas.get("max_nivel_estudios", ""))
    actualmente_estudia = st.radio("¿Actualmente estudias?", ["Sí", "No"], index=["Sí", "No"].index(respuestas_guardadas.get("actualmente_estudia", "Sí")))
    semestre_academico = st.text_input("Semestre Académico", value=respuestas_guardadas.get("semestre_academico", ""))
    escuela_profesional = st.text_input("Escuela Profesional", value=respuestas_guardadas.get("escuela_profesional", ""))
    
    st.subheader("Información Laboral")
    actualmente_empleado = st.radio("¿Actualmente empleado?", ["Sí", "No"], index=["Sí", "No"].index(respuestas_guardadas.get("actualmente_empleado", "Sí")))
    tipo_empleo = st.radio("Tipo de empleo", ["Tiempo completo", "Tiempo parcial"], index=["Tiempo completo", "Tiempo parcial"].index(respuestas_guardadas.get("tipo_empleo", "Tiempo completo")))
    ingresos = st.text_input("Ingresos (mensuales/semanales)", value=respuestas_guardadas.get("ingresos", ""))

    if st.button("Guardar Nivel Socioeconómico y Laboral"):
        if nivel_educativo and max_nivel_estudios and actualmente_estudia and semestre_academico and escuela_profesional and actualmente_empleado and tipo_empleo and ingresos:
            try:
                st.session_state.respuestas_guardadas['nivel_socioeconomico'] = {
                    "nivel_educativo": nivel_educativo,
                    "max_nivel_estudios": max_nivel_estudios,
                    "actualmente_estudia": actualmente_estudia,
                    "semestre_academico": semestre_academico,
                    "escuela_profesional": escuela_profesional,
                    "actualmente_empleado": actualmente_empleado,
                    "tipo_empleo": tipo_empleo,
                    "ingresos": ingresos
                }
                st.success("Nivel Socioeconómico y Laboral Guardado")

                st.session_state.pagina_actual = 'situacion_sentimental'
                st.rerun() 
            except ValueError:
                st.error("Error al guardar los datos.")
        else:
            st.error("Por favor, complete todos los campos.")

def situacion_sentimental():
    st.subheader("Situación Sentimental")
    
    respuestas_guardadas = st.session_state.respuestas_guardadas.get('situacion_sentimental', {})
    
    tiene_pareja = st.radio("¿Tienes pareja?", ["Sí", "No"], index=["Sí", "No"].index(respuestas_guardadas.get("tiene_pareja", "No")))
    estado_civil = st.text_input("Estado Civil", value=respuestas_guardadas.get("estado_civil", ""))
    tiene_hijos = st.radio("¿Tienes hijos?", ["Sí", "No"], index=["Sí", "No"].index(respuestas_guardadas.get("tiene_hijos", "No")))

    if st.button("Guardar Situación Sentimental"):
        if tiene_pareja and estado_civil and tiene_hijos:
            try:
                st.session_state.respuestas_guardadas['situacion_sentimental'] = {
                    "tiene_pareja": tiene_pareja,
                    "estado_civil": estado_civil,
                    "tiene_hijos": tiene_hijos
                }
                st.success("Situación Sentimental Guardada")

                st.session_state.pagina_actual = 'salud_y_bienestar'
                st.rerun() 
            except ValueError:
                st.error("Error al guardar los datos.")
        else:
            st.error("Por favor, complete todos los campos.")

def salud_y_bienestar():
    st.subheader("Salud y Bienestar")
    
    respuestas_guardadas = st.session_state.respuestas_guardadas.get('salud_y_bienestar', {})
    
    padece_enfermedad = st.radio("¿Padeces alguna enfermedad crónica?", ["Sí", "No"], index=["Sí", "No"].index(respuestas_guardadas.get("padece_enfermedad", "No")))
    actividad_fisica = st.radio("Actividad física semanal", ["0", "1-2", "3-4", "5+"], index=["0", "1-2", "3-4", "5+"].index(respuestas_guardadas.get("actividad_fisica", "0")))

    if st.button("Guardar Salud y Bienestar"):
        if padece_enfermedad and actividad_fisica:
            try:
                st.session_state.respuestas_guardadas['salud_y_bienestar'] = {
                    "padece_enfermedad": padece_enfermedad,
                    "actividad_fisica": actividad_fisica
                }
                st.success("Salud y Bienestar Guardada")

                st.session_state.pagina_actual = 'habitos_estilo_de_vida'
                st.rerun() 
            except ValueError:
                st.error("Error al guardar los datos.")
        else:
            st.error("Por favor, complete todos los campos.")

def habitos_estilo_de_vida():
    st.subheader("Hábitos y Estilo de Vida")
    
    respuestas_guardadas = st.session_state.respuestas_guardadas.get('habitos_estilo_de_vida', {})
    
    fuma = st.radio("¿Fumas?", ["Sí", "No"], index=["Sí", "No"].index(respuestas_guardadas.get("fuma", "No")))
    toma_alcohol = st.radio("¿Tomas bebidas alcohólicas?", ["Sí", "No"], index=["Sí", "No"].index(respuestas_guardadas.get("toma_alcohol", "No")))
    actividades_recreativas = st.radio("¿Haces actividades recreativas?", ["Sí", "No"], index=["Sí", "No"].index(respuestas_guardadas.get("actividades_recreativas", "No")))

    if st.button("Guardar Hábitos y Estilo de Vida"):
        if fuma and toma_alcohol and actividades_recreativas:
            try:
                st.session_state.respuestas_guardadas['habitos_estilo_de_vida'] = {
                    "fuma": fuma,
                    "toma_alcohol": toma_alcohol,
                    "actividades_recreativas": actividades_recreativas
                }
                st.success("Hábitos y Estilo de Vida Guardados")

                st.session_state.pagina_actual = 'opiniones_o_interes'
                st.rerun() 
            except ValueError:
                st.error("Error al guardar los datos.")
        else:
            st.error("Por favor, complete todos los campos.")

def opiniones_o_interes():
    st.subheader("Opiniones e Intereses")
    
    respuestas_guardadas = st.session_state.respuestas_guardadas.get('opiniones_o_interes', {})
    
    mayor_logro = st.text_input("¿Cuál considera que es su mayor logro personal?", value=respuestas_guardadas.get("mayor_logro", ""))
    cambios_entorno = st.text_input("¿Qué cambios le gustaría ver en su entorno?", value=respuestas_guardadas.get("cambios_entorno", ""))

    if st.button("Guardar Opiniones e Intereses"):
        if mayor_logro and cambios_entorno:
            try:
                st.session_state.respuestas_guardadas['opiniones_o_interes'] = {
                    "mayor_logro": mayor_logro,
                    "cambios_entorno": cambios_entorno
                }
                st.success("Opiniones e Intereses Guardados")

                st.session_state.pagina_actual = 'consentimientos_y_comentarios'
                st.rerun() 
            except ValueError:
                st.error("Error al guardar los datos.")
        else:
            st.error("Por favor, complete todos los campos.")

def consentimientos_y_comentarios():
    st.subheader("Consentimientos y Comentarios")
    
    respuestas_guardadas = st.session_state.respuestas_guardadas.get('consentimientos_y_comentarios', {})
    
    consentimiento = st.radio("¿Está de acuerdo en que los datos proporcionados sean utilizados únicamente para fines de este estudio?", ["Sí", "No"], index=["Sí", "No"].index(respuestas_guardadas.get("consentimiento", "Sí")))
    comentario_adicional = st.text_input("¿Desea agregar algún comentario adicional?", value=respuestas_guardadas.get("comentario_adicional", ""))

    if st.button("Guardar Consentimientos y Comentarios"):
        if consentimiento and comentario_adicional:
            try:
                st.session_state.respuestas_guardadas['consentimientos_y_comentarios'] = {
                    "consentimiento": consentimiento,
                    "comentario_adicional": comentario_adicional
                }
                st.success("Consentimientos y Comentarios Guardados")
            except ValueError:
                st.error("Error al guardar los datos.")
        else:
            st.error("Por favor, complete todos los campos.")
    
    if st.button("Enviar Respuestas"):
        st.session_state.pagina_actual = 'enviar_respuestas'
        st.rerun() 

def enviar_respuestas():
    respuestas_guardadas = st.session_state.respuestas_guardadas

    archivo_csv = 'data/respuestas_encuesta.csv'

    with open(archivo_csv, mode='a', newline='', encoding='utf-8') as archivo:
        escritor_csv = csv.writer(archivo)
        
        if archivo.tell() == 0:
            escritor_csv.writerow([
                'Nombres', 'Apodo', 'Apellidos', 'Edad', 'Género', 'Fecha de Nacimiento',

                'Teléfono', 'Correo', 'Redes Sociales', 'Dirección', 'Calle y Número', 'Departamento', 'Provincia',

                'Nivel Educativo', 'Máximo Nivel de Estudios', 'Actualmente Estudia', 'Semestre Académico',
                'Escuela Profesional', 'Actualmente Empleado', 'Tipo Empleo', 'Ingresos',

                'Tiene Pareja', 'Estado Civil', 'Tiene Hijos',

                'Padece Enfermedad', 'Actividad Física',

                'Fuma', 'Toma Alcohol', 'Actividades Recreativas',

                'Mayor Logro', 'Cambios Entorno',

                'Consentimiento', 'Comentario Adicional'])

        escritor_csv.writerow([
            respuestas_guardadas.get('informacion_personal', {}).get('nombres', ''),
            respuestas_guardadas.get('informacion_personal', {}).get('apodo', ''),
            respuestas_guardadas.get('informacion_personal', {}).get('apellido', ''),
            respuestas_guardadas.get('informacion_personal', {}).get('edad', ''),
            respuestas_guardadas.get('informacion_personal', {}).get('genero', ''),
            respuestas_guardadas.get('informacion_personal', {}).get('fecha_nacimiento', ''),
            
            respuestas_guardadas.get('contacto', {}).get('telefono', ''),
            respuestas_guardadas.get('contacto', {}).get('correo', ''),
            respuestas_guardadas.get('contacto', {}).get('redes_sociales', ''),
            respuestas_guardadas.get('contacto', {}).get('direccion', ''),
            respuestas_guardadas.get('contacto', {}).get('calle_numero', ''),
            respuestas_guardadas.get('contacto', {}).get('departamento', ''),
            respuestas_guardadas.get('contacto', {}).get('provincia', ''),

            respuestas_guardadas.get('nivel_socioeconomico', {}).get('nivel_educativo', ''),
            respuestas_guardadas.get('nivel_socioeconomico', {}).get('max_nivel_estudios', ''),
            respuestas_guardadas.get('nivel_socioeconomico', {}).get('actualmente_estudia', ''),
            respuestas_guardadas.get('nivel_socioeconomico', {}).get('semestre_academico', ''),
            respuestas_guardadas.get('nivel_socioeconomico', {}).get('escuela_profesional', ''),
            respuestas_guardadas.get('nivel_socioeconomico', {}).get('actualmente_empleado', ''),
            respuestas_guardadas.get('nivel_socioeconomico', {}).get('tipo_empleo', ''),
            respuestas_guardadas.get('nivel_socioeconomico', {}).get('ingresos', ''),
            
            respuestas_guardadas.get('situacion_sentimental', {}).get('tiene_pareja', ''),
            respuestas_guardadas.get('situacion_sentimental', {}).get('estado_civil', ''),
            respuestas_guardadas.get('situacion_sentimental', {}).get('tiene_hijos', ''),

            respuestas_guardadas.get('salud_y_bienestar', {}).get('padece_enfermedad', ''),
            respuestas_guardadas.get('salud_y_bienestar', {}).get('actividad_fisica', ''),
            respuestas_guardadas.get('habitos_estilo_de_vida', {}).get('fuma', ''),
            respuestas_guardadas.get('habitos_estilo_de_vida', {}).get('toma_alcohol', ''),
            respuestas_guardadas.get('habitos_estilo_de_vida', {}).get('actividades_recreativas', ''),

            respuestas_guardadas.get('opiniones_o_interes', {}).get('mayor_logro', ''),
            respuestas_guardadas.get('opiniones_o_interes', {}).get('cambios_entorno', ''),

            respuestas_guardadas.get('consentimientos_y_comentarios', {}).get('consentimiento', ''),
            respuestas_guardadas.get('consentimientos_y_comentarios', {}).get('comentario_adicional', '')
        ])

    st.session_state.encuesta_completada = True

    return archivo_csv

def pagina_inicio():
    st.write("### ¡Bienvenido al Sistema de Encuesta Personal!")
    st.write("Seleccione una opción del menú para comenzar a llenar la encuesta.")
    st.image("assets/image.png", caption="Complete su encuesta", use_container_width=True)
    
    if st.button("  Continuar ->  ", use_container_width=True):
        st.session_state.pagina_actual = 'informacion_personal'
        st.rerun()
    
    elif st.button("LogIn"):
        st.session_state.pagina_actual = 'autenticacion'  # Cambiar el estado a 'autenticacion'
        st.rerun()  # Recargar la página para mostrar la pantalla de login
