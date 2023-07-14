from django.urls import path
from .views import LaLiga

urlpatterns = [
    path('', LaLiga.as_view(), name="laliga"),
    path('<str:lan>/', LaLiga.as_view(), name="laliga"),
    path('<str:lan>/<str:years>/', LaLiga.as_view(), name="laliga"),
]