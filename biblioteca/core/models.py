from django.db import models


class LivroModel(models.Model):
    titulo = models.CharField("Título", max_length=200)
    editora = models.CharField("editora", max_length=200)
    ano = models.IntegerField("ano", null=True)
    autor = models.CharField("Autor", null=True, max_length=200)
    isbn = models.CharField("ISBN", null=True, max_length=200)
    numero_paginas = models.IntegerField("Número de Páginas", null=True)
    data_cadastro = models.DateTimeField(
        "Data de Cadastro", null=True, auto_now_add=True
    )
    data_alteracao = models.DateTimeField("Data de Alteração", null=True, auto_now=True)
    objects = models.Manager()

    # def __str__(self):
    #     return self.titulo
