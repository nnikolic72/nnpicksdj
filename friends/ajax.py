'''
Created on Mar 2, 2015

@author: n.nikolic
'''
from dajaxice.decorators import dajaxice_register

@dajaxice_register
def interact_with_friends_photo(req, p_photo_id):
    '''AJAX function to interact with friends photo'''
    
    