from django.shortcuts import render

from .models import VideoGame

def index(request):
    games = VideoGame.objects.all()
    return render(request, 'games/index.html', {'games': games})
