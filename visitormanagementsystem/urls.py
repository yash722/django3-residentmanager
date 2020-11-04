"""visitormanagementsystem URL Configuration

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
from django.urls import path, include
from management_system import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    # Residents going out
    path('outgoingentry/', views.outgoing_entryform, name='outgoingentryform'),
    path('outgoingentrylist/', views.outgoing_list, name='outgoing_list'),
    path('outgoingentrylist/<int:person_pk>',
         views.outgoing_info, name='outgoing_info'),
    path('outgoingentrylist/<int:person_pk>/returned',
         views.visitorreturn, name='visitorreturn'),
    path('returned/', views.returned, name='returned'),
    path('outgoingentrylist/<int:person_pk>/positive',
         views.positive, name='positive'),
    path('isolated/', views.isolate, name="isolated"),
    path('isolateresident/', views.isolate_entryform, name='isolate_entryform'),
    path('isolated/<int:person_pk>/remove',
         views.isolated_remove, name="isolated_remove"),
    # Visitor coming in
    path('visitorentry/', views.visitor_entryform, name='visitorentryform'),
    path('visitorentrylist/', views.visitor_list, name='visitor_list'),
    path('visitorentrylist/<int:person_pk>',
         views.visitor_info, name='visitor_info'),
    path('visitorentrylist/<int:person_pk>/departed',
         views.visitordepart, name='visitordepart'),
    path('departed/', views.departed, name='departed'),

    # Authentication System
    path('auth/', include('accounts.urls'))
]
