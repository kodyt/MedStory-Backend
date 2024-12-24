"""
URL configuration for api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from symptoms import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/get_symptoms/', views.get_symptoms, name='symptom'),
    path('api/add_general_symptom_log/', views.add_general_symptom_log, name='general_symptom_log'),
    path('api/add_numerical_symptom_log/', views.add_numerical_symptom_log, name='numerical_symptom_logging'),
    path('api/get_timeline_data/', views.get_timeline_data, name='timeline_data'),
]
