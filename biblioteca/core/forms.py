from django import forms
from django.core.exceptions import ValidationError
from core.models import LivroModel
import re


# titulo e editora validacao
def validate_title(value):
    if len(value) < 3:
        raise ValidationError("Deve ter pelo menos 3 caracteres")


def validate_isbn(value):
    if len(value) < 13:
        raise ValidationError("Deve ter pelo menos 13 caracteres")


def validate_autor(value):
    if len(value) < 10:
        raise ValidationError("Deve ter pelo menos 10 caracteres")


# Número de Páginas: Validar a string para cadastro entre 1 e 3 caracteres e todos numéricos.
def validate_numero_paginas(value):
    # /d garante 0a9 numeros
    if not re.match(r"^\d{1,3}$", value):
        raise ValidationError("Deve ter entre 1 e 3 numeros e somente numeros")


# Ano: : Validar a string para cadastro com exatos 4 caracteres e todos numéricos.
def validate_ano(value):
    if len(value) != 4:
        raise ValidationError("Deve ter 4 numeros")


class LivroForm(forms.ModelForm):
    class Meta:
        model = LivroModel
        fields = ["titulo", "editora"]
        error_messages = {
            "titulo": {
                "required": ("Informe o título do livro."),
            },
            "editora": {
                "required": ("Informe a editora do livro."),
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

    def clean(self):
        self.cleaned_data = super().clean()
        return self.cleaned_data
