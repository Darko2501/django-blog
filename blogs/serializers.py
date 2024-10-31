from rest_framework import serializers
from .models import Category,Blog,Comments,Reply

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'
class BlogSerializer(serializers.ModelSerializer):
    category=CategorySerializer(read_only=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    author = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model=Blog
        fields=['id','title','post','category','author']
class CommentsSerializer(serializers.ModelSerializer):
    blog=BlogSerializer(read_only=True)
    blog=serializers.PrimaryKeyRelatedField(queryset=Blog.objects.all())
    class Meta:
        model=Comments
        fields=['id','blog','comment','user']
class ReplySerializer(serializers.ModelSerializer):
    comment=CommentsSerializer(read_only=True)
    comment=serializers.PrimaryKeyRelatedField(queryset=Comments.objects.all())
    class Meta:
        model=Reply
        fields=['id','user','comment','parent']
        
    
        
        
    
    
    