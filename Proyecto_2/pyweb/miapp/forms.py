from django import forms
from .models import Producto, Cliente, Factura, DetalleFactura

# Clase form para Producto
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre','descripcion','precio','stock']
    
# Clase form para Cliente
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nit','nombre','direccion']

# Clase form para Facturas
class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['cliente']

class DetalleFacturaForm(forms.ModelForm):
    class Meta:
        model = DetalleFactura
        fields = ['producto', 'cantidad']

    