from django.urls import path
from app import views

urlpatterns = [
    path('setcookie/', views.setcookie),
    path('getcookie/', views.getcookie),
    path('deletecookie/', views.deletecookie),
    path('setsession/', views.ses),
    path('getsession/', views.getses),
]
