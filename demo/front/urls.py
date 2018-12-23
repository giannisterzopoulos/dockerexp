from django.urls import path, re_path
from demo.front import views


app_name = 'front'

urlpatterns = [
    path('', views.home, name='home'),
]
