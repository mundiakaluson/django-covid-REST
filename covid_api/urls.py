from django.contrib import admin
from django.urls import path
from api import views

#render to the 'api' view class
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.CovidAPI.as_view()),
    path("api/<slug:country>/",views.CountryView.as_view()),
]
