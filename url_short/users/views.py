from django.views.generic import CreateView

from django.urls import reverse_lazy

from .forms import SignUpForm


class SignUp(CreateView):
    """Класс-представление,
    Реализует создание нового пользователя
    Доступно только пользователям, наделенным правами администратора"""
    form_class = SignUpForm
    success_url = reverse_lazy('service:main_page')
    template_name = 'users/signup.html'
    extra_context = {'register': True}
