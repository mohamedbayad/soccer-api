from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from main.data import FootBall
from main.tools import url

# Create your views here.

class LigueOne(APIView):

    def get(self, request, *args, **kwargs):
        try:
            if kwargs.get('lan') == "en":
                lang = "int"
            else:
                lang = kwargs.get("lan")
            if kwargs.get("lan") is not None :
                football = FootBall(url=url(lang=lang, country="france", league="ligue-1"))
                if kwargs.get("years") is not None:
                    football = FootBall(url=url(lang=lang, years=kwargs.get("years"), country="france", league="ligue-1"))
                else:
                    football = FootBall(url=url(lang=lang, country="france", league="ligue-1"))
            else:
                football = FootBall(url=url(country="france", league="ligue-1"))

            football.finishData = dict()
            all_data = football.getData() 
            return Response(all_data, status=status.HTTP_200_OK)
        except:
            return Response({"error" : "Page Not Found"}, status=status.HTTP_404_NOT_FOUND)