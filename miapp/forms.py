from django import forms
from django.core import validators

class FormCurso(forms.Form):
    titulo = forms.CharField(
        label="Titulo",
        max_length=40,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese el título',
                'class': 'titulo_form_curso'
            }
        ),
        validators=[
            validators.MinLengthValidator(4,'El título es corto'),
            validators.RegexValidator('^[A-Za-z0-9ñÑ ]*$','El título tiene caracteres inválidos','titulo_invalido')
        ]
    )

    contenido = forms.CharField(
        label="Contenido",
        widget=forms.Textarea,
        validators=[
            validators.MaxLengthValidator(500,'Superaste el límite de caracteres')
        ]        
    )
    contenido.widget.attrs.update({
        'placeholder': 'Ingrese el contenido del curso',
        'class': 'contenido_form_curso',
        'id':'contenido_form'
    })

    opciones_publicado = [
        (1,'Si'),
        (0,'No'),
    ]
    publicado = forms.TypedChoiceField(
        label="¿Publicado?",
        choices=opciones_publicado
    )

class FormCarrera(forms.Form):
    titulo = forms.CharField(
        label="Titulo",
        max_length=40,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese el título',
                'class': 'titulo_form_carrera'
            }
        ),
        validators=[
            validators.MinLengthValidator(4,'El título es corto'),
            validators.RegexValidator('^[A-Za-z0-9ñÑ ]*$','El título tiene caracteres inválidos','titulo_invalido')
        ]
    )

    contenido = forms.CharField(
        label="Contenido",
        widget=forms.Textarea,
        validators=[
            validators.MaxLengthValidator(500,'Superaste el límite de caracteres')
        ]        
    )
    contenido.widget.attrs.update({
        'placeholder': 'Ingrese el contenido del curso',
        'class': 'contenido_form_curso',
        'id':'contenido_form'
    })

    opciones_publicado = [
        (1,'Si'),
        (0,'No'),
    ]
    publicado = forms.TypedChoiceField(
        label="¿Publicado?",
        choices=opciones_publicado
    )