from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PostSerializer
from .models import Post
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .permissions import IsPostPossessor
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .filter import PostFilter
# Create your views here.

class HelloWorldView(APIView):
    def get(self, request):
        return Response({"message": "Hello, World!"})
    
    
class PostView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated , IsPostPossessor]
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['id']
    filterset_class = PostFilter
    search_fields = ['title', 'content']

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)
    