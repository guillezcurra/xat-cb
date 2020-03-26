from django.shortcuts import render, redirect, reverse
from .models import Room

# Create your views here.
# vista principal
from django.contrib.auth import get_user
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views import View

from django.contrib.auth import login, authenticate

from chat.forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('inici')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})

def home(request):
    return render(request, 'chat/inici.html', {})

@login_required
def index(request):
    usuari = get_user(request)

    return render(request, 'chat/index.html', {
    'usuari' : usuari,
    })

@login_required
def room(request, room_name):
    # If the room with the given label doesn't exist, automatically create it
    # upon first visit (a la etherpad).
    room, created = Room.objects.get_or_create(label=room_name)
    usuari = get_user(request)
    messages = reversed(room.messages.order_by('-timestamp')[:50])

    if room_name == 'barrus':
      val = 'Barrufets'
    elif room_name == 'tois':
      val = 'Tois i Daines'
    elif room_name == 'ring':
      val = 'Ràngers i Noies Guia'
    elif room_name == 'pic':
        val = 'Pioners i Caravel·les'
    else:
      val = 'Truc'
    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'nom_unitat': val,
        'messages':messages,
        'usuari' : usuari,
    })
