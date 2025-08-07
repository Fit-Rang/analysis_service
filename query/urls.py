from django.urls import path
from .views import get_verdict

urlpatterns = [
    path('verdict/', get_verdict, name='get-verdict'),
]
