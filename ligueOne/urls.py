from django.urls import path
from .views import LigueOne

urlpatterns = [
    path('', LigueOne.as_view(), name="LigueOne"),
    path('<str:lan>/', LigueOne.as_view(), name="LigueOne"),
    path('<str:lan>/<str:years>/', LigueOne.as_view(), name="LigueOne"),
]