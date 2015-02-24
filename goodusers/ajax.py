'''
Created on Feb 24, 2015

@author: n.nikolic
'''
from dajaxice.decorators import dajaxice_register
#from .forms import ContactForm
#import json

@dajaxice_register
def send_message(req):
    return "xyz"
    