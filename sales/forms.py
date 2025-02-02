from django import forms
from .models import Sale

class SaleModelForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = (
            "first_name",
            "last_name",
            "age",
            "person"
        )
        styleInput="w-full max-w-sm border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-400 focus:border-indigo-400 transition"
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