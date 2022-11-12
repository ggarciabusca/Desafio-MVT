from django.urls import path
from app1.views import *


urlpatterns = [
    path('familiares/',listado_familiares,name="app1-listado_personas"),
    path('inicio/',inicio,name="app1-inicio")
]