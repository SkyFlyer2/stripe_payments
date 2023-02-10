from django.urls import path

from . import views

app_name = 'payments'

urlpatterns = [
    path('', views.main_page.as_view(), name='main'),
    path('buy/<int:id>/', views.item_purchase, name='item_purchase'),
    path('item/<int:id>/', views.item_detail, name='item_detail'),
    path('success/', views.order_success.as_view()),
    path('cancelled/', views.order_cancelled.as_view()),
]
