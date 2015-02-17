'''
Created on Feb 17, 2015

@author: Nenad
'''

from sys import exc_info
import logging

from instagram import InstagramAPI
from instagram.bind import InstagramAPIError, InstagramClientError

from nnpicksdj.settings import INSTAGRAM_API_KEY
from goodusers.models import GoodUser


class InstagramSession():
    '''Set of tools regarding Instagram API'''

    api = None
    
    def init_instagram_API(self):
        '''Initializes Instagram API session
        
        Parameters: -
        Returns: Instagram API session
        '''
        
        '''Read variable from settings.py'''
        access_token = INSTAGRAM_API_KEY
        try:
            api = InstagramAPI(access_token=access_token)
        except InstagramAPIError as e:
            logging.exception("init_instagram_API: ERR-00001 Instagram API Error %s : %s" % (e.status_code, e.error_message))
            #self.message_user(request, buf, level=messages.WARNING)
            
        except InstagramClientError as e:
            logging.exception("init_instagram_API: ERR-00002 Instagram Client Error %s : %s" % (e.status_code, e.error_message))
            #self.message_user(request, buf, level=messages.WARNING)
            
        except:
            logging.exception("init_instagram_API: ERR-00003 Unexpected error: " + exc_info()[0]   ) 
            #self.message_user(request, buf, level=messages.ERROR) 
        
    
    def is_instagram_user_valid(self, p_gooduser):
        '''Check if you can find Instagram user'''
        
        user_search = None
        if self.api:
            try:
                user_search = self.api.user_search(q=p_gooduser.instagram_user_name, count=1)
            except InstagramAPIError as e:
                logging.exception("is_instagram_user_valid: ERR-00004 Instagram API Error %s : %s" % (e.status_code, e.error_message))
    
            except InstagramClientError as e:
                logging.exception("is_instagram_user_valid: ERR-00005 Instagram Client Error %s : %s" % (e.status_code, e.error_message))
                return None
            except:
                logging.exception("is_instagram_user_valid: ERR-00006 Unexpected error: " + str(exc_info()[0]))    
                raise               
        
        if user_search:
            return True
        else:
            return False
        
    def get_instagram_user(self, user_search_result):
        '''Get Instagram user
        
        Parameters:
        p_gooduser - GoodUser object
        
        Returns
        Instagram user object
        '''
        
        instagram_user = None
        
        if self.api:        
            try:         
                instagram_user = self.api.user(user_search_result[0].id)
            except InstagramAPIError as e:
                logging.exception("get_instagram_user: ERR-00004 Instagram API Error %s : %s" % (e.status_code, e.error_message))

            except InstagramClientError as e:
                logging.exception("get_instagram_user: ERR-00005 Instagram Client Error %s : %s" % (e.status_code, e.error_message))
            except IndexError:
                logging.exception("get_instagram_user: ERR-00006 Instagram search unsuccessful: %s" % (exc_info()[0]))                
            except:
                logging.exception("get_instagram_user: ERR-00007 Unexpected error: %s" % (exc_info()[0]))    
 
            
        return instagram_user         