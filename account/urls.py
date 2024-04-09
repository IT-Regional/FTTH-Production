from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.login_view, name= 'index'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('adminpage/', views.admin, name='adminpage'),
    path('customer/', views.customer, name='customer'),
    path('employee/', views.employee, name='employee'),
    path('view_admins/', views.view_admins, name='view_admins'),
    path('register_customer/', views.register_customer,name='register_customer'),
    path('view_customers/', views.view_customers, name='view_customers'),
    path('view_customers/edit_customer/<int:customer_id>/', views.edit_customer, name='edit_customer'),
    path('view_customers/delete_customer/<int:customer_id>/', views.delete_customer, name='delete_customer'),
    path('view_customers/view_customer/<int:customer_id>/', views.view_customer, name='view_customer'),
]