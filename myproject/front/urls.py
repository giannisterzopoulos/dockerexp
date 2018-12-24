from django.urls import path, re_path
from myproject.front import views


app_name = 'front'

urlpatterns = [
    path('', views.home, name='home'),
]
