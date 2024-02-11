from django.urls import path
from .views import (register_user, 
                    login_user, 
                    changePassword, 
                    address, 
                    bankDetail, 
                    forgot_password, 
                    logout_user,
                    index)

urlpatterns = [
    path("", index, name="home"),
    path("register/", register_user, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("forgotpassword/", forgot_password, name="forgotpassword"),
    path("changepassword/",changePassword, name="changepassword"),
    path("address/",address, name="address"),
    path("bank/",bankDetail, name="bank"),
]