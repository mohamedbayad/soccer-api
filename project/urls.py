from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include("main.urls")),
    path('premier-league/', include("premier_league.urls")),
    path('la-liga/', include("laliga.urls")),
    path('serie-a/', include("serieA.urls")),
    path('bundesliga/', include("bundesliga.urls")),
    path('ligue-1/', include("ligueOne.urls")),
    path('match-day/', include("matchs.urls")),
]
