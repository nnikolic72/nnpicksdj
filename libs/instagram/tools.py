'''
Created on Feb 17, 2015

@author: Nenad
'''

from sys import exc_info

from instagram import InstagramAPI
from instagram.bind import InstagramAPIError, InstagramClientError

from nnpicksdj.settings import INSTAGRAM_API_KEY

class InstagramAPIError(Exception):
    ''''''
    
    pass

class InstagramClientError(Exception):
    ''''''
    
    pass

class InstagramUnhandledError(Exception):
    ''''''
    
    pass

class InstagramSession():
    '''Set of tools regarding Instagram API'''
    InstagramAPIError = InstagramAPIError
    InstagramClientError = InstagramClientError
    InstagramUnhandledError = InstagramUnhandledError
    
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
            buf = "process_gooduser: ERR-00001 Instagram API Error %s : %s" % (e.status_code, e.error_message)
            raise InstagramAPIError
            #self.message_user(request, buf, level=messages.WARNING)
            
        except InstagramClientError as e:
            buf = "process_gooduser: ERR-00002 Instagram Client Error %s : %s" % (e.status_code, e.error_message)
            raise InstagramClientError
            #self.message_user(request, buf, level=messages.WARNING)
            
        except:
            buf = "process_gooduser: ERR-00003 Unexpected error: " + exc_info()[0]    
            #self.message_user(request, buf, level=messages.ERROR)
            raise InstagramUnhandledError  
        
        return api    