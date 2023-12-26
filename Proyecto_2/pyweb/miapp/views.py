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

# Funciones para las Facturas
def crear_factura(request):
    productos = Producto.objects.all()

    if request.method == 'POST':
        print(request.POST)
        cliente_form = ClienteForm(request.POST, prefix='cliente')
        factura_form = FacturaForm(request.POST, prefix='factura')
        detalle_form = DetalleFacturaForm(request.POST, prefix='detalle')

        if cliente_form.is_valid() and factura_form.is_valid() and detalle_form.is_valid():
            cliente = cliente_form.save()
            factura = factura_form.save(commit=False)
            factura.cliente = cliente
            factura.save()

            detalle = detalle_form.save(commit=False)
            detalle.factura = factura
            detalle.save()

            return redirect('detalle_factura', pk=factura.pk)
    else:
        cliente_form = ClienteForm(prefix='cliente')
        factura_form = FacturaForm(prefix='factura')
        detalle_form = DetalleFacturaForm(prefix='detalle')

    return render(request, 'factura/crear_factura.html', {
        'cliente_form': cliente_form,
        'factura_form': factura_form,
        'detalle_form': detalle_form,
        'clientes': Cliente.objects.all(),
        'productos': productos,
    })
    
def guardar_factura(request):
    if request.method == 'POST':
        factura_form = FacturaForm(request.POST)
        detalle_formset = DetalleFacturaForm(request.POST, prefix='detalle')

        if factura_form.is_valid() and detalle_formset.is_valid():
            factura = factura_form.save()
            detalle_formset.instance = factura  # Asocia el detalle con la factura recién creada
            detalle_formset.save()

            # Redirige a la página de detalles de la factura
            return redirect('detalle_factura', pk=factura.pk)

    else:
        factura_form = FacturaForm()
        detalle_formset = DetalleFacturaForm(prefix='detalle')

    return render(request, 'factura/crear_factura.html', {
        'factura_form': factura_form,
        'detalle_formset': detalle_formset,
        'clientes': Cliente.objects.all(),
        'productos': Producto.objects.all(),
    })

def lista_facturas(request):
    facturas = Factura.objects.all()
    return render(request, 'factura/lista_facturas.html', {'facturas': facturas})

def detalle_factura(request, pk):
    factura = get_object_or_404(Factura, pk=pk)
    detalle = DetalleFactura.objects.filter(factura=factura)

    if request.method == 'POST':
        factura_form = FacturaForm(request.POST, instance=factura)
        detalle_form = DetalleFacturaForm(request.POST, prefix='detalle')

        if factura_form.is_valid() and detalle_form.is_valid():
            factura_form.save()

            detalle = detalle_form.save(commit=False)
            detalle.factura = factura
            detalle.save()

            return redirect('detalle_factura', pk=factura.pk)

    else:
        factura_form = FacturaForm(instance=factura)
        detalle_form = DetalleFacturaForm(prefix='detalle')

    return render(request, 'factura/detalle_factura.html', {
        'factura': factura,
        'factura_form': factura_form,
        'detalle_form': detalle_form,
        'detalle': detalle,
    })

def eliminar_factura(request, pk):
    factura = get_object_or_404(Factura, pk=pk)
    factura.delete()
    return redirect('lista_facturas')

# miapp
def pagina_inicio(request):
    return render(request, 'menu/pagina_inicio.html')
