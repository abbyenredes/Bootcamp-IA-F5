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

En la carpeta book_manage -> settings.py -> instale apps agregamos una linea para `'books',` para anexarlo.

![setting](https://github.com/abbyenredes/Bootcamp-IA-F5/blob/main/Taller_django/img/setting.png)

> [!IMPORTANT]
> escribir books con b minuscula ya que si no dara error

Por ultimo iniciamos la app:

```plaintext
 django-admin startapp books
```
Nos crea la carpeta books que contiene los sigientes archivos:

![book2](https://github.com/abbyenredes/Bootcamp-IA-F5/blob/main/Taller_django/img/book2.png)

## Configuracion

En la carpeta books -> models.py realizamos el siguiente modelo:

```python
class Book(models.Model):
    title = models.CharField(max_length=250, null=False) # null=fase campo requerido
    author = models.CharField(max_length=100)
    description = models.TextField()
    publish_date = models.DateField() # DateTimeField es para fecha y hora
    isbn = models.CharField(max_length=13, unique=True)
    
    def __str__(self):
        return self.title
```
Ejacutamos el siguiente comando para crear nuestro modelo:

```plaintext
python3 manage.py makemigrations
```

En la misma carpeta archivo admin.py importamos nuestro modelo:

```python
from django.contrib import admin
from.models import Book
# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author', 'publish_date', 'isbn')
    search_fields = ('title', 'author', 'isbn')
    list_filter = ('publish_date', 'author')
```

 Ejecutamos el siguiente comando para empezar la migración:

```plaintext
 python3 manage.py migrate
```

Finalmente vamos a crear nuestro super user:

```plaintext
 python3 manage.py createsuperuser
```

![superuser](https://github.com/abbyenredes/Bootcamp-IA-F5/blob/main/Taller_django/img/superusuario-_1_.gif)

Y accedemos al servidor de django

```plaintext
python manage.py runserver
```

![acceso](https://github.com/abbyenredes/Bootcamp-IA-F5/blob/main/Taller_django/img/acceso.gif)
