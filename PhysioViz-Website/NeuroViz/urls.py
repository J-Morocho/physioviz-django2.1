"""NeuroViz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from visualizations.views import subject_chart
from subjects.views import subject_detail_view
from subjects.views import subject_charts_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', subject_chart, name='home_view'),
    path('detail/', subject_detail_view, name='detail'),
    path('table/', subject_charts_view, name='data')
]
