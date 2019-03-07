from django.shortcuts import render
from django.http import HttpResponse
from .forms import SuperHeroForm, SuperHeroModel
# Create your views here.



def index(request):
    return render(request,'SuperHeroApp/index.html')


def HeroForm(request):
    return render(request,'SuperHeroApp/heroForm.html',{'form':SuperHeroForm})


def thankYou(request):
    formToSubmit = SuperHeroForm(request.POST)
    if formToSubmit.is_valid():
        formToSubmit.save()
        return render(request,'SuperHeroApp/ThankYou.html')
    else:
        return render(request,'SuperHeroApp/heroForm.html',{'form':formToSubmit})