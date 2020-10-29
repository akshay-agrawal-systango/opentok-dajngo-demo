from django.shortcuts import render, HttpResponse, redirect
from opentok import OpenTok, MediaModes
from django.conf import settings
from .models import OpenTokSessions, OpenTokTokens

def index(request):
    opentok_sessions = OpenTokSessions.objects.all()
    context = {'opentok_sessions': opentok_sessions}
    return render(request, 'index.html', context)

def video_chat_room(request, room_id):
    session_obj = OpenTokSessions.objects.get(id=room_id)
    session_id = session_obj.session_id
    token = session_obj.opentoktokens_set.all().last().token
    context = {'token':token, 'session_id': session_id, 'api_key': settings.API_KEY}
    return render(request, 'video_chat_room.html', context)

def create_video_chat_room(request):
    opentok = OpenTok(settings.API_KEY, settings.PEOJECT_SECRET)
    session = opentok.create_session(media_mode=MediaModes.routed)
    token = opentok.generate_token(session.session_id)
    session_obj = OpenTokSessions.objects.create(session_id=session.session_id)
    session_obj.opentoktokens_set.create(token=token)
    return redirect('video_chat_room', room_id=session_obj.id)