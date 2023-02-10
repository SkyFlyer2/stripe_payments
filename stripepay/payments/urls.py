from django.urls import path

from . import views

app_name = 'payments'

urlpatterns = [
    path('', views.MainPage.as_view(), name='main'),
    path('buy/<int:id>/', views.item_purchase, name='item_purchase'),
    path('item/<int:id>/', views.item_detail, name='item_detail'),
    path('success/', views.SuccessView.as_view()),
    path('cancelled/', views.CancelledView.as_view()),
#    path('create-checkout-session/', views.create_checkout_session),
]
