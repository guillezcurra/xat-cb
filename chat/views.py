from django.shortcuts import render

# Create your views here.
# vista principal
def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
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
        'nom_unitat': val
    })