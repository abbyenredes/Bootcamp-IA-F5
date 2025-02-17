# Ejecutar django en un entorno virtual usando uv

Creamos una nueva carpeta que sera nuestro entorno virtua (carpeta madre), en este caso sera una tienda de libros

```plaintext
mkdir book_store
```
Accedemos a esta carpeta:

```plaintext
cd book_store
```
Creamos el entorno virtual usando uv:

```plaintext
uv venv .venv
```
Iniciamos ese entorno virtual:

```plaintext
source .venv/bin/activate
```
Iniciamos nuestro proyecto (esto nos crea el archivo pyproject.toml):

```plaintext
uv init --bare
```
Descargamos nuestra dependencia de django (nos crea el archivo uv.lock):

```plaintext
uv add django
```
Abrimos VS:

```plaintext
code .
```
Iniciamos el proyecto en django:

```plaintext 
django-admin startproject book_manage .
```
Nos crea la carpeta book_manage que contiene los sigientes archivos:

![book](https://github.com/abbyenredes/Bootcamp-IA-F5/blob/main/Taller_django/img/book.png)

Por ultimo iniciamos la app:

```plaintext
 django-admin startapp books
```
Nos crea la carpeta books que contiene los sigientes archivos:

## Configuracion
En la carpeta book_manage -> settings.py -> instale apps agregamos una linea para `"Books",`
