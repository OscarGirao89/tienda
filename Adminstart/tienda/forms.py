from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class registro_form(UserCreationForm):
    email = forms.EmailField(
        max_length=254,
        help_text="Requerido. Ingrese una dirección de correo electrónico válida.",
    )

    class f_registro:
        model = User
        campos = ["username", "email", "password1", "password2"]


class inicio_form(AuthenticationForm):
    pass
