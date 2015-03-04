from django.shortcuts import render
from django.views.generic.base import TemplateView

from photos.models import Photo
from .forms import EmailForm
from .models import Member

# Create your views here.

class DashboardIndexView(TemplateView):
    '''View Good User Details'''
    
    template_name = 'members/index.html'
    
    def get(self, request, *args, **kwargs):
        '''Serve GET request'''
        
        return render(request, self.template_name, 
                      {'emailform': EmailForm()
                       
                       }
                      )
        
class FeedView(TemplateView):
    '''Member's feed view'''
                    
    template_name = 'members/feed.html'
    
    def get(self, request, *args, **kwargs):
        '''Serve GET request'''
        
        return render(request, self.template_name, 
                      {
                       'x': 'string'
                       
                       }
                      )    
        
class MyBestPhotosView(TemplateView):
    '''Member's feed view'''
                    
    template_name = 'members/mybestphotos.html'

    
    def get(self, request, *args, **kwargs):
        '''Serve GET request'''
        
        l_member = Member.objects.get(user_id__id=request.user.id)
        best_photos = Photo.objects.filter(member_id=l_member).order_by('-photo_rating')
            
        return render(request, self.template_name, 
                      {
                       'best_photos': best_photos
                       
                       }
                      )         