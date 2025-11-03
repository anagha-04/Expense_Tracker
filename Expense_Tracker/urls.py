"""
URL configuration for Expense_Tracker project.

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
from user_app.views import *
from expense_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',RegisterView.as_view(),name ='signup'),
    path('login/',LoginView.as_view(),name ='login'),
    path('logout/',LogoutView.as_view(),name ='logout'),
    path('add_expense/',Add_Expense_View.as_view(),name='expense_add'),
    path('list/',ExpenseList.as_view(),name="expense_list"),
    path('update/<int:pk>',ExpenseUpdate.as_view(),name='expense_update'),
    path("",BaseView.as_view(),name="home"),
    path('delete/<int:pk>',ExpenseDelete.as_view(),name='expense_delete'),
    path('search/',ExpenseSearchView.as_view(), name='search'),

    
]
