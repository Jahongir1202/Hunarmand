from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('product/<int:pk>/', views.product_detail, name='product_detail'),
    # path('order/<int:pk>/', views.order_product, name='order_product'),
    # path('contact/', views.contact, name='contact'),

    # 🆕 Custom admin panel
    path('admin/login/', views.admin_login, name='admin_login'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/logout/', views.admin_logout, name='admin_logout'),
]
