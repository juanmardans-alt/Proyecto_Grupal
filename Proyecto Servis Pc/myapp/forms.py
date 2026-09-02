from django import forms
from .models import Cliente


class ClientesFormulario(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'telefono', 'email', 'direccion']
    telefono = forms.CharField(max_length=20, label="Teléfono")
    email = forms.EmailField(label="Correo Electrónico")
    direccion = forms.CharField(max_length=200, label="Dirección")
class ClientesFilter(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'telefono', 'email']

