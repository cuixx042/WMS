"""WMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path

from .views import (HelloWorld, WafersView, WaferDetailView, WaferCreateView, 
                    WaferUpdateView, WaferDeleteView, UserDetailView, EditProfile)

urlpatterns = [
	path('helloworld', HelloWorld.as_view(), name='helloworld'),
	path('', WafersView.as_view(), name='wafers'),
	path('wafer/<int:pk>/', WaferDetailView.as_view(), name='wafer_detail'),
	path('wafer/new/', WaferCreateView.as_view(), name='make_wafer'),
    path('wafer/update/<int:pk>/', WaferUpdateView.as_view(), name='wafer_update'),
    path('wafer/delete/<int:pk>/', WaferDeleteView.as_view(), name='wafer_delete'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('edit_profile/<int:pk>/', EditProfile.as_view(), name='edit_profile'),
]
