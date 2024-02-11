from django.urls import path
from .views import  login_views ,otp , register  ,send_otp


app_name='otptest'
urlpatterns = [
    path("login/",login_views,name="test_login"),
    path("register/",register,name="test_register"),
    path("otp/",login_views,name="test_otp"),
    

]