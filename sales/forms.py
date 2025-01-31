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

class SaleForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    age = forms.IntegerField(min_value=0)