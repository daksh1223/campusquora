from django.shortcuts import render
from django.http import HttpResponse
from authentication.models import User
from .models import question,answer
# Create your views here.
def feed(request,id):
    if request.method == 'POST':
        q = question()
        q.topic = request.POST.get('question')
        q.writer = User.objects.get(pk=id)
        q.save()
    user = User.objects.get(pk=id)
    ques = question.objects.all()
    return render(request,'post/feed.html',{'ques':ques, 'user':user})

def quest(request,uid,qid):
    if request.method == 'POST':
        a = answer()
        a.content = request.POST.get('answer')
        a.writer = User.objects.get(pk=uid)
        a.ques = question.objects.get(pk=qid)
        a.save()
    user = User.objects.get(pk=uid)
    quest = question.objects.get(pk=qid)
    ans = answer.objects.all().filter(ques=quest)
    return render(request,'post/question.html',{'user':user, 'ans':ans , 'ques':quest})


