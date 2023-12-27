from django.urls import path
from .views import pagina_inicio
from .views import (
    lista_productos, detalle_producto, nuevo_producto, editar_producto, eliminar_producto, lista_clientes,
    detalle_cliente, nuevo_cliente, editar_cliente, eliminar_cliente, crear_factura, editar_factura, lista_facturas,
    detalle_factura, eliminar_factura
)

urlpatterns = [
    path('', pagina_inicio, name='pagina_inicio'),
    # URLs para los productos
    path('productos/', lista_productos, name='lista_productos'),
    path('producto/<int:pk>/', detalle_producto, name='detalle_producto'),
    path('producto/nuevo/', nuevo_producto, name='nuevo_producto'),
    path('producto/editar/<int:pk>/', editar_producto, name='editar_producto'),
    path('producto/eliminar/<int:pk>/', eliminar_producto, name='eliminar_producto'),
    
    # URLs para los clientes
    path('clientes/', lista_clientes, name='lista_clientes'),
    path('cliente/<int:pk>/', detalle_cliente, name='detalle_cliente'),
    path('cliente/nuevo/', nuevo_cliente, name='nuevo_cliente'),
    path('cliente/editar/<int:pk>/', editar_cliente, name='editar_cliente'),
    path('cliente/eliminar/<int:pk>/', eliminar_cliente, name='eliminar_cliente'),
    
    # URLs para facturas
    path('facturas/', lista_facturas, name='lista_facturas'),
    path('facturas/<int:pk>/', detalle_factura, name='detalle_factura'),  
    path('facturas/nueva/', crear_factura, name='crear_factura'),
    path('facturas/editar/<int:pk>/', editar_factura, name='editar_factura'),
    path('facturas/eliminar/<int:pk>/', eliminar_factura, name='eliminar_factura'),
    
]
