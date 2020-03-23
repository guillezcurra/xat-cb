from django.shortcuts import render, redirect, reverse
from .models import Room

# Create your views here.
# vista principal

from django.contrib.auth.forms import UserCreationForm

from django.views import View

class RegisterView(View):
    def get(self, request):
        return render(request, 'registration/register.html', { 'form': UserCreationForm() })

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(reverse('login'))

        return render(request, 'registration/register.html', { 'form': form })

def home(request):
    return render(request, 'chat/inici.html', {})

def index(request):

    return render(request, 'chat/index.html', {})

def room(request, room_name):
    # If the room with the given label doesn't exist, automatically create it
    # upon first visit (a la etherpad).
    room, created = Room.objects.get_or_create(label=room_name)

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
    })
