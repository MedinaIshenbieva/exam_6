from django import forms
from django.forms import widgets

from webapp.models import STATUS_CHOICES


class GuestBookForm(forms.Form):
    author = forms.CharField(max_length=200, required=True, label="Автор")
    email = forms.EmailField(max_length=200, required=True, label="Имейл")
    text = forms.TextField(max_length=2000, required=True, label="Текст записи")
    status = forms.CharField(max_length=20, choices=STATUS_CHOICES)

