from . import views
from django.urls import path

app_name = 'superheroes'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:superhero_id>/', views.details, name='details'),
    path('new_superhero/', views.create, name='create_superhero')
]