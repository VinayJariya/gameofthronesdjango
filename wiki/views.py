from django.shortcuts import render, get_object_or_404
from .models import House, Character

def index(request):
    houses = House.objects.all()
    return render(request, 'wiki/index.html', {'houses': houses})

def detail(request, house_id):
    house = get_object_or_404(House, pk=house_id)
    return render(request, 'wiki/detail.html', {'house': house,})
