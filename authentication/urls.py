from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path('register/', views.registration, name="registration"),
    path('logout/', views.logout_view, name="logout"),
]
