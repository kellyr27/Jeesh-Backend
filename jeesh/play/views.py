from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from play.core.game import initialize_game

# Create your views here.
class IndexView(APIView):
    def post(self, request):
        return Response({"message": "Post request performed successfully"}, status=status.HTTP_200_OK)

class InitializeView(APIView):
    def post(self, request):
        return Response(initialize_game(), status=status.HTTP_200_OK)