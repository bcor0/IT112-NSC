from django.shortcuts import render, get_object_or_404
from .models import VideoGame

def game_list(request):
    games = VideoGame.objects.all()
    return render(request, 'games/game_list.html', {'games': games})

def game_detail(request, pk):
    game = get_object_or_404(VideoGame, pk=pk)
    return render(request, 'games/game_detail.html', {'game': game})
