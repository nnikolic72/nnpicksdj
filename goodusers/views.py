from django.shortcuts import render
from django.http import Http404

from .models import GoodUser


# Create your views here.
def index(request):
    '''Test index page'''
    
    '''Prepare a list of GoodUsers to display in the template index.html'''
    try:
        goodusers_list = GoodUser.objects.order_by('user_name')
    except GoodUser.DoesNotExist:
        raise Http404('No Instagram Talents found in our database.')
            
    '''render is rendered using index.html and data assigned in context'''
    return render(request, 'goodusers/index.html', {'goodusers_list': goodusers_list, })


def detail(request, p_instagram_user_name):
    '''View Good User Details'''
    
    try:
        '''Get user with given Instagram user name'''
        good_user = GoodUser.objects.get(instagram_user_name=p_instagram_user_name)
    except GoodUser.DoesNotExist:
        raise Http404('No Instagram Talents with username %s found in our database.' % (p_instagram_user_name))
    
    
    return render(request, 'goodusers/goodusers_detail.html', {'good_user': good_user})
    