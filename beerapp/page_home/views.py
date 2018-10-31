from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.views import View
from beerapp.db_models.t_beers.models import BeerApp
from .forms import PersonalDataForm
from django.conf import settings
class HomeView(View):

    def get(self, request):
        #Render data from google map api and ipstack api!
        response = requests.get('http://api.ipstack.com/check?access_key='+settings.ACCESS_KEY+'&format=1')
        geodata = response.json()
        context= {
            "ip" : geodata['ip'],
            'country': geodata['country_name'],
            'latitude': geodata['latitude'],
            'longitude': geodata['longitude'],
            'api_key':settings.GOOGLE_API_KEY,
        }
        return render(request, "myhome.html", context)

class DetailView(View):
    def get(self, request, beerid):
        #Variable used to see if given record exists
        notexist=""

        try:
            beerobj = BeerApp.objects.get(pk=beerid)
            beername = beerobj.beername
            remarks = beerobj.comments
            beer_img_name = beerobj.beer_img_name
            
        #If it does not exist, set all values to blank and nonexist flag to true
        except:
            beerobj =""
            remarks=""
            beername=""
            beer_img_name=""
            notexist="True"
        

        
        context={
            'beername':beername,
            'remarks': remarks,
            'beerobj': beerobj,
            'beer_img_name':beer_img_name,
            'notexist': notexist,
            }
        
        return render(request, "beerdetail.html", context)
