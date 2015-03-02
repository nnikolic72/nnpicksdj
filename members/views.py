from django.shortcuts import render
from django.views.generic.base import TemplateView

from .forms import EmailForm

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