from django import forms
from django.forms import ModelForm
from .models import Contact, Accounts

class FeedbackForm(forms.Form):
    email = forms.EmailField(label="Your Email")
    username = forms.CharField(label="Name")
    message = forms.CharField(label="Body", widget=forms.Textarea)


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        #exclude = ['user_name']
        fields = ('contact', 'address', 'memo',)


class AccountForm(ModelForm):
    class Meta:
        model = Accounts
        fields = ('user_name', 'name', 'address', 'seed',)
