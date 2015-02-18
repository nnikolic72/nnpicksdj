from django.shortcuts import render
from django.http import Http404
from django.views import generic

from .models import Photo

# Create your views here.
class IndexView(generic.ListView):
    '''Generic Django ListView extension - displays a list of Photos'''
    
    template_name = 'photos/index.html'
    context_object_name = 'photos_list'
    
    def get_queryset(self):
        return Photo.objects.order_by('instagram_photo_id')