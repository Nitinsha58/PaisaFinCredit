from django.urls import path
from .views import register_user, login_user, changePassword , address , bankDetail


urlpatterns = [
    path("register/", register_user, name="register"),
    path("login/", login_user, name="login"),
    path("changepassword/",changePassword, name="changepassword"),
    path("address/",address, name="address"),
    path("bank/",bankDetail, name="bank"),
]