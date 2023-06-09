from django.urls import path
from . import views
from .views import Signup

urlpatterns =[
    path('signin/', views.UserSignIn.as_view(), name='user_sign_in'),
    path('signup/', views.UserSignUp.as_view(), name='user_sign_up'),
    path('profile/', views.UserProfile.as_view(), name='user_profile'),
    path('update/<int:id>/', views.UpdateProfile.as_view(), name='update_user_profile'),
    path('update/<int:id>/budget/', views.UpdateBudget.as_view(), name='update_user_budget'),
]