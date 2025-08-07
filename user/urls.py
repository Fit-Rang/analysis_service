from django.urls import path
from . import views

urlpatterns = [
    path('profiles/', views.get_all_profiles, name='user-friends'),
]
