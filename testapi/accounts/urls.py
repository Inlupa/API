from django.urls import path, include
from account.views import PasswordResetTokenView
from .views import *
app_name = 'accounts'
urlpatterns = [
    path(r"account/", include("account.urls")),
    path(r"account/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/", PasswordResetTokenView.as_view(),
        name="account_password_reset_token"),
    path(r"account/login/", LoginView.as_view(), name="account_login"),
    path(r"account/signup/", SignupView.as_view(), name="account_signup"),
    path(r"account/change/", change_password, name='change'),


]