from django.shortcuts import render
from django.views.generic.base import TemplateView

from friends.models import Friend
from categories.models import Category
from photos.models import Photo

# Create your views here.
class FriendsListView(TemplateView):
    '''Complex version of IndexView'''
    
    
    template_name = 'friends/index.html'
    friends_list = None
    categories_list = None
    photos_dict = {}
    
    def get(self, request, *args, **kwargs):
        '''Serve GET request'''
        
        self.friends_list = Friend.objects.order_by('instagram_user_name')
        self.categories_list = Category.objects.filter(parent__isnull=True).order_by('title')
        self.photos_dict = {}
            
        for friend in self.friends_list:
            l_friend_photos = Photo.objects.filter(friend_id=friend).order_by('-photo_rating')
            for photo in l_friend_photos:
                if friend.id in self.photos_dict.keys():
                    self.photos_dict[friend.id].extend([photo])
                else:
                    self.photos_dict[friend.id] = [photo]
                    
        return render(request, self.template_name, {'friends_list': self.friends_list, 
                                                    'categories_list' : self.categories_list,
                                                    'photos_dict': dict(self.photos_dict)
                                                    }
                      )
        
class FriendsDetailView(TemplateView):
    '''View Friend Details'''
    
    template_name = 'friends/friends_detail.html'        