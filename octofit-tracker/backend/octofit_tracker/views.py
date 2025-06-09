from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from pymongo import MongoClient
from django.conf import settings
from rest_framework.views import APIView
import logging

logger = logging.getLogger(__name__)

@api_view(['GET'])
def api_root(request, format=None):
    # Use the correct Codespace URL for external access
    base_url = 'https://sturdy-meme-94vx4q5g9ph794w-8000.app.github.dev'
    return Response({
        'users': f'{base_url}/api/users/',
        'teams': f'{base_url}/api/teams/',
        'activity': f'{base_url}/api/activity/',
        'leaderboard': f'{base_url}/api/leaderboard/',
        'workouts': f'{base_url}/api/workouts/',
    })

class UserList(APIView):
    def get(self, request):
        print('UserList API called')
        client = MongoClient(settings.DATABASES['default']['CLIENT']['host'], settings.DATABASES['default']['CLIENT']['port'])
        db = client[settings.DATABASES['default']['NAME']]
        users = list(db.octofit_tracker_user.find())
        print(f'Fetched users from MongoDB: {users}')
        for user in users:
            user['_id'] = str(user['_id'])
        print(f'Returning users: {users}')
        return Response(users)