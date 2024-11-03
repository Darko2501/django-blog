from django.shortcuts import render
from .models import Blog,Category,Comments,Reply
from .serializers import BlogSerializer,CategorySerializer,CommentsSerializer,ReplySerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework import status
# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny])
def get_categorys(request):
    category=Category.objects.all()
    serializer=CategorySerializer(category,many=True)
    return Response({'Category:':serializer.data},status=status.HTTP_200_OK)
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
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_post(request):
    serializer=BlogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(author=request.user)
        return Response({'mesage':serializer.data},status=status.HTTP_201_CREATED)
    return Response({'message':'You did not enter valid data'},status=status.HTTP_406_NOT_ACCEPTABLE)
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_post(request,pk):
    try:
        blog=Blog.objects.get(pk=pk,author=request.user)
        blog.delete()
        return Response({'message':'Your blog is deleted'},status=status.HTTP_204_NO_CONTENT)
    except:
        return Response({'message':'You cant dellete this blog'},status=status.HTTP_403_FORBIDDEN)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_comment(request,pk):
    try:
        blog=Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        return Response({"message":"Blog is not found"},status=status.HTTP_404_NOT_FOUND)
    data={
        'blog':pk,
        'comment':request.data.get('comment'),
        'user':request.user.id
    }
    serializer=CommentsSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"You add comment to this blog"},status=status.HTTP_201_CREATED)
    return Response({"message": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
@permission_classes([AllowAny])
def get_camments(request,pk):
    try: 
        blog=Blog.objects.get(pk=pk)
       
    except Blog.DoesNotExist:
        return Response({'message':"Blog is not found"},status=status.HTTP_404_NOT_FOUND)
    comments=Comments.objects.filter(blog=blog)
    
    serializer=CommentsSerializer(comments,many=True)
    return Response({"Comments:":serializer.data},status=status.HTTP_200_OK)
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_comment( request,pk):
    try:
      comment=Comments.objects.get(user=request.user,pk=pk)
      comment.delete()
      return Response({'message':'Your blog is deleted'},status=status.HTTP_204_NO_CONTENT)
    except Comments.DoesNotExist:
        return Response({"message":"Comment does not exist"},status=status.HTTP_404_NOT_FOUND)
@api_view(['GET'])
@permission_classes([AllowAny])
def single_comment(request,pk):
    try:
        comment=Comments.objects.get(pk=pk)
        serializer=CommentsSerializer(comment)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except Comments.DoesNotExist:
        return Response({"message":"This comment is not exist"},status=status.HTTP_404_NOT_FOUND)
@api_view(['GET'])
@permission_classes([AllowAny])
def get_replys(request,pk):
    try:
        comment=Comments.objects.get(pk=pk)
        reply=Reply.objects.filter(comment=comment)
        serializer=ReplySerializer(reply,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except Comments.DoesNotExist:
        return Response({"message":"Comment does not exist"},status=status.HTTP_404_NOT_FOUND)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_reply(request, pk):
    try:
        comment = Comments.objects.get(pk=pk)
        if 'parent' not in request.data:
            reply_data = {
                'user': request.user.id,
                'reply': request.data.get('reply'),
                'comment': pk,
            }
        else:
            parent_id = request.data['parent']
            try:
                parent_reply = Reply.objects.get(pk=parent_id)
                reply_data = {
                    'user': request.user.id,
                    'reply': request.data.get('reply'),
                    'comment': pk,
                    'parent': parent_id,  
                }
            except Reply.DoesNotExist:
                return Response({"message": "Parent reply does not exist."}, status=status.HTTP_404_NOT_FOUND)
        serializer = ReplySerializer(data=reply_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"reply": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Enter valid data"}, status=status.HTTP_400_BAD_REQUEST)

    except Comments.DoesNotExist:
        return Response({"message": "Comment does not exist"}, status=status.HTTP_404_NOT_FOUND)
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_reply(request, pk):
    try:
        reply = Reply.objects.get(pk=pk)
        if reply.user != request.user:
            return Response({"message": "You do not have permission to delete this reply."}, status=status.HTTP_403_FORBIDDEN)
        reply.delete()
        return Response({"message": "Reply deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

    except Reply.DoesNotExist:
        return Response({"message": "Reply does not exist."}, status=status.HTTP_404_NOT_FOUND)

