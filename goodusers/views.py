

from django.shortcuts import render
from django.http import Http404
from django.views import generic
from django.views.generic.base import TemplateView

from social_auth.models import UserSocialAuth  # @UnresolvedImport


from .models import GoodUser
from photos.models import Photo
from categories.models import Category
from .forms import PhotoCommentForm
from libs.instagram.tools import MyLikes, InstagramSession



# Create your views here.
class IndexView(generic.ListView):
    '''Generic Django ListView extension - displays a list of GoodUsers'''
    
    template_name = 'goodusers/index.html'
    context_object_name = 'goodusers_list'
    
    def get_queryset(self):
        return GoodUser.objects.order_by('instagram_user_name')


class GoodUsersListView(TemplateView):
    '''Complex version of IndexView'''
    
    template_name = 'goodusers/index.html'
    goodusers_list = GoodUser.objects.order_by('instagram_user_name')
    categories_list = Category.objects.filter(parent__isnull=True).order_by('title')
    
    def get(self, request, *args, **kwargs):
        '''Serve GET request'''
        
        return render(request, self.template_name, {'goodusers_list': self.goodusers_list, 
                                                    'categories_list' : self.categories_list
                                                    }
                      )

class UsersInCategory(TemplateView):
    '''View of users in specific category'''
     
    template_name = 'goodusers/users_in_category.html'
    l_category = ""
    
    
    def get(self, request, *args, **kwargs):
        '''Serve GET request'''
        self.l_category = kwargs['p_category_name']
        try:        
            l_categories = Category.objects.filter(slug=self.l_category).first()
        except Category.DoesNotExist:
            raise Http404('No Photo Category %s found in our database.' % (self.l_category)) 
            
        x = l_categories.title
        goodusers_list = \
            GoodUser.objects.filter(user_category__slug=l_categories.slug).order_by('instagram_user_name')
        goodusers_list_child = \
            GoodUser.objects.filter(user_category__parent__slug=l_categories.slug).\
                distinct().order_by('instagram_user_name')
        
        child_categories = Category.objects.filter(parent__slug=l_categories.slug)
        
        return render(request, self.template_name, { 'goodusers_list': goodusers_list,
                                                    'goodusers_list_child': goodusers_list_child, 
                                                    'category': x,
                                                    'child_categories': child_categories                                                  
                                                    }
                      )    
    
class GoodUsersDetailView(TemplateView):
    '''View Good User Details'''
    
    template_name = 'goodusers/goodusers_detail.html'
    
    def get(self, request, *args, **kwargs):
        '''Serve GET request'''
        
        '''Get users Instagram token'''
        #request_user_id = request.user.id # get logged users Django user id
        #instance = UserSocialAuth.objects.get(user=request.user, provider='instagram') 
        #token = instance.tokens
        
        self.instagram_user_name = kwargs['p_instagram_user_name']
        
        try:
            '''Get user with given Instagram user name'''
            good_user = GoodUser.objects.get(instagram_user_name=self.instagram_user_name)
        except GoodUser.DoesNotExist:
            raise Http404('No Instagram Talents with username %s found in our database.' % (self.instagram_user_name))
        
        try:
            photos = Photo.objects.filter(good_user_id=good_user.pk).order_by('-photo_rating')
        except Photo.DoesNotExist:
            photos = None
            pass
            #raise Http404('No Instagram photos of username %s found in our database.' % (p_instagram_user_name))
        
        '''Check if user has liked those photos'''
       
        '''Init Instagram session using authenticated user token'''
        tokens = UserSocialAuth.get_social_auth_for_user(request.user).get().tokens
        ig_session = InstagramSession(p_is_admin=False, p_token=tokens['access_token'])
        ig_session.init_instagram_API()

        self.l_instagram_api_limit_start, self.l_instagram_api_limit = \
             ig_session.get_api_limits()
            
        liked_photos = [] 
        for photo in photos:
            my_likes = MyLikes(request.user.username, photo.instagram_photo_id, ig_session )
            has_user_liked_media, no_of_likes = my_likes.has_user_liked_media()       
            if has_user_liked_media:
                liked_photos.extend([photo.instagram_photo_id])
            #x = Photo.objects.filter(id=photo.id)
            photo.instagram_likes = no_of_likes
            photo.save()
        
        self.l_instagram_api_limit_stop, self.l_instagram_api_limit = \
             ig_session.get_api_limits()
             
        self.api_limit_spent = int(self.l_instagram_api_limit_start) - int(self.l_instagram_api_limit_stop)
                     
        return render(request, self.template_name, 
                      {'good_user': good_user, 'photos': photos, 'form':PhotoCommentForm(),
                       'liked_photos': liked_photos, 'api_limit_spent': self.api_limit_spent,
                       'api_limit_current': self.l_instagram_api_limit_stop
                       }
                      )
    
