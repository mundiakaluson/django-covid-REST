from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
import requests

global url

class CovidAPI(generics.ListAPIView):
    #issue a get request using django rest framework
    def get(self, request, *args, **kwargs):
        # using a url of data loaded with covid data
        url = "https://coronavirus-19-api.herokuapp.com/countries"
        data = requests.get(url)
        #rendering as json and giving an error response
        try:
            data = data.json()
        except:
            return Response({'error': "Something's not correct"})
        data = {"success": data}
        #render the request through django rest framwork for easy visualization,
        return Response(data)