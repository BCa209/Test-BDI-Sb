import csv
import streamlit as st
import datetime
from modules.admin_methods import *
from modules.api_methods import *

def pagina_inicio():
    st.title("¡Bienvenido al Sistema de Encuesta Personal!")
    st.divider()
    st.write("Seleccione una opción del menú para comenzar a llenar la encuesta.")
    st.image("assets/image.png", caption="Complete su encuesta", use_container_width=True)
    
    if st.button("  Continuar ->  ", use_container_width=True):
        st.session_state.pagina_actual = 'informacion_personal'
        st.rerun()
    
    elif st.button("LogIn"):
        st.session_state.pagina_actual = 'autenticacion'  # Cambiar el estado a 'autenticacion'
        st.rerun()  # Recargar la página para mostrar la pantalla de login

def informacion_personal():
    st.subheader("Información Personal")
    st.divider()

    # Cargar respuestas guardadas si existen
    respuestas_guardadas = st.session_state.respuestas_guardadas.get('informacion_personal', {})

    # Campos de texto
    nombres = st.text_input("Nombres", value=respuestas_guardadas.get("nombres", ""))
    apodo = st.text_input("Apodo", value=respuestas_guardadas.get("apodo", ""))
    apellidos = st.text_input("Apellidos", value=respuestas_guardadas.get("apellidos", ""))
    edad = st.text_input("Edad", value=respuestas_guardadas.get("edad", ""))

    # Selección de género con opción para escribir directamente
    genero_opciones = ["Masculino", "Femenino"]
    genero = st.radio(
        "Género",
        options=genero_opciones + ["Especificar otro"],
        index=(genero_opciones + ["Especificar otro"]).index(
            respuestas_guardadas.get("genero", "Masculino")
        ) if respuestas_guardadas.get("genero", "Masculino") in genero_opciones
        else len(genero_opciones)  # Índice para "Especificar otro"
    )

    if genero == "Especificar otro":
        genero = st.text_input("Especifica tu género", value=respuestas_guardadas.get("genero", ""))

    # Fecha de nacimiento
    fecha_nacimiento = st.date_input(
        "Fecha de Nacimiento",
        value=respuestas_guardadas.get("fecha_nacimiento", None)
    )

    # Botón para guardar la información
    if st.button("Guardar"):
        if nombres and apodo and apellidos and edad and genero and fecha_nacimiento:
            try:
                # Formatear los datos según el JSON requerido
                datos = {
                    "data": [
                        {
                            "nombres": nombres,
                            "apodo": apodo,
                            "apellidos": apellidos,
                            "edad": int(edad),  # Convertir edad a entero
                            "genero": genero,
                            "fecha_nacimiento": str(fecha_nacimiento)
                        }
                    ]
                }

                # Enviar los datos al endpoint de la API
                respuesta = enviar_info_personal(datos)

                if "error" in respuesta:
                    st.error(f"Error al enviar los datos: {respuesta['error']}")
                else:
                    st.success("Información Personal Guardada y Enviada a la API")

                    # Guardar las respuestas en el estado de la sesión
                    st.session_state.respuestas_guardadas['informacion_personal'] = datos["data"][0]

                    # Cambiar a la siguiente página
                    st.session_state.pagina_actual = 'contacto'
                    st.rerun()
            except ValueError as e:
                st.error(f"Error al guardar los datos: {str(e)}")
        else:
            st.error("Por favor, complete todos los campos.")

def contacto(): 
    st.subheader("Información de Contacto")
    st.divider()
    
    # Obtén los datos guardados del estado de sesión
    respuestas_guardadas = st.session_state.respuestas_guardadas.get('contacto', {})
    
    # Campos de entrada
    telefono = st.text_input("Teléfono", value=respuestas_guardadas.get("telefono", ""))
    correo = st.text_input("Correo Electrónico", value=respuestas_guardadas.get("correo", ""))
    
    # Multiselección para redes sociales
    redes_sociales = st.multiselect(
        "Redes Sociales",
        options=["Facebook", "Twitter", "Instagram", "WhatsApp", "TikTok", "Otras"],  # Opciones posibles
        default=respuestas_guardadas.get("redes_sociales", [])  # Valor predeterminado como lista
    )
    
    direccion = st.text_input("Dirección", value=respuestas_guardadas.get("direccion", ""))
    distrito = st.text_input("Distrito", value=respuestas_guardadas.get("distrito", ""))
    provincia = st.text_input("Provincia", value=respuestas_guardadas.get("provincia", ""))
    departamento = st.text_input("Departamento", value=respuestas_guardadas.get("departamento", ""))
    
    # Botón para guardar y enviar los datos
    if st.button("Guardar y Enviar"):
        # Validación de los campos
        if telefono and correo and redes_sociales and direccion and distrito and provincia and departamento:
            try:
                # Construir el JSON en el formato esperado por la API
                datos_contacto = {
                    "data": [
                        {
                            "telefono": telefono,
                            "correo_electronico": correo,
                            "redes_sociales": ",".join(redes_sociales),  # Convertir la lista en una cadena separada por comas
                            "direccion": direccion,
                            "distrito": distrito,
                            "provincia": provincia,
                            "departamento": departamento
                        }
                    ]
                }

                # Enviar los datos a la API
                respuesta_api = enviar_contacto(datos_contacto)

                if "error" in respuesta_api:
                    st.error(f"Error al enviar datos a la API: {respuesta_api['error']}")
                else:
                    st.success("Información de Contacto enviada correctamente")

                    # Guardar en el estado de sesión
                    st.session_state.respuestas_guardadas['contacto'] = {
                        "telefono": telefono,
                        "correo": correo,
                        "redes_sociales": redes_sociales,
                        "direccion": direccion,
                        "distrito": distrito,
                        "provincia": provincia,
                        "departamento": departamento
                    }

                    # Navegar a la siguiente página
                    st.session_state.pagina_actual = 'nivel_socioeconomico'
                    st.rerun()  # Recargar para mostrar la siguiente página
            except ValueError as e:
                st.error(f"Error inesperado: {str(e)}")
        else:
            st.error("Por favor, complete todos los campos.")

def nivel_socioeconomico():
    st.subheader("Nivel Socioeconómico")
    st.divider()

    # Recuperar respuestas previas
    respuestas_guardadas = st.session_state.respuestas_guardadas.get('nivel_socioeconomico', {})

    # Pregunta si actualmente estudia
    actualmente_estudia = st.radio(
        "¿Actualmente estudias?",
        ["No", "Sí"],
        index=["Sí", "No"].index(respuestas_guardadas.get("actualmente_estudia", "Sí"))
    )

    # Si responde "Sí", mostrar opciones relacionadas con nivel educativo
    if actualmente_estudia == "Sí":
        nivel_educativo = st.selectbox(
            "Nivel Educativo",
            ["Primaria", "Secundaria", "Técnico", "Universitario", "Otro"],
            index=["Primaria", "Secundaria", "Técnico", "Universitario", "Otro"].index(respuestas_guardadas.get("nivel_educativo", "Universitario"))
        )

        # Si selecciona "Universitario", mostrar campos adicionales
        if nivel_educativo == "Universitario":
            escuela_profesional = st.text_input(
                "Escuela Profesional",
                value=respuestas_guardadas.get("escuela_profesional", "")
            )
            semestre_academico = st.number_input(
                "Semestre Académico",
                value=respuestas_guardadas.get("semestre_academico", 1),
                min_value=1,
                step=1
            )
        else:
            escuela_profesional = None
            semestre_academico = None
    else:
        nivel_educativo = None
        escuela_profesional = None
        semestre_academico = None

    # Información laboral
    st.subheader("Información Laboral")
    actualmente_empleado = st.radio(
        "¿Actualmente empleado?",
        ["Sí", "No"],
        index=["Sí", "No"].index(respuestas_guardadas.get("actualmente_empleado", "No"))
    )

    # Si responde "Sí", mostrar campos relacionados con empleo
    if actualmente_empleado == "Sí":
        tipo_empleo = st.radio(
            "Tipo de empleo",
            ["Completo", "Parcial"],
            index=["Completo", "Parcial"].index(respuestas_guardadas.get("tipo_empleo", "Completo"))
        )
        ingreso_mensual = st.number_input(
            "Ingreso Mensual",
            value=respuestas_guardadas.get("ingreso_mensual", 0),
            min_value=0,
            step=100
        )
    else:
        tipo_empleo = None
        ingreso_mensual = None

    # Botón para guardar datos
    if st.button("Guardar y Enviar Nivel Socioeconómico"):
        # Validación básica
        if (
            actualmente_estudia == "No" or 
            (nivel_educativo and 
            (nivel_educativo != "Universitario" or (escuela_profesional and semestre_academico)))
        ) and (
            actualmente_empleado == "No" or (tipo_empleo and ingreso_mensual is not None)
        ):
            # Preparar datos en formato JSON
            datos = {
                "data": [
                    {
                        "actualmente_estudiando": actualmente_estudia,
                        "nivel_educativo": nivel_educativo,
                        "escuela_profesional": escuela_profesional,
                        "semestre_academico": semestre_academico if semestre_academico else None,
                        "empleado": actualmente_empleado,
                        "tipo_empleo": tipo_empleo,
                        "ingresos": ingreso_mensual if ingreso_mensual else None
                    }
                ]
            }

            # Enviar los datos al endpoint
            respuesta = enviar_socio_economico(datos)

            if "error" in respuesta:
                st.error(f"Error al enviar los datos: {respuesta['error']}")
            else:
                # Guardar en session_state
                st.session_state.respuestas_guardadas['nivel_socioeconomico'] = {
                    "actualmente_estudia": actualmente_estudia,
                    "nivel_educativo": nivel_educativo,
                    "escuela_profesional": escuela_profesional,
                    "semestre_academico": semestre_academico,
                    "actualmente_empleado": actualmente_empleado,
                    "tipo_empleo": tipo_empleo,
                    "ingreso_mensual": ingreso_mensual,
                }
                st.success("Nivel Socioeconómico enviado correctamente")
                st.session_state.pagina_actual = 'situacion_sentimental'
                st.rerun()
        else:
            st.error("Por favor, complete todos los campos necesarios.")

def situacion_sentimental():
    st.subheader("Situación Sentimental")
    st.divider()

    # Recuperar respuestas previas
    respuestas_guardadas = st.session_state.respuestas_guardadas.get('situacion_sentimental', {})

    # Preguntar si tiene pareja
    tiene_pareja = st.radio(
        "¿Tienes pareja?", 
        ["Sí", "No"], 
        index=["Sí", "No"].index(respuestas_guardadas.get("tiene_pareja", "No"))
    )

    # Cambiar a radio para estado civil con las opciones Soltero, Casado, Divorciado
    estado_civil = st.radio(
        "Estado Civil", 
        ["Soltero", "Casado", "Divorciado"], 
        index=["Soltero", "Casado", "Divorciado"].index(respuestas_guardadas.get("estado_civil", "Soltero"))
    )

    # Preguntar si tiene hijos
    tiene_hijos = st.radio(
        "¿Tienes hijos?", 
        ["Sí", "No"], 
        index=["Sí", "No"].index(respuestas_guardadas.get("tiene_hijos", "No"))
    )

    # Botón para guardar la información
    if st.button("Guardar Situación Sentimental"):
        # Validación de que los campos no estén vacíos
        if tiene_pareja and estado_civil and tiene_hijos:
            try:
                # Guardar respuestas en session_state
                datos = {
                    "data": [
                        {
                            "tiene_pareja": tiene_pareja,
                            "estado_civil": estado_civil,
                            "tiene_hijos": tiene_hijos
                        }
                    ]
                }

                # Enviar los datos a la API
                from modules.api_methods import enviar_situacion_sentimental
                respuesta = enviar_situacion_sentimental(datos)

                if "error" in respuesta:
                    st.error(f"Error al enviar los datos: {respuesta['error']}")
                else:
                    # Guardar localmente si la respuesta fue exitosa
                    st.session_state.respuestas_guardadas['situacion_sentimental'] = datos["data"][0]
                    st.success("Situación Sentimental Guardada y Enviada")
                    st.session_state.pagina_actual = 'salud_y_bienestar'
                    st.rerun()

            except ValueError:
                st.error("Error al guardar los datos.")
        else:
            st.error("Por favor, complete todos los campos.")

def salud_y_bienestar(): 
    st.subheader("Salud y Bienestar")
    st.divider()
    
    # Recuperar respuestas previas
    respuestas_guardadas = st.session_state.respuestas_guardadas.get('salud_y_bienestar', {})

    # Preguntar si padece alguna enfermedad crónica
    padece_enfermedad = st.radio(
        "¿Padeces alguna enfermedad crónica?", 
        ["No", "Sí"], 
        index=["Sí", "No"].index(respuestas_guardadas.get("padece_enfermedad", "No"))
    )

    # Mostrar un campo de texto para la enfermedad si la respuesta es Sí
    if padece_enfermedad == "Sí":
        enfermedad = st.text_input("¿Cuál es la enfermedad?", value=respuestas_guardadas.get("especificacion_enfermedad", ""))
    else:
        enfermedad = ""

    # Preguntar sobre la actividad física semanal
    actividad_fisica = st.radio(
        "Actividad física semanal", 
        ["0", "1-2", "3-4", "5+"], 
        index=["0", "1-2", "3-4", "5+"].index(respuestas_guardadas.get("actividad_fisica", "0"))
    )

    # Botón para guardar la información
    if st.button("Guardar Salud y Bienestar"):
        # Validación de que los campos no estén vacíos
        if padece_enfermedad and actividad_fisica:
            try:
                # Crear el payload JSON
                datos_salud = {
                    "data": [
                        {
                            "padece_enfermedad": padece_enfermedad,
                            "especificacion_enfermedad": enfermedad,
                            "actividad_fisica": actividad_fisica
                        }
                    ]
                }

                # Enviar datos a la API
                respuesta_api = enviar_salud(datos_salud)

                # Verificar si hubo un error en la respuesta de la API
                if "error" in respuesta_api:
                    st.error(f"Error al enviar los datos: {respuesta_api['error']}")
                else:
                    # Guardar respuestas en session_state si el envío fue exitoso
                    st.session_state.respuestas_guardadas['salud_y_bienestar'] = {
                        "padece_enfermedad": padece_enfermedad,
                        "especificacion_enfermedad": enfermedad,
                        "actividad_fisica": actividad_fisica
                    }
                    st.success("Salud y Bienestar Guardada y enviada correctamente")

                    # Navegar a la siguiente página
                    st.session_state.pagina_actual = 'habitos_estilo_de_vida'
                    st.rerun()
            except ValueError:
                st.error("Error al guardar o enviar los datos.")
        else:
            st.error("Por favor, complete todos los campos.")

def habitos_estilo_de_vida():
    st.subheader("Hábitos y Estilo de Vida")
    st.divider()

    respuestas_guardadas = st.session_state.respuestas_guardadas.get('habitos_estilo_de_vida', {})

    # Pregunta sobre el consumo de tabaco
    fuma = st.radio("¿Fumas?", ["Sí", "No"], index=["Sí", "No"].index(respuestas_guardadas.get("fuma", "No")))

    # Pregunta sobre el consumo de alcohol
    toma_alcohol = st.radio("¿Tomas bebidas alcohólicas?", ["Sí", "No"], index=["Sí", "No"].index(respuestas_guardadas.get("toma_alcohol", "No")))

    # Pregunta sobre actividades recreativas
    actividades_recreativas = st.radio(
        "¿Haces actividades recreativas?", 
        ["No", "Sí"], 
        index=["Sí", "No"].index(respuestas_guardadas.get("actividades_recreativas", "No"))
    )

    # Si la respuesta a actividades recreativas es 'Sí', mostrar un campo de texto
    if actividades_recreativas == "Sí":
        actividades = st.text_input("¿Qué actividades recreativas realizas?", value=respuestas_guardadas.get("actividades", ""))
    
    # Botón para guardar los datos
    if st.button("Guardar Hábitos y Estilo de Vida"):
        # Validación de que todos los campos estén completos
        if fuma and toma_alcohol and actividades_recreativas:
            try:
                # Guardar las respuestas en session_state
                st.session_state.respuestas_guardadas['habitos_estilo_de_vida'] = {
                    "fuma": fuma,
                    "bebe_alcohol": toma_alcohol,  # Guardar "bebe_alcohol" según respuesta
                    "actividades_recreativas": actividades_recreativas,
                    "act_rec_realiza": actividades if actividades_recreativas == "Sí" else ""  # Guardar las actividades si la respuesta fue 'Sí'
                }

                # Crear el objeto JSON con los datos en el formato esperado
                datos_habitos = {
                    "data": [
                        {
                            "fuma": fuma,
                            "bebe_alcohol": toma_alcohol,
                            "actividades_recreativas": actividades_recreativas,
                            "act_rec_realiza": actividades if actividades_recreativas == "Sí" else ""
                        }
                    ]
                }

                # Enviar los datos a la API
                respuesta_api = enviar_habitos_y_estilo(datos_habitos)

                if 'error' in respuesta_api:
                    st.error(f"Error al enviar los datos: {respuesta_api['error']}")
                else:
                    st.success("Hábitos y Estilo de Vida Guardados y Enviados Exitosamente")
                    st.session_state.pagina_actual = 'opiniones_o_interes'
                    st.rerun()
            except ValueError:
                st.error("Error al guardar los datos.")
        else:
            st.error("Por favor, complete todos los campos.")

def opiniones_o_interes():
    st.subheader("Opiniones e Intereses")
    st.divider()

    # Recuperar las respuestas guardadas previamente
    respuestas_guardadas = st.session_state.respuestas_guardadas.get('opiniones_o_interes', {})
    
    # Inputs de texto para las opiniones
    mayor_logro = st.text_input("¿Cuál considera que es su mayor logro personal?", value=respuestas_guardadas.get("mayor_logro", ""))
    cambios_deseados = st.text_input("¿Qué cambios le gustaría ver en su entorno?", value=respuestas_guardadas.get("cambios_deseados", ""))

    # Botón para guardar y enviar las respuestas
    if st.button("Guardar Opiniones e Intereses"):
        if mayor_logro and cambios_deseados:
            try:
                # Guardar las respuestas en session_state
                st.session_state.respuestas_guardadas['opiniones_o_interes'] = {
                    "mayor_logro": mayor_logro,
                    "cambios_deseados": cambios_deseados
                }
                
                # Enviar los datos a la API
                datos = {
                    "data": [
                        {
                            "mayor_logro_personal": mayor_logro,
                            "cambios_deseados": cambios_deseados
                        }
                    ]
                }
                
                respuesta_api = enviar_opiniones_intereses(datos)

                # Verificar la respuesta de la API
                if "error" in respuesta_api:
                    st.error(f"Error al enviar los datos: {respuesta_api['error']}")
                else:
                    st.success("Opiniones e Intereses Guardados y Enviados Correctamente")
                
                # Cambiar a la siguiente página
                st.session_state.pagina_actual = 'consentimientos_y_comentarios'
                st.rerun()

            except ValueError:
                st.error("Error al guardar los datos.")
        else:
            st.error("Por favor, complete todos los campos.")

def consentimientos_y_comentarios():
    st.subheader("Consentimientos y Comentarios")
    st.divider()

    # Recuperar las respuestas guardadas en la sesión
    respuestas_guardadas = st.session_state.respuestas_guardadas.get('consentimientos_y_comentarios', {})
    
    # Campos del formulario
    consentimiento = st.radio(
        "¿Está de acuerdo en que los datos proporcionados sean utilizados únicamente para fines de este estudio?", 
        ["Sí", "No"], 
        index=["Sí", "No"].index(respuestas_guardadas.get("consentimiento", "Sí"))
    )
    
    comentario_adicional = st.text_input(
        "¿Desea agregar algún comentario adicional?", 
        value=respuestas_guardadas.get("comentario_adicional", "")
    )

    # Botón para guardar las respuestas
    if st.button("Guardar Consentimientos y Comentarios"):
        if consentimiento and comentario_adicional:
            try:
                # Guardar respuestas en la sesión
                st.session_state.respuestas_guardadas['consentimientos_y_comentarios'] = {
                    "consentimiento": consentimiento,
                    "comentario_adicional": comentario_adicional
                }
                st.success("Consentimientos y Comentarios Guardados")
            except ValueError:
                st.error("Error al guardar los datos.")
        else:
            st.error("Por favor, complete todos los campos.")
    
    # Botón para enviar las respuestas a la API
    if st.button("Enviar Respuestas"):
        if consentimiento and comentario_adicional:
            # Preparar los datos en el formato esperado por la API
            data = {
                "data": [
                    {
                        "consentimiento": consentimiento,  # Valor del consentimiento
                        "comentario_adicional": comentario_adicional  # Comentario adicional
                    }
                ]
            }
            
            # Enviar los datos a la API usando la función 'enviar_consentimientos_comentarios'
            respuesta_api = enviar_consentimientos_comentarios(data)
            
            # Verificar la respuesta de la API
            if "error" in respuesta_api:
                st.error(f"Error al enviar los datos: {respuesta_api['error']}")
            else:
                st.success("Datos enviados correctamente a la API.")
        
        # Cambiar de página para mostrar mensaje de éxito
        st.session_state.pagina_actual = 'enviar_respuestas'
        st.rerun()

def enviar_respuestas():
    """
    Construye el JSON y envía las respuestas a la API Laravel.
    """
    respuestas = {
        "info_personal": {
            "nombres": st.session_state.respuestas_guardadas.get("nombres"),
            "apellidos": st.session_state.respuestas_guardadas.get("apellidos"),
            "genero": st.session_state.respuestas_guardadas.get("genero"),
            "fecha_nacimiento": st.session_state.respuestas_guardadas.get("fecha_nacimiento"),
        },
        "contacto": {
            "telefono": st.session_state.respuestas_guardadas.get("telefono"),
            "correo_electronico": st.session_state.respuestas_guardadas.get("correo"),
        },
        "socioeconomico": {
            "actualmente_estudiando": st.session_state.respuestas_guardadas.get("actualmente_estudiando"),
        },
        "salud": {
            "padece_enfermedad": st.session_state.respuestas_guardadas.get("padece_enfermedad"),
        },
        "situacion_sentimental": {
            "tiene_pareja": st.session_state.respuestas_guardadas.get("tiene_pareja"),
        },
        "habitos": {
            "fuma": st.session_state.respuestas_guardadas.get("fuma"),
        },
        "opiniones": {
            "mayor_logro_personal": st.session_state.respuestas_guardadas.get("mayor_logro_personal"),
        },
        "consentimiento": {
            "consentimiento": st.session_state.respuestas_guardadas.get("consentimiento"),
        },
    }


    respuesta_api = enviar_datos(API_ENCUESTA_URL, respuestas)
    if "error" in respuesta_api:
        st.error(f"Error al enviar las respuestas: {respuesta_api['error']}")
    else:
        st.success("¡Respuestas enviadas exitosamente!")
        st.session_state.respuestas_guardadas = {}

    st.session_state.encuesta_completada = True

    return 0
