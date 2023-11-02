from django import forms
from django.core.exceptions import ValidationError
from core.models import LivroModel
import re


# titulo e editora validacao
def validate_title(value):
    if len(value) < 3:
        raise ValidationError("Editora deve ter pelo menos 3 caracteres")


def validate_isbn(value):
    if len(value) < 13:
        raise ValidationError("ISBN deve ter pelo menos 13 caracteres")


def validate_autor(value):
    if len(value) < 10:
        raise ValidationError("Autor Deve ter pelo menos 10 caracteres")


# Número de Páginas: Validar a string para cadastro entre 1 e 3 caracteres e todos numéricos.
def validate_numero_paginas(value):
    # /d garante 0a9 numeros
    if value < 1 or value > 999:
        raise ValidationError("Quantidade de paginas deve ser entre 1 e 999")


# Ano: : Validar a string para cadastro com exatos 4 caracteres e todos numéricos.
# def validate_ano(value):
#     if value < 4:
#         raise ValidationError("Informe o ano de publicação do livro.")
def validate_ano(value):
    if len(str(value)) != 4 or not str(value).isdigit():
        raise ValidationError("O ano deve conter exatamente 4 dígitos numéricos.")


class LivroForm(forms.ModelForm):
    class Meta:
        model = LivroModel
        fields = ["titulo", "editora", "isbn", "autor", "numero_paginas", "ano"]
        error_messages = {
            "titulo": {
                "required": ("Informe o título do livro."),
            },
            "editora": {
                "required": ("Informe a editora do livro."),
            },
            "isbn": {
                "required": ("Informe o ISBN do livro."),
            },
            "autor": {
                "required": ("Informe o autor do livro."),
            },
            "numero_paginas": {
                "required": ("Informe o número de páginas do livro."),
            },
            "ano": {
                "required": ("Informe o ano de publicação do livro."),
            },
        }

    # Novos campos
    #     O cliente deseja armazenar os novos campos referente a livros:

    #     Autor
    #     ISBN
    #     Número de Páginas
    #     Ano em que a obra foi escrita

    def clean_titulo(self):
        titulo = self.cleaned_data["titulo"]
        validate_title(titulo)
        return titulo

    def clean_editora(self):
        editora = self.cleaned_data["editora"]
        # usa a mesma validacao do titulo com 3 caracteres
        validate_title(editora)
        return editora

    def clean_isbn(self):
        isbn = self.cleaned_data["isbn"]
        validate_isbn(isbn)
        return isbn

    def clean_autor(self):
        autor = self.cleaned_data["autor"]
        validate_autor(autor)
        return autor

    def clean_numero_paginas(self):
        numero_paginas = self.cleaned_data["numero_paginas"]
        validate_numero_paginas(numero_paginas)
        return numero_paginas

    def clean_ano(self):
        ano = self.cleaned_data["ano"]
        validate_ano(ano)
        return ano

    def clean(self):
        self.cleaned_data = super().clean()
        return self.cleaned_data
