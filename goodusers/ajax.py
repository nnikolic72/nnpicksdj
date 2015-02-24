'''
Created on Feb 24, 2015

@author: n.nikolic
'''
from dajaxice.decorators import dajaxice_register
from .forms import ContactForm
import json

@dajaxice_register
def send_message(req, form):
    f = ContactForm(form)
    if f.is_valid(): 
        # Use mail_admin or something to send off the data like you normally would.
        return json.dumps({'status':'Success!'})
    return json.dumps({'status':f.errors})
    