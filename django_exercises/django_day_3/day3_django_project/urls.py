"""
URL configuration for day3_django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from day3_app.views import ex1, ex2, forms_ex1, forms_ex2

urlpatterns = [
    path("admin/", admin.site.urls),
    path("exercise1/", ex1),
    path("exercise1/<int:start>/", ex1),
    path("exercise1/<int:start>/<int:end>/", ex1),
    path("exercise2/<int:width>/<int:height>/", ex2),
    path("forms/exercise1/", forms_ex1),
    path("forms/exercise2/", forms_ex2),
]
