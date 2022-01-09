from django.urls import path
from firstapp import views

urlpatterns = [
    path('contact/', views.contact_list),
    path('contact/<int:pk>/', views.contact_detail),
  
]