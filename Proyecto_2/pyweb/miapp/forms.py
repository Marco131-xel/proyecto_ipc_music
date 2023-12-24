from django import forms
from .models import Producto, Cliente

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre','descripcion','precio','stock']
    
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nit','nombre','direccion']
    