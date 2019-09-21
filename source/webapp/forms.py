from django import forms
from django.forms import widgets


class GuestBookForm(forms.Form):
    name = forms.CharField(max_length=200, required=True, label='Имя')
    email = forms.CharField(max_length=254, required=True, label='Email', widget=widgets.EmailInput)
    text = forms.CharField(max_length=3000, required=True, label='Текст', widget=widgets.Textarea)


class SearchForm(forms.Form):
    search = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class': "form-control mr-sm-2"}))
