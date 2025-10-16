from django.urls import path
from usuarios.views import renderizar_index

urlpatterns = [
    path('', renderizar_index, name="index"),
]