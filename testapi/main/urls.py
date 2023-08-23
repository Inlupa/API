from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name='home'),
    path("users", users_in_db, name='users'),
]