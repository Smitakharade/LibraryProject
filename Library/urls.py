"""Library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from firstapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('show_active_books/', views.show_books, name='show_active_books'),
    path('update_books/<int:id>/', views.update_books, name='update_books'),
    path('delete_books/<int:id>/', views.delete_books, name='delete_books'),
    path('soft_delete_books/<int:id>/', views.soft_delete_books, name='soft_delete_books'),
    path('show_inactive_books/', views.show_inactive_books, name='show_inactive_books'),
    path('restore_books/<int:id>/', views.restore_books, name='restore_books'),
]
