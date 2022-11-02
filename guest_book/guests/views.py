from django.shortcuts import render
from django.template import loader
from .models import Guest

def index(request):
    return render(request, 'guests/index.html')

def create_guest(request):
    return render(request, 'guests/create')

def view_guests(request):
    guests = Guest.objects.all()
    context = {'guest_list':guests}
    return render(request, 'guests/guest_list.html', context)

def view_individual_guest(request):
    return

def delete_guests(request):
    return

