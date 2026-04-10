# Yu-Gi-Oh Nexus App

## Descripción general
Yu-Gi-Oh Nexus App es una aplicación interactiva diseñada para la búsqueda, gestión y análisis de cartas del juego de cartas coleccionables Yu-Gi-Oh!. El sistema permite a los usuarios buscar cartas específicas, visualizar sus detalles técnicos, gestionar un mazo personalizado (Deck Builder) y realizar análisis estratégicos basados en las estadísticas de las cartas.

La aplicación utiliza la API de Yu-Gi-Oh (YGOPRODeck) para obtener información actualizada y precisa directamente desde sus servidores oficiales.

## Tecnologías utilizadas
El desarrollo de este proyecto se fundamenta en el uso de herramientas modernas que garantizan escalabilidad y un alto rendimiento:

* **Python:** Lenguaje de programación principal para la lógica de negocio.
* **Streamlit:** Framework utilizado para la creación de la interfaz de usuario web interactiva.
* **Requests:** Biblioteca para la gestión de peticiones HTTP al servidor de la API.
* **API YGOPRODeck:** Fuente de datos centralizada para la información de las cartas.

## Instalación y ejecución
Para desplegar el proyecto en un entorno local, siga estos pasos:

1. **Clonar el repositorio:**
   ```bash
   git clone <url-del-repositorio>
   ```

2. **Instalar dependencias:**
   Asegúrese de tener instalado Python y ejecute:
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar la aplicación:**
   Inicie el servidor de Streamlit con el siguiente comando:
   ```bash
   streamlit run app.py
   ```

## Estructura del proyecto
El proyecto sigue una estructura modular basada en la separación de responsabilidades (MVC), lo que facilita el mantenimiento y la escalabilidad del código:

```text
yugioh_app/
├── app.py                # Punto de entrada de la aplicación Streamlit
├── requirements.txt       # Dependencias del proyecto
├── controllers/          # Lógica de control y coordinación
├── models/               # Modelos de datos y lógica de persistencia
├── views/                # Componentes de la interfaz de usuario
├── utils/                # Servicios externos y funciones auxiliares
└── data/                 # Almacenamiento local en formato JSON
```

## Archivos clave y diseño de la aplicación

1) **app.py (entrada principal):**
   Configura la UI de Streamlit y gestiona el layout. Usa `initialize_session_state()` para sesión, `render_search_section()` para búsqueda y el renderizado dinámico de resultados. Llama a controladores y vistas según la navegación del usuario.

2) **Modelo (data):**
   *   `models/card_model.py`: Clases y funciones para el procesamiento técnico de los datos de las cartas.
   *   `models/deck_model.py`: Gestión de persistencia del mazo de usuario en `data/deck.json`.
   *   `models/history_model.py`: Gestión de persistencia del historial de búsquedas en `data/history.json`.

3) **Controladores (lógica):**
   *   `controllers/yugioh_controller.py`: Funciones `manejar_busqueda()` y `manejar_aleatorio()` que coordinan la lógica de negocio y el estado de la aplicación.
   *   `controllers/deck_controller.py`: Lógica para la gestión del mazo y el cálculo de diagnósticos estratégicos (`analizar_mazo()`).

4) **Vistas (UI):**
   *   `views/layout.py`: Configura los parámetros de Streamlit, el tema Premium, encabezado, pie de página y carga de CSS.
   *   `views/yugioh_view.py`: Renderiza la tarjeta de la carta, la barra lateral de información y la sección de búsqueda.
   *   `views/deck_view.py`: Renderiza la vista del mazo, permitiendo previsualizar y eliminar cartas.
   *   `views/analysis_view.py`: Muestra el panel de diagnóstico de sinergia y composición del mazo.

5) **Utilidades:**
   *   `utils/constants.py`: Define constantes globales como el endpoint de la API y rutas de archivos.
   *   `utils/helpers.py`: Funciones de utilidad para operaciones repetitivas (carga/guardado de JSON, formateo).
   *   `utils/yugioh_service.py`: Centraliza las peticiones HTTP a la API externa de YGOPRODeck.

6) **Datos JSON:**
   *   `data/deck.json`: Archivo de persistencia para el mazo activo.
   *   `data/history.json`: Archivo de persistencia para el historial de consultas locales.

## Flujo de ejecución principal

1. El usuario abre la aplicación y realiza una búsqueda por nombre o solicita una carta aleatoria.
2. Se invoca la función `manejar_busqueda()` o `manejar_aleatorio()` en `controllers/yugioh_controller.py`.
3. El controlador obtiene los datos técnicos desde el servicio de API (`utils/yugioh_service.py`).
4. La vista correspondiente en `views/yugioh_view.py` renderiza la tarjeta de la carta y los botones de interacción ("Añadir al mazo").
5. Si el usuario modifica el mazo, los cambios se persisten automáticamente en `data/deck.json`.
6. Al navegar a la pestaña de análisis, se procesan los datos del mazo para generar diagnósticos automáticos.

## Funcionalidades del sistema
La aplicación ofrece un conjunto de herramientas técnicas para los entusiastas de Yu-Gi-Oh!:

* **Búsqueda de cartas por nombre:** Acceso instantáneo a la base de datos oficial.
* **Visualización de información detallada:** Despliegue de estadísticas, descripciones e imágenes de alta calidad.
* **Registro de historial de búsquedas:** Persistencia de las consultas recientes para acceso rápido.
* **Construcción de mazos (Deck Builder):** Herramienta para crear y gestionar mazos personalizados.
* **Validación de reglas del mazo:** Control automático de límites (máximo 40 cartas y máximo 3 copias por cada carta).
* **Análisis de sinergia del mazo:** Diagnóstico basado en algoritmos de balance y potencia.

## Información de la API
* **Nombre de la API:** YGOPRODeck API
* **Tipo:** REST API
* **URL base:** [https://db.ygoprodeck.com/api/v7/](https://db.ygoprodeck.com/api/v7/)

Esta es una API pública y gratuita (Free API) que no requiere claves de acceso (API Keys) para su consumo básico, lo que facilita el desarrollo de aplicaciones de código abierto y herramientas para la comunidad.

## Endpoints utilizados
El proyecto consume principalmente los siguientes endpoints:

### Búsqueda de cartas
`GET /cardinfo.php`

Este endpoint permite filtrar cartas basándose en diversos criterios de búsqueda.

**Parámetros aceptados:**
* `name`: Permite realizar búsquedas por el nombre exacto de la carta.
* `type`: Filtra por el tipo de carta (ej: Monster, Spell, Trap).
* `atk`: Filtra cartas con un valor de ataque específico.
* `def`: Filtra cartas con un valor de defensa específico.

**Ejemplo de petición:**
`https://db.ygoprodeck.com/api/v7/cardinfo.php?name=Dark%20Magician`

**Campos importantes en la respuesta:**
* `id`: Identificador único numérico de la carta.
* `name`: Nombre oficial de la carta.
* `type`: Categoría de la carta (Normal Monster, Ritual Effect Monster, etc.).
* `desc`: Texto descriptivo con el efecto o historia de la carta.
* `atk`: Puntos de ataque (si aplica).
* `def`: Puntos de defensa (si aplica).
* `level`: Nivel o Rango de la carta.
* `race`: Tipo de criatura o clasificación (ej: Spellcaster, Warrior).
* `attribute`: Atributo elemental (ej: DARK, LIGHT).
* `card_images`: Arreglo de URLs que contienen las imágenes de las cartas en diferentes tamaños.

### Ejemplo de respuesta JSON
A continuación se presenta una estructura simplificada de la respuesta obtenida al consultar una carta específica:

```json
{
  "id": 46986414,
  "name": "Dark Magician",
  "type": "Normal Monster",
  "atk": 2500,
  "def": 2100,
  "attribute": "DARK"
}
```

## Ejemplo de uso en Python
A continuación se muestra cómo se realiza el consumo de la API dentro del entorno de desarrollo utilizando la biblioteca `requests`.

```python
import requests

def consultar_api_yugioh(nombre_carta):
    # Definición de la URL y parámetros
    url = "https://db.ygoprodeck.com/api/v7/cardinfo.php"
    params = {'name': nombre_carta}

    try:
        # Ejecución de la petición GET
        response = requests.get(url, params=params)
        
        # Validación del código de estado HTTP
        if response.status_code == 200:
            # Conversión de la respuesta a formato JSON
            data = response.json()
            
            # Validación adicional de la estructura de datos
            if data and 'data' in data:
                return data['data']
            else:
                return []
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")
        return None
```

## Integración en el proyecto
La API se integra de forma modular siguiendo la arquitectura MVC del proyecto:

1. **Búsqueda de cartas:** El controlador utiliza el servicio de API para buscar coincidencias basadas en el input del usuario.
2. **Interfaz de usuario:** Los datos se renderizan en Streamlit utilizando componentes personalizados para mostrar imágenes y estadísticas.
3. **Deck Builder:** Las cartas recuperadas pueden ser añadidas al mazo local, persistiendo los datos básicos en formato JSON.
4. **Análisis de mazo:** El sistema procesa los atributos y niveles de las cartas obtenidas vía API para generar reportes sobre el balance estratégico del mazo.

## Manejo de errores
Para garantizar la estabilidad de la aplicación, se implementan las siguientes validaciones:

* **Carta inexistente:** Se captura el error 400 que devuelve la API cuando no encuentra coincidencias, mostrando un mensaje informativo al usuario.
* **Respuestas vacías:** Se valida que la lista de resultados no sea nula antes de intentar procesar cualquier objeto `Card`.
* **Validación de datos None:** Debido a que las cartas de tipo Spell y Trap no poseen estadísticas de combate, se implementa lógica para manejar valores `None` en los campos `atk` y `def`, evitando errores de ejecución durante el renderizado o análisis.

## Ventajas de la API
* **Gratuita:** No genera costos operativos para el proyecto.
* **Sin autenticación:** Elimina la complejidad de gestionar tokens o cabeceras OAuth.
* **Gran cantidad de datos:** Ofrece acceso a miles de cartas y variaciones.
* **Fácil integración:** Formato JSON estándar y bien documentado.

## Limitaciones
* **Conexión a internet:** Al ser un servicio externo, la aplicación requiere acceso constante a la red.
* **Campos opcionales:** Algunos campos (como el precio o estadísticas) pueden no estar presentes en todas las cartas.
* **Solo lectura:** No permite la creación o modificación de registros en la base de datos oficial (Operaciones GET únicamente).

## Conclusión
La integración de la API de YGOPRODeck trasciende la mera visualización de datos, funcionando como el motor que soporta la lógica de negocio y las reglas del sistema. La arquitectura implementada procesa la información en tiempo real para habilitar las funcionalidades principales:

1. **Lógica del Deck Builder:** El sistema valida las reglas oficiales de construcción de mazos, permitiendo un máximo de 40 cartas y restringiendo la inclusión de más de 3 copias por cada carta individual basándose en su identificador único.
2. **Análisis de Sinergia y Diagnóstico:** Mediante el procesamiento de los campos obtenidos (ATK, DEF, Type), el sistema realiza cálculos estadísticos para determinar promedios de potencia ofensiva y defensiva.
3. **Evaluación de Estrategia:** El algoritmo evalúa el balance del mazo analizando la distribución entre monstruos y cartas de soporte (mágicas/trampas), clasificando la estrategia resultante como agresiva (beatdown), equilibrada o vulnerable, proporcionando diagnósticos técnicos automáticos para el usuario.
