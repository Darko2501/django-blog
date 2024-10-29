from django.shortcuts import render
from .models import Blog
from .serializers import BlogSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny])
def get_blogs(request):
    blog=Blog.objects.all()
    serializer=BlogSerializer(blog,many=True)
    return Response(serializer.data)
        
@api_view(['GET'])
@permission_classes([AllowAny])
def single_blog(request,pk):
    try:
       blog=Blog.objects.get(pk=pk)
       
    except Blog.DoesNotExist:
        return Response({'error':'The blog does not exist'},status=status.HTTP_404_NOT_FOUND)
    serializer=BlogSerializer(blog)
    return Response (serializer.data,status=status.HTTP_200_OK)
