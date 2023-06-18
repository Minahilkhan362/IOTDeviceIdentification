from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class LightStatus(APIView):
    def post(self, request, *args, **kwargs):
        return Response({'success': True, 'status': request.data.get('status')}, status=status.HTTP_200_OK)
