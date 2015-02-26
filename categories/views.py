from django.shortcuts import render
from django.views import generic
from django.http import Http404

from .models import Category

# Create your views here.
class IndexView(generic.ListView):
    '''Generic Django ListView extension - displays a list of Categories'''
    
    template_name = 'categories/index.html'
    context_object_name = 'categories_list'
    
    def get_queryset(self):
        return Category.objects.order_by('title')
    

def detail(request, p_category_name):
    '''View Category Details'''    
    
    try:
        '''Get category with given name'''
        category = Category.objects.get(slug=p_category_name)
        child_categories = Category.objects.filter(parent__slug=p_category_name)
    except Category.DoesNotExist:
        raise Http404('No Photo Category %s found in our database.' % (p_category_name))    
    
    '''To Do - get all photographers in this category'''
    return render(request, 'categories/categories_detail.html', 
                  {'category': category, 'child_categories': child_categories }
                  )    