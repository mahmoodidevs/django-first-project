from django import forms
from .models import customer

class CustomerForm(forms.Form):
    firstname = forms.CharField(max_length=255)
    lastname = forms.CharField(max_length=255)

class UpdateCustomerForm(forms.ModelForm):
    class Meta:
        model = customer
        fields = "__all__"
