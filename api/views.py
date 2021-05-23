from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
import requests

global url;url = "https://coronavirus-19-api.herokuapp.com/countries"

class CovidAPI(generics.ListAPIView):
    #issue a get request using django rest framework
    def get(self, request, *args, **kwargs):
        # using a url of data loaded with covid data
        data = requests.get(url)
        #rendering as json and giving an error response
        try:
            data = data.json()
        except:
            return Response({'error': "Something's not right"})
        data = {"success": data}
        #render the request through django rest framwork for easy visualization,
        return Response(data)

class CountryView(generics.ListAPIView):
    def get(self, request, country="Kenya", *args, **kwargs):
        data = requests.get(url)
        try :
            data = data.json()
        except :
            return Response({"error": "Something's not right"})
        for value in data:
            if value.get("country").lower() == country.lower():
                data_for_countries = value
                break
            else :
                data_for_countries = "null"
                continue
        if data_for_countries == "null" :
            return Response({"error":"Country does not exist!"})
        data = {"Success" : data_for_countries}
        return Response(data)