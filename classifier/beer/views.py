from django.http import HttpResponse
from django.shortcuts import render
from .models import Styles
from .forms import BeerForm

def home(request):
    return render(request, 'beer/dashboard.html')

def results(request):
    context = {}
    form = BeerForm(request.POST)
    context['ibu'] = form.data['IBU']
    context['srm'] = form.data['SRM']
    context['og'] = form.data['OG']
    context['fg'] = form.data['FG']
    context['abv'] = form.data['ABV']

    return render(request, 'beer/results.html', context)
    # styles = Styles.objects.all()

    