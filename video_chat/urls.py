from django.urls import path
from .views import index, video_chat_room, create_video_chat_room

urlpatterns = [
    path('', index, name='index'),
    path('create_video_chat_room/', create_video_chat_room, name='create_video_chat_room'),
    path('video_chat_room/<int:room_id>/', video_chat_room, name='video_chat_room')
]
