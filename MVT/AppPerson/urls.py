from django.urls import path
from .views import *


urlpatterns = [
    path('', list_person),
    path('crear/', create_person, name='create_person'),
    path('eliminar/<id>', delete_person, name='delete_person'),
]
