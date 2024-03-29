from . import views
from django.urls import path

app_name = 'superheroes'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:superhero_id>/', views.details, name='details'),
    path('new_superhero/', views.create, name='create_superhero'),
    path('delete_superhero<int:id>/', views.delete, name='delete_superhero'),
    path('edit_superhero<int:id>/', views.edit, name='edit_superhero'),
    path('confirm_delete<int:id>/', views.confirm_delete, name='confirm_delete')
]