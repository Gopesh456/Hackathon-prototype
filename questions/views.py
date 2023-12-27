from django.shortcuts import render, redirect
from .models import Questions,answer
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime

# Create your views here.

@login_required(login_url='login')
def questions(req,pk):
    context = {
        'pk': str(pk)
    }
    if req.method == 'POST':
        userAns = req.POST['textarea']
        # print(questions)
        ans_q = Questions.objects.get(qno = pk)
        current_username = req.user.username
        ans_q.ans = userAns
        ans_q.save()
        ans_a = answer(username = current_username,ans = userAns)
        ans_a.qno = pk
        ans_a.create = datetime.now()
        ans_a.Result = '-'
        ans_a.save()
        print(ans_q.ans)
        print(ans_a.create)

        
    return render(req,'questions/index.html',context)

def homepage(req):
    return render(req,'index.html')

def getques(req):
    questions = Questions.objects.all()
    return JsonResponse({'question':list(questions.values())})

@login_required(login_url='login')
def overview(req):
    context = {
        '1_QE' : answer.objects.filter(username = req.user.username, qno = '1').exists(),
        '2_QE' : answer.objects.filter(username = req.user.username, qno = '2').exists(),
        '3_QE' : answer.objects.filter(username = req.user.username, qno = '3').exists(),
        '4_QE' : answer.objects.filter(username = req.user.username, qno = '4').exists(),
        '5_QE' : answer.objects.filter(username = req.user.username, qno = '5').exists(),
        '6_QE' : answer.objects.filter(username = req.user.username, qno = '6').exists(),
        '7_QE' : answer.objects.filter(username = req.user.username, qno = '7').exists(),
        '8_QE' : answer.objects.filter(username = req.user.username, qno = '8').exists(),
        '9_QE' : answer.objects.filter(username = req.user.username, qno = '9').exists(),
        '10_QE' : answer.objects.filter(username = req.user.username, qno = '10').exists(),
    }
    context2 = {
        '1_QE' : '-',
        '2_QE' : '-',
        '3_QE' : '-',
        '4_QE' : '-',
        '5_QE' : '-',
        '6_QE' : '-',
        '7_QE' : '-',
        '8_QE' : '-',
        '9_QE' : '-',
        '10_QE' : '-'
    }
    for i in range(1,11):
        key = str(i)+'_QE'
        if context[key]:
            context2[key] = answer.objects.filter(username = req.user.username, qno = i).last().Result
        else:
            pass
            

    return render(req,'questions/overview.html',context2)

    