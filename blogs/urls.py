from django.urls import path
from . import views
urlpatterns=[
    path('category/',views.get_categorys,name='category'),
    path('blogs/',views.get_blogs,name='get_blogs'),
    path('blog/<int:pk>/',views.single_blog,name='get_blog'),
    path('create/blog/',views.create_post,name='create_post'),
    path('blog/delete/<int:pk>/',views.delete_post,name='delete_post'),
    path('comment/create/<int:pk>/',views.add_comment,name='add_comment'),
    path('comments/<int:pk>/', views.get_camments, name='get_comments'),
    path('comment/delete/<int:pk>/', views.delete_comment, name='delete_comment'),
    path('comment/<int:pk>/', views.single_comment, name='single_comment'),
    path('comments/<int:pk>/replies/', views.get_replys, name='get_replies'),
    path('comments/<int:pk>/replies/post/', views.post_reply, name='post_reply'), 
    path('replies/<int:pk>/delete/', views.delete_reply, name='delete_reply'),    
]