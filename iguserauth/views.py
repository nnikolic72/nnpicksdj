from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.messages.api import get_messages
#from django.contrib.auth import logout as auth_logout

# Create your views here.
from social_auth import __version__ as version

from libs.instagram.tools import InstagramSession
from .models import IGUserAuth



def home(request):
    """Home view, displays login mechanism"""
    
    if request.user.is_authenticated():
        return HttpResponseRedirect('done')
    else:
        return render_to_response('iguserauth/home.html', {'version': version},
                                  RequestContext(request))

def ig(request):
    """Error view"""
    
    code = request.GET.get('code', '')
    if code:
        ig_session = InstagramSession()
        api = ig_session.api
        token = api.exchange_code_for_access_token(code)
        info = token[1]
        users = IGUserAuth.objects.filter(userid=info['id'])
        if users:
            user = users[0]
            user.access_token = token[0]
        else:
            user = IGUserAuth(access_token=token[0],
                                 userid=info['id'],
                                 username=info['username'])
        user.save()
        return render_to_response('iguserauth/index.html', {'code': code},
                                  context_instance=RequestContext(request))
    else:        
        messages = get_messages(request)
        return render_to_response('iguserauth/error.html', {'version': version,
                                             'messages': messages, 'code': code, 'request': request},
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