from django.http import HttpResponse
from django.shortcuts import render


def 홈페이지(request):
    #return render(request, 'newfolder/아무거나1.html')
    return render(request, '아무거나2.html')