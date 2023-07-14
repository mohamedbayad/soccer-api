from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .data import FootBall
from .tools import url



# Create your views here.
class Main(APIView):
    
    def get(self, request,*args, **kwargs):
        major_leagues = [
                {
                    "country" : "england",
                    "league" : "premier-league" # Done
                },
                {
                    "country" : "italy",
                    "league" : "serie-a" # Done
                },
                {
                    "country" : "spain",
                    "league" : "primera-division" # Done
                },
                {
                    "country" : "germany",
                    "league" : "bundesliga"
                },
                {
                    "country" : "france",
                    "league" : "ligue-1"
                },
            ]
        languages = [
                {
                    'lang' : 'English',
                    'short-lang' : 'en',
                },
                {
                    'lang' : 'Arabic',
                    'short-lang' : 'ar',
                },
                {
                    'lang' : 'Français',
                    'short-lang' : 'fr',
                },
                {
                    'lang' : 'Türkçe',
                    'short-lang' : 'tr',
                },
                {
                    'lang' : 'Japanese',
                    'short-lang' : 'jp',
                },
                {
                    'lang' : 'Español - Español',
                    'short-lang' : 'es',
                },
                {
                    'lang' : 'Italiano',
                    'short-lang' : 'it',
                },
                {
                    'lang' : 'Deutsch',
                    'short-lang' : 'de',
                },
            ]
        message = {
            "alert" : "Just instructions on what information is available"
        }
        settings : dict = {}
        settings.update({
                'message' : message,
                'languages' : languages,
                'major_leagues' : major_leagues,
            })

        # football = FootBall(url=url(lang=lan, years=years, country=country, league=league))
        # football.finishData = dict()
        # all_data = football.getData() 
        return Response(settings)
        
