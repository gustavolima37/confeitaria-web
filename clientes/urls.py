from django.urls import path
from .views import ClienteListView, ClienteDetailView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView

urlpatterns = [
    path('', ClienteListView.as_view(), name="lista_clientes"),
    path('<int:pk>/', ClienteDetailView.as_view(), name="detalhe_clientes"),
    path('novo/', ClienteCreateView.as_view(), name="clientes_novo"),
    path('<int:pk>/editar/', ClienteUpdateView.as_view(), name="clientes_editar"),
    path('<int:pk>/deletar/', ClienteDeleteView.as_view(), name="clientes_deletar"),
]