# Rest Framework imports
from rest_framework.response import Response
from rest_framework.views import APIView


class HomeView(APIView):
    def get(self, request):
        data = {
            'message': 'Welcome to Tudus API',
            'endpoints': {
                'users': request.build_absolute_uri('api/v1/users/'),
                'lists': request.build_absolute_uri('api/v1/lists/'),
                'todo': request.build_absolute_uri('api/v1/todos/'),
            }
        }
        return Response(data)
