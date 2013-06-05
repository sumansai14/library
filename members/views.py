# Create your views here.
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
#from members.forms import RegistrationForm


def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile/')
    #form = RegistrationForm()
    #context = {'form': form}
    return render_to_response('login.html',None, context_instance=RequestContext(request))

def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect('/books/')  # Redirect to a success page.
        else:
            return HttpResponse("your account is disabled")
            # Return a 'disabled account' error message
    else:
        return HttpResponse("invalid login")
        # Return an 'invalid login' error message.
