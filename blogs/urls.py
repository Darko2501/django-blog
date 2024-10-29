from django.urls import path
from . import views
urlpatterns=[
    path('blogs/',views.get_blogs,name='get_blogs'),
    path('blog/<int:pk>/',views.single_blog,name='get_blog'),
]