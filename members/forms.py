'''
Created on Mar 1, 2015

@author: tanja
'''
from django import forms

class EmailForm(forms.Form):
    '''Defines email form in members'''
    
    csrfmiddlewaretoken = forms.HiddenInput()
    email = forms.EmailField(label='')