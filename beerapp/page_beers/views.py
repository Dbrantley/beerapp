from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.views import View
from beerapp.db_models.t_beers.models import BeerApp
from .forms import PersonalDataForm
from .tables import BeerTable
from django_tables2 import RequestConfig

class BeersHomeView(View):

    def get(self, request):
        #If search result is blank then replace with empty string
        search_result = request.GET.get("beer_result","")

        """
        Check if something was inputted in search.
        If so, filter, if not, show all results!
        """
        if search_result:
            beer_data=BeerApp.objects.filter(beername__icontains=search_result)
        else:
            beer_data= BeerApp.objects.all()

        beer_table= BeerTable(data=beer_data)
        
        #Used so the table can be sorted appropiately
        RequestConfig(request).configure(beer_table)

        context= {
            "table" : beer_table,
            "search_result":search_result,
        }
        return render(request, "totalbeers.html", context)
