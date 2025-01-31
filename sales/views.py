from django.http import HttpResponse
from django.shortcuts import render
from .models import Sale


def 세일목록(request):
    사람=Sale.objects.all()
    context={
        "사람키" : 사람
    }
    return render(request, 'newfolder/세일목록.html',context)


def 세일상세(request,pk):
    return HttpResponse("<h1>여기 상세 정보입니다.</h1>")