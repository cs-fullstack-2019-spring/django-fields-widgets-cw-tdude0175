from django.shortcuts import render
from django.http import HttpResponse
from .forms import SuperHeroForm, SuperHeroModel
# Create your views here.


#sends you to home page
def index(request):
    return render(request,'SuperHeroApp/index.html')

# Opens the form page
def HeroForm(request):
    return render(request,'SuperHeroApp/heroForm.html',{'form':SuperHeroForm})

# if the form is filled out right it will send otherwise it will return telling you want to fill out
def thankYou(request):
    formToSubmit = SuperHeroForm(request.POST)
    if formToSubmit.is_valid():
        formToSubmit.save()
        return render(request,'SuperHeroApp/ThankYou.html')
    else:
        return render(request,'SuperHeroApp/heroForm.html',{'form':formToSubmit})