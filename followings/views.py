from django.shortcuts import render
from django.views.generic.base import TemplateView

from endless_pagination.views import AjaxListView

from followings.models import Following
from categories.models import Category
from photos.models import Photo

# Create your views here.
 
class FollowingsListView(AjaxListView):
    '''Complex version of IndexView'''
    
    template_name = 'followings/index.html'
    page_template = 'followings/index_page.html'
    followings_list = None
    categories_list = None
    photos_dict = {}
    
    def get_template_names(self):
        return self.page_template;
    
    def get(self, request, *args, **kwargs):
        '''Serve GET request'''
        
        #if self.request.is_ajax():
        #    self.template_name = self.page_template
        
        self.photos_dict = {}        
        self.followings_list = Following.objects.order_by('instagram_user_name')
        self.categories_list = Category.objects.filter(parent__isnull=True).order_by('title')
            
        for following in self.followings_list:
            l_following_photos = Photo.objects.filter(following_id=following).order_by('-photo_rating')
            
            if l_following_photos.count() > 0:
                for photo in l_following_photos:
                    if following.id in self.photos_dict.keys():
                        self.photos_dict[following.id].extend([photo])
                    else:
                        self.photos_dict[following.id] = [photo]
                    
        return render(request, self.template_name, {'followings_list': self.followings_list, 
                                                    'categories_list' : self.categories_list,
                                                    'photos_dict': dict(self.photos_dict),
                                                    'page_template': self.page_template,                                                    
                                                    }
                      )
        
class FollowingsDetailView(TemplateView):
    '''View Following Details'''
    
    template_name = 'followings/followings_detail.html'        