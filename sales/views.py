from django.http import HttpResponse
from django.shortcuts import render , redirect
from .models import Sale , Person
from .forms import SaleForm , SaleModelForm

def 세일목록(request):
    사람=Sale.objects.all()
    context={
        "사람키" : 사람
    }
    return render(request, 'newfolder/세일목록.html',context)


def 세일상세(request,pk):
    #print(pk)

    #세일 =Sale.objects.get(id=pk)
    #print("세일 :",세일)

    사람 =Sale.objects.get(id=pk)
    context={
        "사람키" : 사람
    }

    #return HttpResponse("<h1>여기 상세 정보입니다.</h1>")
    return render(request, 'newfolder/세일상세.html',context)


def 세일_입력(request):
    폼 =SaleModelForm()

    if request.method == "POST":
       폼 = SaleModelForm(request.POST)
    
       if 폼.is_valid():          
          폼.save()          
          return redirect("/홈페이지")
       
    context={
        "폼키" : SaleModelForm
    }
    return render(request, 'newfolder/세일_입력.html', context)


""" def 세일_입력(request):
    폼 =SaleForm()
    if request.method == "POST":
       print("포스트 메소드로 왔네요")
       폼 = SaleForm(request.POST)
       if 폼.is_valid():
          print("유효하네요.")
          print("폼 cleaned_data : ",폼.cleaned_data)
          first_name =폼.cleaned_data["first_name"]
          last_name =폼.cleaned_data["last_name"]
          age =폼.cleaned_data["age"]
          person=Person.objects.first()

          Sale.objects.create(
             first_name = first_name,
             last_name = last_name,
             age = age,
             person = person
          )
          print("세일이 입력 되었습니다.")          
          return redirect("/홈페이지")
       
    context={
        "폼키" : SaleForm
    }
    return render(request, 'newfolder/세일_입력.html', context) """