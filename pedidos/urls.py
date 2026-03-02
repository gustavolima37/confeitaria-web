from django.urls import path
from .views import PedidoListView, PedidoDetailView, PedidoCreateView, PedidoUpdateView, PedidoDeleteView  

urlpatterns = [
    path('', PedidoListView.as_view(), name='lista_pedidos'), 
    path('pedido/<int:pk>/', PedidoDetailView.as_view(), name='detalhe_pedido'),
    path('pedido/novo/', PedidoCreateView.as_view(), name='criar_pedido'),
    path('pedido/<int:pk>/editar/', PedidoUpdateView.as_view(), name='editar_pedido'), 
    path('pedido/<int:pk>/deletar/', PedidoDeleteView.as_view(), name='deletar_pedido'),     
]