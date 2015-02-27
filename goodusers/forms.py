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
    
class PhotoCommentForm(forms.Form):
    '''Instagram photo comment form''' 
    
    csrfmiddlewaretoken = forms.HiddenInput()
    comment = forms.CharField(widget=forms.Textarea(attrs={'class' : 'igcommentclass'}), label='')  