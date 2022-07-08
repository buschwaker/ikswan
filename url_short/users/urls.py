from django.urls import path
from django.contrib.auth import views as v
from django.contrib.auth.decorators import user_passes_test

from . import views

app_name = 'users'

urlpatterns = [
    path(
        'logout/',
        v.LogoutView.as_view(),
        name='logout'
    ),
    path(
        'login/',
        v.LoginView.as_view(
            template_name='users/signup.html', extra_context={'urls': ['/', '/list/']}
        ),
        name='login'
    ),
    path(
        'signup/',
        user_passes_test(lambda u: u.is_staff)(views.SignUp.as_view()),
        name='signup'
    ),
]
