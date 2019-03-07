from django.urls import  path
from . import views


urlpatterns = \
    [
        path('',views.index,name='index'),
        path('HeroForm/',views.HeroForm,name='HeroForm'),
        path('thankYou/',views.thankYou,name='thankYou'),
    ]