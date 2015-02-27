from django.shortcuts import render
from django.http import Http404
from django.views import generic

from .models import GoodUser
from photos.models import Photo
from categories.models import Category
from .forms import ContactForm
from django.views.generic.base import TemplateView

# Create your views here.
class IndexView(generic.ListView):
    '''Generic Django ListView extension - displays a list of GoodUsers'''
    
    template_name = 'goodusers/index.html'
    context_object_name = 'goodusers_list'
    
    def get_queryset(self):
        return GoodUser.objects.order_by('user_name')


class GoodUsersListView(TemplateView):
    '''Complex version of IndexView'''
    
    template_name = 'goodusers/index.html'
    goodusers_list = GoodUser.objects.order_by('user_name')
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
            GoodUser.objects.filter(user_category__slug=l_categories.slug).order_by('user_name')
        goodusers_list_child = \
            GoodUser.objects.filter(user_category__parent__slug=l_categories.slug).\
                distinct().order_by('user_name')
        
        child_categories = Category.objects.filter(parent__slug=l_categories.slug)
        
        return render(request, self.template_name, { 'goodusers_list': goodusers_list,
                                                    'goodusers_list_child': goodusers_list_child, 
                                                    'category': x,
                                                    'child_categories': child_categories                                                  
                                                    }
                      )    
    
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
                  {'good_user': good_user, 'photos': photos, 'form':ContactForm()}
                  )
    
