from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from datetime import date
import requests


# Create your views here.
class MatchDay(APIView):


    def get(self, request, *args, **kwargs):

        dateNow = date.today()
        if kwargs.get("lang") is not None:
            response = requests.get("https://www.goal.com/api/live-scores/refresh?edition={lan}&date={d}&tzoffset=60".format(d = dateNow, lan = kwargs.get("lang")))
            if kwargs.get("date") is not None:
                response = requests.get("https://www.goal.com/api/live-scores/refresh?edition={lan}&date={d}&tzoffset=60".format(d = kwargs.get("date"), lan = kwargs.get("lang")))
            else:
                response = requests.get("https://www.goal.com/api/live-scores/refresh?edition={lan}&date={d}&tzoffset=60".format(d = dateNow, lan = kwargs.get("lang")))

        else:
            response = requests.get("https://www.goal.com/api/live-scores/refresh?edition={lan}&date={d}&tzoffset=60".format(d = dateNow, lan = "en"))

        data : dict
        data = response.json()
        data.pop("__typename")
        return Response(data)

