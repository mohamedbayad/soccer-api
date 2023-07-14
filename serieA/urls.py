from django.urls import path
from .views import SerieA

urlpatterns = [
    path('', SerieA.as_view(), name="main"),
    path('<str:lan>/', SerieA.as_view(), name="main"),
    path('<str:lan>/<str:years>/', SerieA.as_view(), name="main"),
]