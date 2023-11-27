Ma.Valentina Serrano, 5to grupo, Sprint 6 

Nombre del proyecto: Qa-project-06-es 

  El proyecto está creado para automatizar las pruebas para crear un kit, en especifico para testear el campo "name". Comprende las limitaciones de numero de caracteres, tipos de letras, espacios, caracteres especiales, campo vacio y otros. Dichas pruebas de automatización se ejecutan mediante una lista de comprobación que contiene 9 casos para lo que fue necesario en este orden:  

  1-Instalar los paquetes esenciales: pip, pytest y request

  2-En la carpeta "configuracion.py" almacenar la URL actualizada del servidor, las apis correspondientes y la ruta de los documentos.

  3-Según la documentación de las apis en la carpeta "data.py" almacenamos los datos necesarios para la creación de solicitudes posteriores.


  4- Crear un usuario mediante la api POST /api/v1/users en la carpeta "sender_stand_request", la información correspondiente al usuario ya estaba almacenada en "data.py"

  {
    "firstName": "Max",
    "phone": "+10005553535",
    "address": "8042 Lancaster Ave.Hamburg, NY"
}

  5- Crear un kit para el usuario mediante la api POST /api/v1/kits, vinculamos este kit a ese usuario recien creado a través del Bearer Token que la creación del usuario arrojo(Este token puede variar cada vez que actualizamos el servidor pero dejo un ejemplo ya que es un parametro para la vinculacion del usuario al kit:

  headers_for_kits = {
      'Authorization': 'Bearer 1a563bd1-27b5-4d48-8094-d99506d2a678'
  }

  La informacion del kit que aporta api/docs es:

{
       "name": "Mi conjunto",
       "card": {
           "id": 1,
           "name": "Para la situación"
       },
       "productsList": null,
       "id": 7,
       "productsCount": 0
   }

Ambos estaban previamente almacenadas en la carpeta "Data.py"
Es importante aclarar que en mi proyecto sustituí el "null" por un "1" para obtener resultado positivo de la creación del kit.


LLegó el momento de probar los casos

Antes de empezar cualquier prueba, me asegure de estar exportando debidamente los archivos que fueran necesarios en cada carpeta y tener actualizada la URL y luego en ese orden:

1-Dejé claro sobre que función deseaba testear.
2-LLamé a la funcion positive_asserts para clasificar mis respuestas positivas. 
3-Observé en mi lista cuales eran mis respuestas positivas para ordenarlas todas juntas y luego las probé una a una.
4-LLamé a la funcion negative_asserts para clasificar mis respuestas negativas.
5-Observé en mi lista cuales eran mis respuestas negativas para ordenarlas todas juntas y luego las probe una a una.

Resultado: Todas las respuestas positivas pasaron el test y las negativas lo reprobaron, hace mucho sentido ya que son prácticamente las mismas pruebas pero con otro resultado esperado. 

Muchas gracias por revisar este proyecto!
