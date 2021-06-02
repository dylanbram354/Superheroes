from . import views
from django.urls import path

app_name = 'superheroes'
urlpatterns = [
    path('', views.greeting, name='greeting')
]