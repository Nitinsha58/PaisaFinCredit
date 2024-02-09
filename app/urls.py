from django.urls import path
from .views import register , login , changePassword , address , bankDetail


urlpatterns = [
    path("", register, name="register"),
    path("login/",login, name="login"),
    path("changepassword/",changePassword, name="changepassword"),
    path("address/",address, name="address"),
    path("bank/",bankDetail, name="bank"),
]