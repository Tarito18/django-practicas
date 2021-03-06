"""proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from proyecto1.views import saludo, segunda_vista, dia_hoy, mi_nombre, primer_template #Importo el saludo que hice en views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/',saludo), #aqui, hago el nombre del url, y llamo a la vista, la cual es , saludo
    path('nashe/',segunda_vista),
    path('dias/',dia_hoy),
    path('nombre/<nombre>',mi_nombre),
    path('template/',primer_template),
  
]
