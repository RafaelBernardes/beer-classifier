from django import forms

class BeerForm(forms.Form):
    IBU = forms.DecimalField(max_digits=5, decimal_places=3, label='IBU')
    SRM = forms.DecimalField(max_digits=5, decimal_places=3, label='SRM')
    OG = forms.DecimalField(max_digits=5, decimal_places=3, label='OG')
    FG = forms.DecimalField(max_digits=5, decimal_places=3, label='FG')
    ABV = forms.DecimalField(max_digits=5, decimal_places=3, label='ABV')