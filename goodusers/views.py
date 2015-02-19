from django.shortcuts import render
from django.http import Http404
from django.views import generic

from .models import GoodUser
from photos.models import Photo

# Create your views here.
class IndexView(generic.ListView):
    '''Generic Django ListView extension - displays a list of GoodUsers'''
    
    template_name = 'goodusers/index.html'
    context_object_name = 'goodusers_list'
    
    def get_queryset(self):
        return GoodUser.objects.order_by('user_name')



def detail(request, p_instagram_user_name):
    '''View Good User Details'''
    
    try:
        '''Get user with given Instagram user name'''
        good_user = GoodUser.objects.get(instagram_user_name=p_instagram_user_name)
    except GoodUser.DoesNotExist:
        raise Http404('No Instagram Talents with username %s found in our database.' % (p_instagram_user_name))
    
    try:
        photos = Photo.objects.filter(good_user_id=good_user.pk).order_by('-photo_rating')
    except Photo.DoesNotExist:
        photos = None
        pass
        #raise Http404('No Instagram photos of username %s found in our database.' % (p_instagram_user_name))
    
    return render(request, 'goodusers/goodusers_detail.html', 
                  {'good_user': good_user, 'photos': photos}
                  )
    