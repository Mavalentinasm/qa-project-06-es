# Nombre del proyecto: Qa-project-06-es

Este proyecto está diseñado para automatizar pruebas para la creación de un kit, específicamente para probar el campo "name". El alcance de las pruebas incluye verificar limitaciones en el número de caracteres, tipos de letras, espacios, caracteres especiales, campos vacíos, entre otros.

## Proceso de automatización:

El proceso de automatización se llevó a cabo en los siguientes pasos:

1. **Instalación de paquetes esenciales**: Se instaló pip, pytest y request para facilitar las pruebas.

2. **Configuración de parámetros**: Se almacenó la URL actualizada del servidor, las APIs correspondientes y las rutas de los documentos en el archivo `configuracion.py`.

3. **Datos necesarios para las solicitudes**: Se recopilaron los datos necesarios para las solicitudes según la documentación de las APIs y se almacenaron en el archivo `data.py`.

4. **Creación de un usuario**: Se utilizó la API POST `/api/v1/users` en la carpeta `sender_stand_request` para crear un usuario. La información correspondiente al usuario estaba previamente almacenada en `data.py`.

    ```json
    {
        "firstName": "Max",
        "phone": "+10005553535",
        "address": "8042 Lancaster Ave.Hamburg, NY"
    }
    ```

5. **Creación de un kit vinculado al usuario**: Se utilizó la API POST `/api/v1/kits` para crear un kit y vincularlo al usuario recién creado. Se usó un Bearer Token obtenido tras la creación del usuario para esta vinculación. Ejemplo de headers:

    ```python
    headers_for_kits = {
        'Authorization': 'Bearer 1a563bd1-27b5-4d48-8094-d99506d2a678'
    }
    ```

    La información del kit proporcionada por `api/docs` es:

    ```json
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
    ```

    Nota: Se modificó el valor `null` por `1` en el campo `productsList` para obtener un resultado positivo en la creación del kit. Ambos valores estaban previamente almacenados en `data.py`.

## Pruebas realizadas:

El proceso de pruebas siguió los siguientes pasos:

1. Se especificó la función que se deseaba probar.
2. Se invocó la función `positive_asserts` para clasificar las respuestas positivas.
3. Se identificaron las respuestas positivas en una lista para ordenarlas y luego probarlas individualmente.
4. Se invocó la función `negative_asserts` para clasificar las respuestas negativas.
5. Se identificaron las respuestas negativas en una lista para ordenarlas y luego probarlas individualmente.

## Resultado:

Todas las respuestas positivas pasaron las pruebas, mientras que las respuestas negativas no lo hicieron. Esto era esperado ya que las pruebas son esencialmente las mismas pero con diferentes resultados esperados.

¡Gracias por revisar este proyecto!
