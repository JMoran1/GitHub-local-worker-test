from django.urls import path
from main import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path('logout/', views.logout_user, name='logout'),
]