from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register, name='register'),
    path("login/", views.login_user, name="login"),

    path('user/',views.after_login,name='after_login'),
]
