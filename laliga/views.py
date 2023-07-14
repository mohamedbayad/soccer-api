from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from main.data import FootBall
from main.tools import url

# Create your views here.

class LaLiga(APIView):

    def get(self, request, *args, **kwargs):
        try:
            if kwargs.get('lan') == "en":
                lang = "int"
            else:
                lang = kwargs.get("lan")
            if kwargs.get("lan") is not None :
                football = FootBall(url=url(lang=lang, country="spain", league="primera-division"))
                if kwargs.get("years") is not None:
                    football = FootBall(url=url(lang=lang, years=kwargs.get("years"), country="spain", league="primera-division"))
                else:
                    football = FootBall(url=url(lang=lang, country="spain", league="primera-division"))
            else:
                football = FootBall(url=url(country="spain", league="primera-division"))

            football.finishData = dict()
            all_data = football.getData() 
            return Response(all_data, status=status.HTTP_200_OK)
        except:
            return Response({"error" : "Page Not Found"}, status=status.HTTP_404_NOT_FOUND)