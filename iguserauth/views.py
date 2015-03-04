from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.messages.api import get_messages
from django.contrib.auth import logout as auth_logout
#from django.contrib.auth.models import User
#from django.contrib.auth import logout as auth_logout

# Create your views here.
from social_auth import __version__ as version  # @UnresolvedImport

#from members.models import Member


def home(request):
    """Home view, displays login mechanism"""
    
    #l_user_id = User.objects.get(id=request.session._session['_auth_user_id'])
    #l_new_member = Member(user_id__id=l_user_id)
    
    '''Add a member'''
    if request.user.is_authenticated():
        return HttpResponseRedirect('done')
    else:
        return render_to_response('iguserauth/home.html', {'version': version},
                                  RequestContext(request))

def error(request):
    """error view"""
      
    messages = get_messages(request)
    return render_to_response('iguserauth/error.html', {'version': version,
                                         'messages': messages},
                               RequestContext(request))
    

def logout(request):
    """Logs out user"""
    auth_logout(request)
    return HttpResponseRedirect('/')

        
@login_required
def done(request):
    """Login complete view, displays user data"""
    
    ctx = {
        'version': version,
        'last_login': request.session.get('social_auth_last_login_backend')
    }
    return render_to_response('iguserauth/done.html', ctx, RequestContext(request))
        

@login_required    
def index(request):
    """Home view - My account page, displays user data"""
    
    if request.user.is_authenticated():
        return render_to_response('iguserauth/index.html', {'version': version},
                                  RequestContext(request))    
        
        
def form(request):
    if request.method == 'POST' and request.POST.get('username'):
        request.session['saved_username'] = request.POST['username']
        backend = request.session['partial_pipeline']['backend']
        return redirect('socialauth_complete', backend=backend)
    return render_to_response('iguserauth/form.html', {}, RequestContext(request))


def form2(request):
    if request.method == 'POST' and request.POST.get('first_name'):
        request.session['saved_first_name'] = request.POST['first_name']
        backend = request.session['partial_pipeline']['backend']
        return redirect('socialauth_complete', backend=backend)
    return render_to_response('iguserauth/form2.html', {}, RequestContext(request))        