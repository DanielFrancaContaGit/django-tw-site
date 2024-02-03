from django.db import models

# Create your models here.

class Produtos(models.Model):
    object = models.Manager
    name = models.CharField(max_length=400)
    description = models.CharField(max_length=800)
    url = models.TextField(max_length=10000)

    def __str__(self):
        return f'{self.name} criado com sucesso'


class Home(models.Model):
    object = models.Manager
    title = models.CharField(max_length=400)
    sub_title = models.TextField(max_length=1000)

    def __str__(self):
        return self.title
    