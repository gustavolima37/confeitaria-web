from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Cliente
from django.urls import reverse_lazy

# Create your views here.
class ClienteListView(ListView):
    model = Cliente
    template_name = 'clientes/lista.html'

class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'clientes/detalhe.html'

class ClienteCreateView(CreateView):
    model = Cliente
    fields = ['nome', 'telefone', 'email']
    template_name = "clientes/form.html"
    success_url = reverse_lazy("lista_clientes")

class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = ['nome', 'telefone', 'email']
    template_name = "clientes/form.html"
    seccess_url = reverse_lazy("lista_clientes")

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = "clientes/confirm_delete.html"
    success_url = reverse_lazy("lista_clientes")