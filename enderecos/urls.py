
from django.urls import path
from .views import EnderecoListView, EnderecoDetailView, EnderecoCreateView, EnderecoUpdateView, EnderecoDeleteView

urlpatterns = [
    path('', EnderecoListView.as_view(), name="lista_enderecos"),
    path('<int:pk>/', EnderecoDetailView.as_view(), name="detalhe_enderecos"),
    path('novo/', EnderecoCreateView.as_view(), name="enderecos_novo"),
    path('<int:pk>/editar/', EnderecoUpdateView.as_view(), name="enderecos_editar"),
    path('<int:pk>/deletar/', EnderecoDeleteView.as_view(), name="Enderecos_deletar"),
    path('novo/', EnderecoCreateView.as_view(), name='criar_endereco'),
]