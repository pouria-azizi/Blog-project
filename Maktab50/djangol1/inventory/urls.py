from django.urls import path
from . import views

app_name = 'inventory'
urlpatterns = [
    path('product', views.ListProductView.as_view(), name='list'),
    path('list2/', views.products_list, name='list'),
    path('api/v1', views.ProductList.as_view()),
]
