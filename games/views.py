
from django.http import JsonResponse
from .models import VideoGame
from django.views.decorators.csrf import csrf_exempt
import json

def get_all_games(request):
    if request.method == 'GET':
        games = list(VideoGame.objects.values())
        return JsonResponse(games, safe=False, content_type='application/json')

def get_single_game(request):
    if request.method == 'GET':
        game_id = request.GET.get('id')
        try:
            game = VideoGame.objects.get(id=game_id)
            return JsonResponse({
                'id': game.id,
                'title': game.title,
                'genre': game.genre,
                'release_year': game.release_year
            }, content_type='application/json')
        except VideoGame.DoesNotExist:
            return JsonResponse({'error': 'Game not found'}, content_type='application/json')

@csrf_exempt
def create_game(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            game = VideoGame.objects.create(
                title=data['title'],
                genre=data['genre'],
                release_year=data['release_year']
            )
            return JsonResponse({'success': 'Game created successfully'}, content_type='application/json')
        except Exception as e:
            return JsonResponse({'error': str(e)}, content_type='application/json')
