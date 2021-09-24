from django.urls import path

from .views import contacto_view, index_view

app_name = 'website'

urlpatterns = [
    path('', index_view, name='index'),
    path('contacto/', contacto_view, name='contacto'),
]
