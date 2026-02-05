from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Produto
# Create your views here.

class ProdutoListView(ListView):
    model = Produto
    template_name = 'produtos/lista.html'

class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'produtos/detalhe.html'
       
class ProdutoCreateView(CreateView):
    model = Produto
    fields = ['nome', 'descricao', 'preco', 'disponibilidade', 'quantidade']
    template_name = 'produtos/form.html'
    success_url = reverse_lazy("lista_produtos")

class ProdutoUpdateView(UpdateView):
    model = Produto
    template_name = 'produtos/form.html'
    fields = ['nome', 'descricao', 'preco', 'disponibilidade', 'quantidade']
    success_url = reverse_lazy("lista_produtos")

class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'produtos/confirm_delete.html'
    success_url = reverse_lazy("lista_produtos")