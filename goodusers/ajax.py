'''
Created on Feb 24, 2015

@author: n.nikolic
'''
from django.conf import settings

from dajaxice.decorators import dajaxice_register

from social_auth.models import UserSocialAuth  # @UnresolvedImport

from .forms import PhotoCommentForm
from libs.instagram.tools import MyLikes, InstagramSession
import json

   
@dajaxice_register
def like(req, p_photo_id):
    '''Like/Unlike instagram media with ID p_photo_id'''
    
    tokens = UserSocialAuth.get_social_auth_for_user(req.user).get().tokens    
    ig_session = InstagramSession(p_is_admin=False, p_token=tokens['access_token'])
    ig_session.init_instagram_API()
    
    
    my_likes = MyLikes(req.user.username, p_photo_id, ig_session)
    like_action_result = my_likes.like_instagram_media() # "like", "unlike", "error"  
    
    return json.dumps({'photo_id':p_photo_id, 
                       'like_action_result':like_action_result,
                       'static_url': settings.STATIC_URL
                       }
                      )


@dajaxice_register
def send_comment(req, p_photo_id, form):
    f = PhotoCommentForm(form)
    comment_action_result= 'error'
    if f.is_valid(): 
        # Use mail_admin or something to send off the data like you normally would.
        tokens = UserSocialAuth.get_social_auth_for_user(req.user).get().tokens    
        ig_session = InstagramSession(p_is_admin=False, p_token=tokens['access_token'])
        ig_session.init_instagram_API()
        
        
        my_likes = MyLikes(req.user.username, p_photo_id, ig_session)
        comment_action_result = my_likes.comment_instagram_media(f.data['comment'])
                
    return json.dumps({'status': comment_action_result})
