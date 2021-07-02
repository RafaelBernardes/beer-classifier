from django.http import HttpResponse
from django.shortcuts import render
from .models import Styles
from .forms import BeerForm
import pandas as pd


def home(request):
    return render(request, 'beer/dashboard.html')

def results(request):
    context = {}
    form = BeerForm(request.POST)
    ibu = form.data['IBU']
    srm = form.data['SRM']
    og = form.data['OG']
    fg = form.data['FG']
    abv = form.data['ABV']

    # Busca os dados do banco
    df = pd.read_json("styles.json")

    # Exemple
    ## Create Object
    myBeer = Styles.Selector(df)
    
    # Define variable values
    myBeer.setVariable('ibu', int(ibu))
    myBeer.setVariable('srm', int(srm))
    myBeer.setVariable('og', int(og))
    myBeer.setVariable('fg', int(fg))
    myBeer.setVariable('abv', float(abv))
    
    # Get Possible Classes and its Proabilities and Frequencies
    # Run -> myBeer.getPossibilities(True) to get JSON Response
    context['results'] = myBeer.getPossibilities(True)

    return render(request, 'beer/results.html', context)
    

    