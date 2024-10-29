from django.db import models

# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=100)
    def __str__(self):
        return self.title
class Blog(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='blogs')
    title=models.CharField(max_length=100)
    post=models.TextField()
    def __str__(self):
        return self.title
    

class Comments(models.Model):
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='comments')
    comment=models.TextField()
    def __str__(self):
        return self.blog
class Reply(models.Model):
    comment=models.ForeignKey(Comments,on_delete=models.CASCADE,related_name='replies')
    reply=models.TextField()
    def __str__(self):
        return self.comment

    