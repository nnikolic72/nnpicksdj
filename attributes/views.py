from django.shortcuts import render
from django.views import generic
from django.http import Http404

from .models import Attribute

# Create your views here.
class IndexView(generic.ListView):
    '''Generic Django ListView extension - displays a list of Attributes'''
    
    template_name = 'attributes/index.html'
    context_object_name = 'attributes_list'
    
    def get_queryset(self):
        return Attribute.objects.order_by('title')
    

def detail(request, p_attribute_name):
    '''View Attribute Details'''    
    
    try:
        '''Get attribute with given name'''
        attribute = Attribute.objects.get(slug=p_attribute_name)
    except Attribute.DoesNotExist:
        raise Http404('No Attribute %s found in our database.' % (p_attribute_name))    
    
    return render(request, 'attributes/attributes_detail.html', 
                  {'attribute': attribute }
                  )    