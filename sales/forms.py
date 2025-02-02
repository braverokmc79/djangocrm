from django import forms
from .models import Sale
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth import  get_user_model
User = get_user_model()


styleInput="w-full max-w-sm border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-400 focus:border-indigo-400 transition"

class SaleModelForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = (
            "first_name",
            "last_name",
            "age",
            "person"
        )      
        widgets ={
            "first_name": forms.TextInput(attrs={
                "class": styleInput,
                "placeholder": "이름을 입력하세요",
            }),
            "last_name": forms.TextInput(attrs={
                "class": styleInput,
                "placeholder": "성을 입력하세요",
            }),
            "age": forms.NumberInput(attrs={
                "class": styleInput,
                "placeholder": "나이를 입력하세요",
            }),
            "person": forms.Select(attrs={
                "class": styleInput,                
            }),
        }


class SaleForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    age = forms.IntegerField(min_value=0)


class 우리만의UserCreationForm(UserCreationForm):    
    class Meta:
        model =User
        fields = (
            "username",
            "email",
            "password1",
            "password2"
        )
        widgets ={
            "username": forms.TextInput(attrs={
                "class": styleInput,
                "placeholder": "아이디를 입력하세요",
            }),
            "email": forms.EmailInput(attrs={
                "class": styleInput,
                "placeholder": "이메일을 입력하기",
            }) ,
            "password1": forms.PasswordInput(attrs={
                "class": styleInput,
                "placeholder": "비밀번호을 입력하기",
            }),
            "password2": forms.PasswordInput(attrs={
                "class": styleInput,
                "placeholder": "비밀번호을 다시 입력하기",
            }) 
        }