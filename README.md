# WunderlistPython
Un script de consola escrito en python para crear tareas de forma individual y masiva en tu cuenta de Wunderlist

## Configurar el script

1. Accede a [https://developer.wunderlist.com]()
2. Crea una nueva app desde el menú **Register your app**. Utiliza el nombre y descripción que desees
3. Teclea "http://www.wunderlist.com" en los campos **APP URL** y **AUTH CALLBACK URL**
4. Una vez creada la app, genera un **Access Token** manualmente
5. Abre el fichero wunderlist.py en tu editor favorito
6. Modifica las siguientes dos lineas para incluir la información que acabas de generar para tu app

```python
   CLIENT_ID = "PUT_YOUR_CLIENT_ID_HERE"
   ACCESS_TOKEN = "PUT_YOUR_ACCESS_TOKEN_HERE"
```

## Utilizar el script

El script cuenta con dos opciones:

- Creación de tareas de forma individual

```python
   python3 wunderlist.py -t "Nombre de la tarea a crear"
```

- Creación de tareas de forma masiva desde un fichero de texto (una línea por tarea)

```python
   python3 wunderlist.py -f nombre_del_fichero
```
