from django.urls import path
from .views import (
    home_view,
    SaleListView,
    sale_list_view,
    sale_detail_view,
    SaleDetailView,
    )


app_name = 'sales'

urlpatterns = [
    path('', home_view, name = 'home'),
    path('sales/', sale_list_view, name = 'list'),
    path('sales/<pk>/', sale_detail_view, name = 'detail'),
]