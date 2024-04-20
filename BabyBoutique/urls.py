from django.urls import path
from . import views
from .views import home_view
from django.contrib.auth.views import LoginView
from django.urls import path
from .views import AboutUsView
from .views import ContactUsView

urlpatterns = [
    path('', views.home_view, name='home'),
    path('shop', views.shop, name='shop'),
    path('product_view/', views.product_view, name='product_view'),
    path('logout/', views.logout_user, name='logout'),
    path('adminclick/', views.adminclick_view, name='adminclick'),
    # path('afterlogin/', views.adminlogin_view, name='afterlogin'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-login/admin-dashboard',views.admin_dashboard,name='admin-dashboard'),
    path('about-us/', AboutUsView.as_view(), name='about-us'),  
    path('contact-us/', ContactUsView.as_view(), name='contact-us'),   
    path('cart/', views.cart_view, name='cart'), 
    path('add-to-cart/<int:pk>',views.add_to_cart_view,name='add-to-cart'),
    path('customer-address',views.customer_address_view,name='customer-address'),
    path('admin_add_product/', views.admin_add_product, name='admin_add_product'),
    path('payment/', views.payment, name='payment'), 
    path('process-payment/', views.process_payment, name='process-payment'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    # path('order/', views.OrderView.as_view(), name='order_view'),
    path('orders/', views.order_page, name='order_page'), 
    path('tracking/', views.track_shipment, name='tracking'),
    path('tracking/details/', views.tracking_details, name='tracking_details'),  
    path('add_tracking_details/', views.add_tracking_details, name='add_tracking_details'),
    path('delete-product/<int:pk>/', views.delete_product, name='delete-product'),
    # path('update-bus-list/<int:pk>/', views.update_bus_list_view, name='update-bus-list'),

    # Add other URL patterns as needed

   
      
      
]


