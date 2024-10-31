from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=100)
    def __str__(self):
        return self.title
class Blog(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='blogs')
    title=models.CharField(max_length=100)
    author=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    post=models.TextField()
    def __str__(self):
        return self.title
    

class Comments(models.Model):
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='comments')
    comment=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    def __str__(self):
        return self.blog
class Reply(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    comment=models.ForeignKey(Comments,on_delete=models.CASCADE,related_name='replies')
    reply=models.TextField()
    parent=models.ForeignKey('self',null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.comment}-{self.reply}'

    