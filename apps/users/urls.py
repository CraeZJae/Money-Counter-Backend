from django.urls import path
from . import views
from .views import Signup

urlpatterns = [
    path("signup/", Signup.as_view() )
]