from django import forms

# from .models import DataOrder

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class AccountForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label='Phone', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label='Email', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    name.widget.attrs.update({'placeholder': 'Name'})
    phone.widget.attrs.update({'placeholder': 'Phone'})
    email.widget.attrs.update({'placeholder': 'Email'})
    name.label = ''
    phone.label = ''
    email.label = ''
    name.required = False
    phone.required = False
    email.required = False

