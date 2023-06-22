from django.shortcuts import render, get_object_or_404
from .models import Flight, Agency

def home(request):
    flights = Flight.objects.all()
    return render(request, 'index.html', {'flights': flights})

def overview(request):
    agencies = Agency.objects.all()
    return render(request, 'overview.html', {'agencies': agencies})

def detail(request, agency_id):
    agency = get_object_or_404(Agency, id=agency_id)
    return render(request, 'detail.html', {'agency': agency})




