from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Cliente, Factura, DetalleFactura
from .forms import ProductoForm, ClienteForm, FacturaForm, DetalleFacturaForm

# Funciones para Listas para los productos
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
    
    return render(request, 'producto/editar_producto.html', {'form': form, 'producto': producto})

def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    
    if request.method == "POST":
        producto.delete()
        return redirect('lista_productos')

    return render(request, 'producto/eliminar_producto.html', {'producto': producto})

# Funciones para Listas para clientes

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
    return render(request, 'cliente/editar_cliente.html', {'form': form, 'cliente': cliente})

def eliminar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)

    if request.method == "POST":
        cliente.delete()
        return redirect('lista_clientes')

    return render(request, 'cliente/eliminar_cliente.html', {'cliente': cliente})

# Funciones para Listas para las facturas

def lista_facturas(request):
    facturas = Factura.objects.all()
    return render(request, 'factura/lista_facturas.html', {'facturas': facturas})

def detalle_factura(request, pk):
    factura = get_object_or_404(Factura, pk=pk)
    detalles = DetalleFactura.objects.filter(factura=factura)

    # Calcula el total de la factura sumando los subtotales de cada detalle
    total_factura = sum(detalle.subtotal for detalle in detalles)

    return render(request, 'factura/detalle_factura.html', {'factura': factura, 'detalles': detalles, 'total_factura': total_factura})

def crear_factura(request):
    if request.method == "POST":
        # Creamos el formulario de la factura
        factura_form = FacturaForm(request.POST)
        detalle_form = DetalleFacturaForm(request.POST)

        if factura_form.is_valid() and detalle_form.is_valid():
            # Guardamos la factura sin commit para poder asignar el cliente después
            factura = factura_form.save(commit=False)

            # Asignamos el cliente
            cliente_id = request.POST.get('cliente')
            cliente = get_object_or_404(Cliente, pk=cliente_id)
            factura.cliente = cliente
            factura.save()

            # Guardamos el detalle de la factura
            detalle = detalle_form.save(commit=False)
            detalle.factura = factura
            detalle.save()

            return redirect('detalle_factura', pk=factura.pk)
    else:
        factura_form = FacturaForm()
        detalle_form = DetalleFacturaForm()

    return render(request, 'factura/crear_factura.html', {'factura_form': factura_form, 'detalle_form': detalle_form})

def editar_factura(request, pk):
    factura = get_object_or_404(Factura, pk=pk)
    detalles = DetalleFactura.objects.filter(factura=factura)

    if request.method == "POST":
        detalle_form = DetalleFacturaForm(request.POST)

        if detalle_form.is_valid():
            # Actualiza los campos de producto y cantidad
            factura_detalle = detalles.first()  # Suponemos que hay solo un detalle por factura
            factura_detalle.producto = detalle_form.cleaned_data['producto']
            factura_detalle.cantidad = detalle_form.cleaned_data['cantidad']
            factura_detalle.save()

            return redirect('detalle_factura', pk=factura.pk)
    else:
        # Rellena el formulario con los datos actuales
        detalle_form = DetalleFacturaForm(initial={'producto': detalles.first().producto,
                                                   'cantidad': detalles.first().cantidad})

    return render(request, 'factura/editar_factura.html', {'factura': factura, 'detalle_form': detalle_form})


def eliminar_factura(request, pk):
    factura = get_object_or_404(Factura, pk=pk)

    if request.method == "POST":
        factura.delete()
        return redirect('lista_facturas')

    return render(request, 'factura/eliminar_factura.html', {'factura': factura})

# miapp
def pagina_inicio(request):
    return render(request, 'menu/pagina_inicio.html')
