from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
    path('store/', views.store, name="store"),
    path('update_item/', views.updateItem, name='update_item'),
    path('product_detail/<int:product_id>', views.product_details, name='product_detail')
]