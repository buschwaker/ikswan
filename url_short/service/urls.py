from django.urls import path


from . import views

app_name = 'service'

urlpatterns = [
    path('', views.index, name='main_page'),
    path('list/', views.urls_list, name='urls_list')
]
