from django.http import HttpResponse
from django.shortcuts import render
from .models import 아이디


def 홈페이지(request):
    #return render(request, 'newfolder/아무거나1.html')
    드실분=아이디.objects.all()
    context={
        "메뉴명" :"짜장",
        "가격" : "700원",
        "손님" : 드실분
    }
    return render(request, '아무거나2.html',context)