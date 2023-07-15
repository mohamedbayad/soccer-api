from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from main.data import FootBall
from main.tools import url


import datetime

# Create your views here.

class Bundesliga(APIView):

    dt_defualt = datetime.datetime.now()
    years = f"{dt_defualt.strftime('%Y')}{int(dt_defualt.strftime('%Y')) + 1}"

    def get(self, request, *args, **kwargs):
        try:
            if kwargs.get('lan') == "en":
                lang = "int"
            else:
                lang = kwargs.get("lan")
            if kwargs.get("lan") is not None :
                football = FootBall(url=url(lang=lang, country="germany", league="bundesliga"))
                if kwargs.get("years") is not None:
                    football = FootBall(url=url(lang=lang, years=kwargs.get("years"), country="germany", league="bundesliga"))
                else:
                    football = FootBall(url=url(lang=lang, country="germany", league="bundesliga"))
            else:
                football = FootBall(url=url(country="germany", league="bundesliga"))

            football.finishData = dict()
            if kwargs.get("years") is not None:
                all_data = football.getData(date=kwargs.get("years")) 
            else:
                all_data = football.getData(date=self.years) 
            return Response(all_data, status=status.HTTP_200_OK)
        except:
            return Response({"error" : "Page Not Found"}, status=status.HTTP_404_NOT_FOUND)