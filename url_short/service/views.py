from django.shortcuts import render
from django.contrib.auth.decorators import login_required


from .forms import UrlForm
from .models import URL


@login_required
def index(request):
    """Функция-представление,
    записывает в БД ссылки, выводит пользователю сокращенную ссылку
    Доступно только аутентифицированным пользователям
    """
    form = UrlForm()
    sent_url = False
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            full_url = form.cleaned_data['full_url']
            try:
                url = URL.objects.get(full_url=full_url, user=request.user)
            except URL.DoesNotExist:
                new = form.save(commit=False)
                new.user = request.user
                new.save()
                url = URL.objects.get(full_url=full_url, user=request.user)
            sent_url = url
    return render(
        request, 'service/index.html', {'form': form, 'sent_url': sent_url}
    )


@login_required
def urls_list(request):
    """Функция-представление, выводит все ссылки пользователя из БД,
    доступно только пользователям, наделенным правами администратора
    """
    user = request.user
    url_list = user.urls.all()
    context = {
        'url_list': url_list,
    }
    return render(request, 'service/urls_list.html', context)
