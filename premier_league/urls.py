from django.urls import path
from .views import PremierLeague

urlpatterns = [
    path('', PremierLeague.as_view(), name="main"),
    path('<str:lan>/', PremierLeague.as_view(), name="main"),
    path('<str:lan>/<str:years>/', PremierLeague.as_view(), name="main"),
]