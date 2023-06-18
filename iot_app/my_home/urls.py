from django.urls import path
from .views import (LightStatus)

urlpatterns = [
    path('light_status', LightStatus.as_view()),
]
