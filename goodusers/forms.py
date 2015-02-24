'''
Created on Feb 24, 2015

@author: n.nikolic
'''
from django import forms

class ContactForm(forms.Form):
    '''simple contact form'''
    csrfmiddlewaretoken = forms.HiddenInput()
    email = forms.EmailField(label='Your Email')
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)