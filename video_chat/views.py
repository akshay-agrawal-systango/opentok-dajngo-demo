from django.shortcuts import render, HttpResponse, redirect
from opentok import OpenTok, MediaModes, Roles
from django.conf import settings
from .models import OpenTokSessions
import time

def index(request):
    opentok_sessions = OpenTokSessions.objects.all()
    user_ip = request.META['REMOTE_ADDR']
    context = {'opentok_sessions': opentok_sessions, 'user_ip':user_ip}
    return render(request, 'index.html', context)

def video_chat_room(request, room_id):
    session_obj = OpenTokSessions.objects.get(id=room_id)
    session_id = session_obj.session_id
    opentok = OpenTok(settings.API_KEY, settings.PEOJECT_SECRET)
    expire_time = int(time.time()) + 3600
    token = opentok.generate_token(session_id, Roles.publisher, expire_time)
    context = {'token':token, 'session_id': session_id, 'api_key': settings.API_KEY}
    return render(request, 'video_chat_room.html', context)

def create_video_chat_room(request):
    opentok = OpenTok(settings.API_KEY, settings.PEOJECT_SECRET)
    user_ip = request.META['REMOTE_ADDR']
    session = opentok.create_session(media_mode=MediaModes.routed, location=user_ip)
    session_obj = OpenTokSessions.objects.create(session_id=session.session_id)
    return redirect('video_chat_room', room_id=session_obj.id)