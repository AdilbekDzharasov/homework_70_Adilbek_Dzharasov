from django.urls import path
from accounts.views import LoginView, logout_view
from accounts.views import RegisterView


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('create/', RegisterView.as_view(), name='register'),
    path('logout/', logout_view, name='logout')
]

