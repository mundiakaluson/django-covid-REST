from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
import requests

global url

class CovidAPI(generics.ListAPIView):
    
    def get(self, request, *args, **kwargs):
        url = "https://coronavirus-19-api.herokuapp.com/countries"
        data = requests.get(url)

        try:
            data = data.json()
        except:
            return Response({'error': "Something's not correct"})
        data = {"success": data}
        return Response(data)