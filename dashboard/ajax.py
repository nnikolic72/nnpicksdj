'''
Created on Mar 1, 2015

@author: tanja
'''
import json

from django.contrib.auth.models import User

from dajaxice.decorators import dajaxice_register

from .forms import EmailForm


@dajaxice_register
def send_email(req, form):
    '''AJAX fuction that saves e-mail address of logged_in UserWarning
    
    Parameters:
    email_address - text of email address
    
    Returns:
    Nothing
    '''
    
    f = EmailForm(form)
    submit_action_result= 'error'
        
    if f.is_valid():
        l_logged_user_id = req.user.id
        l_logged_users = User.objects.filter(id=l_logged_user_id)
        for l in l_logged_users:
            l.email = f.data['email']
            l.save()
            submit_action_result= 'ok'
        
    return json.dumps({'status': submit_action_result})