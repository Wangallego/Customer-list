Busqueda-lista-clientes
Una plantilla que sirve para filtrar y mostrar los detalles del cliente. Este programa es una aplicación web desarrollada con Flask que permite gestionar una lista de clientes. Los clientes se cargan desde un archivo CSV y se muestran en una página web donde se pueden buscar y ver los detalles de cada cliente.

#Estructura de la aplicación La estructura de la aplicación se organiza de la siguiente manera:

-app.py: Archivo principal de la aplicación Flask.
-model.py: Contiene la definición de la clase Cliente y métodos relacionados.
-templates/: Carpeta que contiene las plantillas HTML utilizadas por la aplicación.
-base.html: Plantilla base que define la estructura común de las páginas.
-clientes.html: Plantilla para la página principal que muestra la lista de clientes.
-detalle_cliente.html: Plantilla para mostrar los detalles de un cliente específico.
-404.html: Plantilla para mostrar la página de error 404.
-static/: Carpeta que contiene archivos estáticos, como imágenes o archivos CSS.
-perfil.jpg: Imagen utilizada en la página de detalle del cliente.
-data/: Carpeta que contiene los datos de los clientes en formato CSV. #Esquema de rutas: Ruta principal ("/"): Muestra la -- 
 lista de clientes y permite realizar búsquedas y paginación. Ruta de detalle de cliente ("/detalle_cliente/int:id"): Muestra 
 los detalles de un cliente según su ID. Ruta de búsqueda de cliente ("/detalle_cliente"): Permite buscar clientes por 
 nombre, apellido y ciudad.
-Ruta de error 404 ("/404"): Página de error cuando una página no se encuentra.
#Descripción breve del modelo El modelo de la aplicación incluye una clase llamada Cliente, que representa a un cliente. Cada instancia de la clase Cliente tiene las siguientes propiedades:

id: ID del cliente.
nombre: Nombre del cliente.
apellidos: Apellidos del cliente.
sexo: Género del cliente.
email: Dirección de correo electrónico del cliente.
telefono: Número de teléfono del cliente.
direccion: Dirección del cliente.
ciudad: Ciudad del cliente.
pais: País del cliente.
El modelo incluye métodos para cargar los datos de los clientes desde un archivo CSV, buscar clientes por ID y filtrar clientes según ciertos criterios. Estos métodos son utilizados por la aplicación para acceder y manipular los datos de los clientes.
#Instrucciones de ejecución Puesta en marcha Para ejecutar la aplicación, sigue estos pasos:

Asegúrate de tener Python instalado en tu sistema.

Instala las dependencias del programa ejecutando el siguiente comando en tu terminal:

pip install flask Abre el archivo app.py en tu editor de código y asegúrate de tener la siguiente línea al final del archivo:

if name == 'main': app.run(debug=True) Ejecuta el archivo app.py desde tu terminal para iniciar el servidor Flask: python app.py Abre tu navegador web y visita la dirección http://localhost:5000 para ver la aplicación en funcionamiento.

Nota Asegúrate de tener el archivo clientes.csv en la carpeta data dentro del directorio del programa. Este archivo debe contener los datos de los clientes en formato CSV para que la carga de clientes funcione correctamente.
