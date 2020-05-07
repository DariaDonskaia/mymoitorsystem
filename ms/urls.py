from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('node/<int:id_node>/', views.node, name='node_adr'),
    path('node_list/', views.nodes, name='node_list'),
    path('add_node/', views.add_node, name='add_node'),
    path('gateway_list/', views.gateways, name='gateway_list'),
    path('add_gateway/', views.add_gateway, name='add_gateway'),
]
