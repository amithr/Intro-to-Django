from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from .models import Guest
from .forms import GuestForm

def index(request):
    # Create Guest here
    form = GuestForm()
    context = {'form':form}
    return render(request, 'guests/index.html', context)

def create(request):
    if request.method == 'POST':
        form = GuestForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email_address = form.cleaned_data['email_address']
            message = form.cleaned_data['message']
            guest = Guest(name=name, email_address=email_address, message=message)
            guest.save()
    return redirect('/guests/list/')
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
    return redirect('/guests/list/')

