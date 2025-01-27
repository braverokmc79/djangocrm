from django.http import HttpResponse
from django.shortcuts import render


def 홈페이지(request):
    return HttpResponse("응 나야")