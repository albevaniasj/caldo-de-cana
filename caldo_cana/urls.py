from django.urls import path
from .views import (
    ClienteListView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView,
    PedidoListView, PedidoCreateView, PedidoUpdateView, PedidoDeleteView
)

urlpatterns = [
    
    path('clientes/', ClienteListView.as_view(), name='cliente-list'),
    path('clientes/novo/', ClienteCreateView.as_view(), name='cliente-create'),
    path('clientes/<int:pk>/editar/', ClienteUpdateView.as_view(), name='cliente-update'),
    path('clientes/<int:pk>/deletar/', ClienteDeleteView.as_view(), name='cliente-delete'),

    
    path('pedidos/', PedidoListView.as_view(), name='pedido-list'),
    path('pedidos/novo/', PedidoCreateView.as_view(), name='pedido-create'),
    path('pedidos/<int:pk>/editar/', PedidoUpdateView.as_view(), name='pedido-update'),
    path('pedidos/<int:pk>/deletar/', PedidoDeleteView.as_view(), name='pedido-delete'),
]
