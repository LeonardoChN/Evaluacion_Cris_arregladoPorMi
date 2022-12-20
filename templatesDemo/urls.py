"""templatesDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from firstApp import views


urlpatterns = [    
    path('admin/', admin.site.urls),
    path('', views.index),
    path('register/', views.register),
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    
    
    path('medicos/',views.medicos),
    path('pacientes/',views.pacientes),
    
    path('citas/',views.citas),
    
    
    path('agregarmedico/', views.agregarMedico),
    path('eliminarmedico/<int:id>', views.eliminarMedico),
    path('actualizarmedico/<int:id>', views.actualizarMedico),
    
    path('agregarpaciente/', views.agregarPaciente),
    path('eliminarpaciente/<int:id>', views.eliminarPaciente),
    path('actualizarpaciente/<int:id>', views.actualizarPaciente),
    
    path('agregarcita/', views.agregarCitas),
    path('eliminarcita/<int:id>', views.eliminarCitas),
    path('actualizarcita/<int:id>', views.actualizarCitas),
]
