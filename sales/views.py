from django.http import HttpResponse
from django.shortcuts import render , redirect , reverse
from .models import Sale , Person
from .forms import SaleForm , SaleModelForm
from django.views import generic , View
from django.contrib.auth import logout

class 첫화면View(generic.TemplateView):
    template_name = '첫화면.html'

def 첫화면(request):  
    return render(request, '첫화면.html')


class 세일_목록View(generic.ListView):
    template_name = 'newfolder/세일목록.html'
    queryset = Sale.objects.all()
    context_object_name =  "사람키"

def 세일목록(request):    
    사람=Sale.objects.all()
    context={
        "사람키" : 사람
    }
    return render(request, 'newfolder/세일목록.html',context)


class 세일_상세View(generic.DetailView):
    template_name = 'newfolder/세일상세.html'
    queryset = Sale.objects.all()
    context_object_name =  "사람키"



def 세일상세(request,pk):
    #세일 =Sale.objects.get(id=pk)
    #print("세일 :",세일)

    사람 =Sale.objects.get(id=pk)
    context={
        "사람키" : 사람
    }

    #return HttpResponse("<h1>여기 상세 정보입니다.</h1>")
    return render(request, 'newfolder/세일상세.html',context)



class 세일_입력View(generic.CreateView):
    template_name = 'newfolder/세일_입력.html'
    form_class = SaleModelForm
    def get_success_url(self):
        return reverse("홈페이지:목록")

def 세일_입력(request):
    폼 =SaleModelForm()

    if request.method == "POST":
       폼 = SaleModelForm(request.POST)
    
       if 폼.is_valid():          
          폼.save()          
          return redirect("/홈페이지")
       
    context={
        "form" : SaleModelForm
    }
    return render(request, 'newfolder/세일_입력.html', context)


class 세일_업데이트View(generic.UpdateView):
      template_name = 'newfolder/세일_업데이트.html'
      form_class = SaleModelForm
      queryset = Sale.objects.all()
      context_object_name =  "사람키"
      def get_success_url(self):
        return reverse("홈페이지:목록")


def 세일_업데이트(request, pk):
    사람 =Sale.objects.get(id=pk)
    
    if request.method == "POST":

        폼=SaleModelForm(request.POST, instance=사람)
        if 폼.is_valid():  
                     
           폼.save()

           return redirect("/홈페이지")
        
    else:        
        폼 =SaleModelForm(instance=사람)
    context={
        "사람키":사람,
        "폼키" : 폼
    }

    return render(request, 'newfolder/세일_업데이트.html', context)    



class 세일_지우기View(generic.DeleteView):
      #template_name = 'newfolder/세일_지우기.html'
      queryset = Sale.objects.all()
      def get_success_url(self):          
        return reverse("홈페이지:목록")


def 세일_지우기(request, pk):
    사람 =Sale.objects.get(id=pk)
    사람.delete()
    return redirect("/홈페이지")



class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')



""" def 세일_업데이트(request, pk):
    사람 =Sale.objects.get(id=pk)
    
    if request.method == "POST":
        폼=SaleForm(request.POST)
        if 폼.is_valid():
            first_name =폼.cleaned_data["first_name"]
            last_name =폼.cleaned_data["last_name"]
            age =폼.cleaned_data["age"]
            person=Person.objects.first()

            사람.first_name = first_name
            사람.last_name = last_name
            사람.age = age
            사람.person = person
            사람.save()
            return redirect("/홈페이지")
        
    else:        
        폼 =SaleModelForm(instance=사람)
    context={
        "사람키":사람,
        "폼키" : 폼
    }

    return render(request, 'newfolder/세일_업데이트.html', context)    
 """


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