from django.urls import path
from .views import MatchDay

urlpatterns = [
    path("", MatchDay.as_view(), name="match-day"),
    path("<str:lang>/", MatchDay.as_view(), name="match-day"),
    path("<str:lang>/<slug:date>/", MatchDay.as_view(), name="match-day"),
]