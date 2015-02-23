from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
#from django.contrib.auth import logout as auth_logout

# Create your views here.
from social_auth import __version__ as version


def home(request):
    """Home view, displays login mechanism"""
    
    if request.user.is_authenticated():
        return HttpResponseRedirect('done')
    else:
        return render_to_response('iguserauth/home.html', {'version': version},
                                  RequestContext(request))


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