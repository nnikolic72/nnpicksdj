'''
Created on Feb 17, 2015

@author: Nenad
'''
from __future__ import division
from sys import exc_info

import numpy as np
import logging

from instagram import InstagramAPI
from instagram.bind import InstagramAPIError, InstagramClientError

from nnpicksdj.settings import INSTAGRAM_API_KEY
#from goodusers.models import GoodUser


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
            self.api = InstagramAPI(access_token=access_token)
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
        
        return user_search

    def is_instagram_photo_valid(self, p_photo_id):
        '''Checks if Instagram photo exists'''
        
        try:
            l_photo = self.api.media(media_id = p_photo_id)
        except InstagramAPIError as e:
            logging.exception("is_instagram_photo_valid: ERR-00018 Instagram API Error %s : %s" % (e.status_code, e.error_message))

        except InstagramClientError as e:
            logging.exception("is_instagram_photo_valid: ERR-00019 Instagram Client Error %s : %s" % (e.status_code, e.error_message))
            return None
        except:
            logging.exception("is_instagram_photo_valid: ERR-00020 Unexpected error: " + str(exc_info()[0]))    
            raise("is_instagram_photo_valid: ERR-00020 Unexpected error: " + str(exc_info()[0]))
        
        if l_photo:
            return True
        else:
            return False      
        
    def get_instagram_photo_info(self, p_photo_id):
        '''returns Instagram photo information'''
        
        try:
            l_photo = self.api.media(media_id = p_photo_id)
        except InstagramAPIError as e:
            logging.exception("get_instagram_photo_info: ERR-00021 Instagram API Error %s : %s" % (e.status_code, e.error_message))

        except InstagramClientError as e:
            logging.exception("get_instagram_photo_info: ERR-00022 Instagram Client Error %s : %s" % (e.status_code, e.error_message))
            return None
        except:
            logging.exception("get_instagram_photo_info: ERR-00023 Unexpected error: " + str(exc_info()[0]))    
            raise("get_instagram_photo_info: ERR-00023 Unexpected error: " + str(exc_info()[0]))
        
        return l_photo
        
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
                instagram_user = self.api.user(user_search_result)
            except InstagramAPIError as e:
                logging.exception("get_instagram_user: ERR-00014 Instagram API Error %s : %s" % (e.status_code, e.error_message))

            except InstagramClientError as e:
                logging.exception("get_instagram_user: ERR-00015 Instagram Client Error %s : %s" % (e.status_code, e.error_message))
            except IndexError:
                logging.exception("get_instagram_user: ERR-00016 Instagram search unsuccessful: %s" % (exc_info()[0]))                
            except:
                logging.exception("get_instagram_user: ERR-00017 Unexpected error: %s" % (exc_info()[0]))
                raise("get_instagram_user: ERR-00017 Unexpected error: %s" % (exc_info()[0]))    
 
            
        return instagram_user   
    
    def get_api_limits(self):
        '''Returns a tuple of (Instagram AOI limit remaining, Instagram API limit)'''
        
        return self.api.x_ratelimit_remaining, self.api.x_ratelimit      


    
class BestPhotos:
    '''Find best photos of instgaram user'''
    l_user_has_photos = True
    
    def __init__(self, instgram_user_id, top_n_photos, search_photos_amount):
        self.l_instgram_user_id = instgram_user_id
        self.l_top_n_photos = top_n_photos
        self.l_search_photos_amount = search_photos_amount
        self.l_instagram_user_id = instgram_user_id
        
    def linreg(self, x, y):
        '''Does linear regression parameter calculation'''
        
        regression = np.polyfit(x, y, 2) 
        return regression
    
    def prediction(self, regression, point):
        '''Returns prediction for given argument(number of likes)'''
        
        y = regression[0]*point + regression[1]
        return y   
    
    def get_instagram_photos(self):
        '''Retreive l_search_photos_amount photos of given Instagram user
        l_instgram_user_id
        
        '''
        
        try:
            recent_media, x_next = self.api.user_recent_media(user_id=self.l_instgram_user_id)
        except InstagramAPIError as e:
            logging.exception("get_instagram_photos: ERR-00008 Instagram API Error %s : %s" % (e.status_code, e.error_message))

        except InstagramClientError as e:
            logging.exception("get_instagram_photos: ERR-00009 Instagram Client Error %s : %s" % (e.status_code, e.error_message))
        except IndexError:
            logging.exception("get_instagram_photos: ERR-00010 Instagram search unsuccessful: %s" % (exc_info()[0]))                
        except:
            logging.exception("get_instagram_photos: ERR-00011 Unexpected error: %s" % (exc_info()[0]))
            raise("get_instagram_user: ERR-00011 Unexpected error: %s" % (exc_info()[0]))    

        if recent_media and x_next:     
            while x_next:
                try:     
                    media_feed, x_next = self.api.user_recent_media(with_next_url = x_next)
                except InstagramAPIError as e:
                    logging.exception("get_instagram_photos: ERR-00012 Instagram API Error %s : %s" % (e.status_code, e.error_message))
        
                except InstagramClientError as e:
                    logging.exception("get_instagram_photos: ERR-00013 Instagram Client Error %s : %s" % (e.status_code, e.error_message))
                except IndexError:
                    logging.exception("get_instagram_photos: ERR-000114 Instagram search unsuccessful: %s" % (exc_info()[0]))                
                except:
                    logging.exception("get_instagram_photos: ERR-00015 Unexpected error: %s" % (exc_info()[0]))
                    raise("get_instagram_user: ERR-00015 Unexpected error: %s" % (exc_info()[0]))    

                    
                recent_media.extend(media_feed)
                if len (recent_media) >= self.l_search_photos_amount:
                    break
        else:
            self.l_user_has_photos = False
        
        if self.l_user_has_photos:    
            self.l_latest_photos = recent_media
        else:
            self.l_user_has_photos = None
