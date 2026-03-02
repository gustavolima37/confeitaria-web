from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Pedido
# Create your views here.

class PedidoListView(ListView):
    model = Pedido
    template_name = 'pedidos/lista_pedidos.html'
    context_object_name = 'pedidos'

class PedidoDetailView(DetailView):
    model = Pedido
    template_name = 'pedidos/detalhe_pedido.html'
       
class PedidoCreateView(CreateView):
    model = Pedido
    fields = ['cliente', 'cpf_cliente', 'produto', 'quantidade','valor_encomenda','forma_pagamento','data_pedido','data_entrega']
    template_name = 'pedidos/form.html'
    success_url = reverse_lazy("lista_pedidos")

class PedidoUpdateView(UpdateView):
    model = Pedido
    template_name = 'pedidos/form.html'
    fields = ['cliente', 'cpf_cliente', 'produto', 'quantidade','valor_encomenda','forma_pagamento','data_pedido','data_entrega']
    success_url = reverse_lazy("lista_pedidos")

class PedidoDeleteView(DeleteView):
    model = Pedido
    template_name = 'pedidos/confirm_delete.html'
    success_url = reverse_lazy("lista_pedidos")
