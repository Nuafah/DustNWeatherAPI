from django.shortcuts import render, HttpResponse
from .models import BangkokDust, BangkokWeather


# Create your views here.
def index(request):
    dust = BangkokDust.objects.all()
    weather = BangkokWeather.objects.all()
    return render(request, "index.html", {"dust": dust,
                                          "weather": weather})


def detail(request, id):
    dust = BangkokDust.objects.all()
    weather = BangkokWeather.objects.all()
    return render(request, "detail.html", {"dust": dust,
                                           "weather": weather})
