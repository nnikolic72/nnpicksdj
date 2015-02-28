'''
Created on Feb 17, 2015

@author: Nenad
'''
from __future__ import division
from sys import exc_info
from datetime import datetime

import numpy as np
import logging

from instagram import InstagramAPI
from instagram.bind import InstagramAPIError, InstagramClientError

from nnpicksdj.settings.local import INSTAGRAM_API_KEY
#from goodusers.models import GoodUser


class InstagramSession():
    '''Set of tools regarding Instagram API'''

    api = None
    
    def __init__(self, p_is_admin, p_token):
        
        if p_is_admin:
            self.access_token = INSTAGRAM_API_KEY
        else:
            self.access_token = p_token
    
    def init_instagram_API(self):
        '''Initializes Instagram API session
        
        Parameters: -
        Returns: Instagram API session
        '''
        
        '''Read variable from settings.py'''
        
        try:
            self.api = InstagramAPI(access_token=self.access_token)
            
            '''Perform simple api search to set x_ratelimit_remaining'''
            temp = self.api.user_search(q='instagram', count=1)  # @UnusedVariable
        except InstagramAPIError as e:
            logging.exception("init_instagram_API: ERR-00001 Instagram API Error %s : %s" % (e.status_code, e.error_message))
            #self.message_user(request, buf, level=messages.WARNING)
            
        except InstagramClientError as e:
            logging.exception("init_instagram_API: ERR-00002 Instagram Client Error %s : %s" % (e.status_code, e.error_message))
            #self.message_user(request, buf, level=messages.WARNING)
            
        except:
            logging.exception("init_instagram_API: ERR-00003 Unexpected error: " + exc_info()[0]   )
            raise 
            #self.message_user(request, buf, level=messages.ERROR) 
        
    
    def is_instagram_user_valid(self, p_gooduser_name):
        '''Check if you can find Instagram user'''
        
        user_search = None
        if self.api:
            try:
                user_search = self.api.user_search(q=p_gooduser_name, count=1)
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
            l_photo = self.api.media(media_id=p_photo_id)
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


class MyLikes:
    '''Store my likes'''
    
    def __init__(self, p_instgram_user, p_photo_id, p_instagram_api):
        '''Initialize class object
           Parameters:
           p_instagram_api - opened instagram session
           p_max_like_id - photo ID
        '''
        
        self.liked_media = None
        self.instagram_session = p_instagram_api
        self.photo_id = p_photo_id # ID of media to check
        self.my_instgram_username = p_instgram_user
        
    
        
    def has_user_liked_media(self):
        '''returns if user liked the media self.max_like_id '''
        
        self.liked_media = self.instagram_session.get_instagram_photo_info(self.photo_id)
        

        if self.liked_media.user_has_liked :
            return True
        else:
            return False
        
    def like_instagram_media(self):
        '''Procedure that likes instagram media with ID  self.photo_id'''
        
        result = 'error'
        
        '''Check if media is already liked'''
        if self.has_user_liked_media():
            '''If already liked - unlike'''
            try:
                self.instagram_session.api.unlike_media(media_id=self.photo_id)
                result = 'unlike'
            except InstagramAPIError as e:
                logging.exception("get_instagram_user: ERR-00032 Instagram API Error %s : %s" % (e.status_code, e.error_message))
            except InstagramClientError as e:
                logging.exception("get_instagram_user: ERR-00033 Instagram Client Error %s : %s" % (e.status_code, e.error_message))
            except IndexError:
                logging.exception("get_instagram_user: ERR-00034 Instagram search unsuccessful: %s" % (exc_info()[0]))                
            except:
                logging.exception("get_instagram_user: ERR-00035 Unexpected error: %s" % (exc_info()[0]))
                raise                   
        else:
            '''if not already liked - like'''
            try:
                self.instagram_session.api.like_media(media_id=self.photo_id)
                result = 'like'
            except InstagramAPIError as e:
                logging.exception("get_instagram_user: ERR-00036 Instagram API Error %s : %s" % (e.status_code, e.error_message))
            except InstagramClientError as e:
                logging.exception("get_instagram_user: ERR-00037 Instagram Client Error %s : %s" % (e.status_code, e.error_message))
            except IndexError:
                logging.exception("get_instagram_user: ERR-00038 Instagram search unsuccessful: %s" % (exc_info()[0]))                
            except:
                logging.exception("get_instagram_user: ERR-00039 Unexpected error: %s" % (exc_info()[0]))
                raise             

        return result
    
    def comment_instagram_media(self, p_comment_text):
        '''Procedure that likes instagram media with ID  self.photo_id'''
        
        result = 'error'
        

        try:
            self.instagram_session.api.create_media_comment (media_id=self.photo_id,
                                                             text=p_comment_text
                                                             )
            result = 'comment'
        except InstagramAPIError as e:
            logging.exception("get_instagram_user: ERR-00040 Instagram API Error %s : %s" % (e.status_code, e.error_message))
        except InstagramClientError as e:
            logging.exception("get_instagram_user: ERR-00041 Instagram Client Error %s : %s" % (e.status_code, e.error_message))
        except IndexError:
            logging.exception("get_instagram_user: ERR-00042 Instagram search unsuccessful: %s" % (exc_info()[0]))                
        except:
            logging.exception("get_instagram_user: ERR-00043 Unexpected error: %s" % (exc_info()[0]))
            raise                   
          

        return result
    
    
class BestPhotos:
    '''Find best photos of instgaram user'''
    l_user_has_photos = True
    
    def __init__(self, instgram_user_id, top_n_photos, search_photos_amount, instagram_api):
        '''Initialize class object'''
        
        self.l_instgram_user_id = instgram_user_id
        self.l_top_n_photos = top_n_photos
        self.l_search_photos_amount = search_photos_amount
        self.l_instagram_user_id = instgram_user_id
        self.l_latest_photos = None
        self.instagram_session = instagram_api
        '''Resulting list of Instagram photo id's, length of max top_n_photos'''
        self.top_photos_list = []
        
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
        
        Returns:
        Nothing
        '''
        
        try:
            recent_media, x_next = self.instagram_session.api.user_recent_media(user_id=self.l_instgram_user_id)
        except InstagramAPIError as e:
            logging.exception("get_instagram_photos: ERR-00008 Instagram API Error %s : %s" % (e.status_code, e.error_message))

        except InstagramClientError as e:
            logging.exception("get_instagram_photos: ERR-00009 Instagram Client Error %s : %s" % (e.status_code, e.error_message))
        except IndexError:
            logging.exception("get_instagram_photos: ERR-00010 Instagram search unsuccessful: %s" % (exc_info()[0]))                
        except:
            logging.exception("get_instagram_photos: ERR-00011 Unexpected error: %s" % (exc_info()[0]))
            raise("get_instagram_user: ERR-00011 Unexpected error: %s" % (exc_info()[0]))    

        if not recent_media:
            self.l_user_has_photos = False
            
        if recent_media and x_next:     
            while x_next:
                try:     
                    media_feed, x_next = self.instagram_session.api.user_recent_media(with_next_url = x_next)
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
            
        
        if self.l_user_has_photos:    
            self.l_latest_photos = recent_media
        else:
            self.l_user_has_photos = None
            

    def get_top_photos(self):
        '''Using linear regression find top photos in media pool of Instagram UserWarning
        
        Parameters:
        p_number_of_photos - top X photos to find
        p_media - Instagram API media object - list of Instagram photos of the user
        '''
        
        if self.l_user_has_photos:
            '''Convert Instagram media object to list'''
            l_media_list = []
            for x_media in self.l_latest_photos:
                l_time_delta = datetime.today() - x_media.created_time
                l_media_list.append([x_media.id, x_media.like_count, 
                                                    x_media.comment_count, 
                                                    l_time_delta.days,
                                                    0 # Error - to be calculated
                                                    ]
                                                   )
            #media_cnt = len(l_media_list)    
            '''Normalize the number of likes and days'''
            l_max_likes = max(l[1] for l in l_media_list)
            l_min_likes = min(l[1] for l in l_media_list)
            l_max_days = max(l[3] for l in l_media_list)
            l_min_days = min(l[3] for l in l_media_list)
                        
            l_normalized_media_list = []
            for val in l_media_list:
                if (l_max_likes - l_min_likes) != 0:
                    val[1] = (val[1] - l_min_likes) / (l_max_likes - l_min_likes)
                else:
                    val[1] = 0
                
                if (l_max_days - l_min_days) != 0:
                    val[3] = (val[3] - l_min_days) / (l_max_days - l_min_days)
                else:
                    val[3] = 0
                l_normalized_media_list.append(val)
            
            '''Sort media by date'''    
            l_normalized_media_list = sorted(l_normalized_media_list, key=lambda x: x[3], reverse = True)
            
            '''Extract feature Date and label Likes to calculate linear regression parameters''' 
            l_linreg_params = []
            l_linreg_results = []
            for val in l_normalized_media_list:
                l_linreg_params.extend([val[3]]) # days
                l_linreg_results.extend([val[1]]) # likes
                
            '''Calculate linear regression quadratic function based on actual likes'''
            l_regression = np.polyfit(l_linreg_params, l_linreg_results, 2)
            l_polynomial = np.poly1d(l_regression)
            l_predictions = l_polynomial(l_linreg_params)
            
            '''Find errors, and write them in l_normalized_media_list'''
            l_cnt = 0
            for val in l_predictions:
                l_error = l_linreg_results[l_cnt] - val
                l_normalized_media_list[l_cnt][4] = l_error
                l_cnt += 1
                
            '''Sort by error value - descending'''
            l_normalized_media_list = sorted(l_normalized_media_list, key=lambda x: x[4], reverse=True)
            
            l_cnt = 1
            l_media_cnt = len(l_normalized_media_list) 
            for val in l_normalized_media_list:
                self.top_photos_list.append([val[0], val[4]])
                if (l_cnt >= self.l_top_n_photos) or (l_cnt >= l_media_cnt):
                    break
                l_cnt += 1

                