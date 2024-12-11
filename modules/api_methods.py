import requests

# Base URL de la API (ajusta según la configuración de tu servidor)
BASE_API_URL = "http://10.3.23.169:8000/api"

def obtener_datos(endpoint):
    """
    Obtiene datos de un endpoint específico de la API.

    Args:
        endpoint (str): El endpoint al cual realizar la solicitud.
                        Ejemplo: "info-personal"
    
    Returns:
        dict: Los datos en formato JSON o un mensaje de error.
    """
    url = f"{BASE_API_URL}/{endpoint}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza un error si la respuesta no es exitosa
        return response.json()      # Retorna los datos en formato JSON
    except requests.RequestException as e:
        return {"error": str(e)}

def enviar_datos(endpoint, datos):
    """
    Envía datos a un endpoint específico de la API.

    Args:
        endpoint (str): El endpoint al cual realizar la solicitud.
                        Ejemplo: "info-personal"
        datos (dict): Un diccionario con los datos a enviar.

    Returns:
        dict: La respuesta de la API o un mensaje de error.
    """
    url = f"{BASE_API_URL}/{endpoint}"
    try:
        response = requests.post(url, json=datos)
        response.raise_for_status()  # Lanza un error si la respuesta no es exitosa
        return response.json()       # Retorna la respuesta en formato JSON
    except requests.RequestException as e:
        return {"error": str(e)}

# Ejemplo de funciones específicas para cada endpoint
def obtener_info_personal():
    return obtener_datos("info-personal")
def enviar_info_personal(datos):
    return enviar_datos("info-personal", datos)

def obtener_contacto():
    return obtener_datos("contacto")
def enviar_contacto(datos):
    return enviar_datos("contacto", datos)

def obtener_socio_economico():
    return obtener_datos("socio-economico")
def enviar_socio_economico(datos):
    return enviar_datos("socio-economico", datos)

def obtener_situacion_sentimental():
    return obtener_datos("situacion-sentimental")
def enviar_situacion_sentimental(datos):
    return enviar_datos("situacion-sentimental", datos)

def obtener_salud():
    return obtener_datos("salud")
def enviar_salud(datos):
    return enviar_datos("salud", datos)

def obtener_habitos_y_estilo():
    return obtener_datos("habitos-y-estilo")
def enviar_habitos_y_estilo(datos):
    return enviar_datos("habitos-y-estilo", datos)

def obtener_opiniones_intereses():
    return obtener_datos("opiniones-intereses")
def enviar_opiniones_intereses(datos):
    return enviar_datos("opiniones-intereses", datos)

def obtener_consentimientos_comentarios():
    return obtener_datos("consentimientos-comentarios")
def enviar_consentimientos_comentarios(datos):
    return enviar_datos("consentimientos-comentarios", datos)
