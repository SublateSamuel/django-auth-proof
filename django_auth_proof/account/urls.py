from django.urls import path
from django.views.generic.base import RedirectView

from django_auth_proof.account.views import UserCreateView, UserUpdateView, LoginView, UserProfileView, UserLogoutView


app_name = 'account'

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='account:login')),
    path('login', LoginView.as_view(), name='login'),
    path('create/', UserCreateView.as_view(), name='user-create'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='user-update'),
    path('profile/<str:username>/', UserProfileView.as_view(), name='profile'),
]
