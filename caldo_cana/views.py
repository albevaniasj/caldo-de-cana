from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from .models import Cliente, Pedido
from django.shortcuts import render


def home_view(request):
    return render(request, 'caldo_cana/home.html')



class ClienteListView(ListView):
    model = Cliente
    template_name = "caldo_cana/cliente_list.html"


class ClienteCreateView(CreateView):
    model = Cliente
    template_name = "caldo_cana/cliente_form.html"
    fields = ['nome', 'email']
    success_url = reverse_lazy('cliente-list')


class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = "caldo_cana/cliente_form.html"
    fields = ['nome', 'email']
    success_url = reverse_lazy('cliente-list')


class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = "caldo_cana/cliente_confirm_delete.html"
    success_url = reverse_lazy('cliente-list')



class PedidoListView(ListView):
    model = Pedido
    template_name = "caldo_cana/pedido_list.html"


class PedidoCreateView(CreateView):
    model = Pedido
    template_name = "caldo_cana/pedido_form.html"
    fields = ['cliente', 'descricao', 'preco']  
    success_url = reverse_lazy('pedido-list')


class PedidoUpdateView(UpdateView):
    model = Pedido
    template_name = "caldo_cana/pedido_form.html"
    fields = ['cliente', 'descricao', 'preco']  
    success_url = reverse_lazy('pedido-list')


class PedidoDeleteView(DeleteView):
    model = Pedido
    template_name = "caldo_cana/pedido_confirm_delete.html"
    success_url = reverse_lazy('pedido-list')
