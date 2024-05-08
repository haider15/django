# hotel/views.py
from django.shortcuts import render
from .models import Hotel

def hotel_list(request):
    if request.method == 'GET':
        hotels = Hotel.objects.all()
        return render(request, 'hotel_list.html', {'hotels': hotels})
