from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from .models import Guest

def index(request):
    # Create Guest here
    return render(request, 'guests/index.html')

def create(request):
    guest = Guest(name="Jack", email_address="jack@gmail.com", message="OK")
    guest.save()
    return redirect('guest_list')
    # Redirect to guest list

def list(request):
    guests = Guest.objects.all()
    context = {'guest_list':guests}
    return render(request, 'guests/guest_list.html', context)

def individual(request, id):
    guest = Guest.objects.get(id=id)
    context = {'guest':guest}
    return render(request, 'guests/guest_profile.html', context)

def delete(request, id):
    guest = Guest.objects.get(id=id)
    guest.delete()
    return redirect('guest_list')

