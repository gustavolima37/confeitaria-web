from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Endereco
from django.urls import reverse_lazy

# Create your views here.
class EnderecoListView(ListView):
    model = Endereco
    template_name = 'enderecos/lista.html'

class EnderecoDetailView(DetailView):
    model = Endereco
    template_name = 'enderecos/detalhe.html'

class EnderecoCreateView(CreateView):
    model = Endereco
    fields = ['cliente','rua', 'numero', 'bairro','complemento','cidade','estado','cep']
    template_name = "enderecos/form.html"
    success_url = reverse_lazy("lista_enderecos")

class EnderecoUpdateView(UpdateView):
    model = Endereco
    fields = ['cliente','rua', 'numero', 'bairro','complemento','cidade','estado','cep']
    template_name = "enderecos/form.html"
    seccess_url = reverse_lazy("lista_enderecos")

class EnderecoDeleteView(DeleteView):
    model = Endereco
    template_name = "enderecos/confirm_delete.html"
    success_url = reverse_lazy("lista_enderecos")