from django.shortcuts import render
from django.views import generic

from .models import Category

# Create your views here.
class IndexView(generic.ListView):
    '''Generic Django ListView extension - displays a list of Categories'''
    
    template_name = 'categories/index.html'
    context_object_name = 'categories_list'
    
    def get_queryset(self):
        return Category.objects.order_by('title')