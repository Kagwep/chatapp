from django.shortcuts import render,redirect
from .models import Friend,ChatMessage,Profile
from django.db.models import Q
from django.http import JsonResponse
import json
# Create your views here.


def home(request):
    
    user = request.user.profile
    
    friends = user.friends.all()
    
    context = {'user':user,'friends':friends}
    
    return render(request,"chat/home.html",context)


def detail(request,pk):
    friend = Friend.objects.get(profile_id=pk)
    chat_messages = ChatMessage.objects.filter((Q(msg_sender = request.user.profile) and Q(msg_receiver = friend.profile)) |  (Q(msg_sender = friend.profile ) and Q(msg_receiver = request.user.profile))).order_by('time_sent')
    chat_count = chat_messages.count()
    if request.method == 'POST':
        chat_data = request.POST
        receiver = Profile.objects.get(id=pk)
        msg = ChatMessage.objects.create(
            body = chat_data['message'],
            msg_sender = request.user.profile,
            msg_receiver = receiver,
        )
        
        chat_messages = ChatMessage.objects.filter((Q(msg_sender = request.user.profile) and Q(msg_receiver = friend.profile)) |  (Q(msg_sender = friend.profile ) and Q(msg_receiver = request.user.profile))).order_by('time_sent')
        chat_count = chat_messages.count()
        context = {"friend":friend,'chat_messages':chat_messages,'chat_count':chat_count}
        return redirect(request.META['HTTP_REFERER'],context)
        
        
    context={"friend":friend,'chat_messages':chat_messages,'chat_count':chat_count}
    return render(request,"chat/detail.html",context)

def sendMessages(request,pk):
    data = json.loads(request.body)
    new_chat = data['msg']
    receiver = Profile.objects.get(id=pk)
    msg_sent = ChatMessage.objects.create(
        body = new_chat,
        msg_sender = request.user.profile,
        msg_receiver = receiver,
    )
    return JsonResponse(msg_sent.body,safe=False)


def recieve_chat(request,pk):
    friend = Friend.objects.get(profile_id=pk)
    user = request.user.profile
    receiver = Profile.objects.get(id=pk)
    chat_messages = ChatMessage.objects.filter((Q(msg_sender = request.user.profile) and Q(msg_receiver = friend.profile)) |  (Q(msg_sender = friend.profile ) and Q(msg_receiver = request.user.profile))).order_by('time_sent')
    chat_messages_data = [ message.body for message in chat_messages]
    return JsonResponse(chat_messages_data,safe=False)


def chat_notifications(request):
    friends = Friend.objects.all()
    user = request.user.profile
    for friend in friends:
        chat_messages = ChatMessage.objects.filter((Q(msg_sender = request.user.profile) and Q(msg_receiver = friend.profile)) |  (Q(msg_sender = friend.profile ) and Q(msg_receiver = request.user.profile))).order_by('time_sent')
        chat_messages_data = [ message.body for message in chat_messages]
    return JsonResponse('working',safe=False)