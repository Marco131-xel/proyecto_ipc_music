from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Cliente
from .forms import ProductoForm, ClienteForm

# Listas para los productos
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'producto/lista_productos.html', {'productos': productos})

def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'producto/detalle_producto.html', {'producto': producto})

def nuevo_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.save()
            return redirect('detalle_producto', pk=producto.pk)
    else:
        form = ProductoForm()
    return render(request, 'producto/nuevo_producto.html', {'form': form})

def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.save()
            return redirect('detalle_producto', pk=producto.pk)
    else:
        form = ProductoForm(instance=producto)
    
    return render(request, 'producto/editar_producto.html', {'form': form})

def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    
    if request.method == "POST":
        producto.delete()
        return redirect('lista_productos')

    return render(request, 'producto/eliminar_producto.html', {'producto': producto})

# Listas para clientes

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/lista_clientes.html', {'clientes': clientes})

def detalle_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'cliente/detalle_cliente.html', {'cliente': cliente})

def nuevo_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.save()
            return redirect('detalle_cliente', pk=cliente.pk)
    else:
        form = ClienteForm()
    return render(request, 'cliente/nuevo_cliente.html', {'form': form})

def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.save()
            return redirect('detalle_cliente', pk=cliente.pk)
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'cliente/editar_cliente.html', {'form': form})

def eliminar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    cliente.delete()
    return redirect('lista_clientes')

# miapp
def pagina_inicio(request):
    return render(request, 'menu/pagina_inicio.html')
