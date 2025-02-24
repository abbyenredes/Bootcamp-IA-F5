from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=250, null=False) # null=fase campo requerido
    author = models.CharField(max_length=100)
    description = models.TextField()
    publish_date = models.DateField() # DateTimeField es para fecha y hora
    isbn = models.CharField(max_length=13, unique=True)
    
    def __str__(self):
        return self.title