from django import forms

from .models import Requests


class CreateReqeustForm(forms.ModelForm):
    class Meta:
        model = Requests
        fields = ('full_name', 'msisdn', 'email', 'comments', 'agreement')
