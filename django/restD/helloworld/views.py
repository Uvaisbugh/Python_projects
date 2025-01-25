from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PostSerializer
from .models import Post
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .permissions import IsPostPossessor
# Create your views here.

class HelloWorldView(APIView):
    def get(self, request):
        return Response({"message": "Hello, World!"})
    
    
class PostView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated , IsPostPossessor]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    