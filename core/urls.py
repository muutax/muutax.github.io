"""gw URL Configuration

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
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    #path('', views.home, name='home'),
    #path('detail/<int:id>', views.detail_page, name='detail_page'),
    path('', views.WorkListView.as_view(), name='work'),
    path('detail/<int:pk>', views.WorkDetailView.as_view(), name='detail_page'),
    path('edit-page', views.RecordCreateView.as_view(), name='edit_page'),
    path('update-page/<int:pk>', views.RecordUpdateView.as_view(), name='update_page'),
    #path('delete-page/<int:pk>', views.RecordDeleteView.as_view(), name='delete_page'),
    path('delete-page/<int:id>', views.delete_page, name='delete_page'),
    path('login', views.LoginView.as_view(), name='login_page'),
    path('logout', views.Logout.as_view(), name='logout_page'),
    #path('register', views.RegisterUserView.as_view(), name='register_page'),
]