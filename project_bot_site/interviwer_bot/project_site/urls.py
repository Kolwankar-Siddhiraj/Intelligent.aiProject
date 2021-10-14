from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login_or_signup', views.login_or_signup, name='login_or_signup'),
    path('login', views.login, name='login'),
    path('create_account', views.create_account, name='create_account'),
    path('otp_verification', views.otp_verification, name='otp_verification'),
    path('forgot_password', views.forgot_password, name='forgot_password'),
    path('reset_password', views.reset_password, name='reset_password'),
    

    # try new feature by pankaj
    path('new_feature_1', views.new_feature_1, name='new_feature_1'),
    path('f2', views.f2, name='f2'),
    path('f3', views.f3, name='f3'),
    path('f4', views.f4, name='f4'),
    path('f5', views.f5, name='f5'),

]


