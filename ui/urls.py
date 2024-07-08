from django.urls import path
from ui.views import home

urlpatterns = [
    path('', home , name='home'),
]
