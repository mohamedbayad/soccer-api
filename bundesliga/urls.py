from django.urls import path
from .views import Bundesliga

urlpatterns = [
    path('', Bundesliga.as_view(), name="Bundesliga"),
    path('<str:lan>/', Bundesliga.as_view(), name="Bundesliga"),
    path('<str:lan>/<str:years>/', Bundesliga.as_view(), name="Bundesliga"),
]