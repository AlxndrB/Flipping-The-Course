from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required


def login(request):
        return render(request,'registration/login.html',{'error_value':''})


def auth_view(request):
        username = request.POST.get('username', "")
        password = request.POST.get('password', "")
        user = auth.authenticate(username=username, password=password)

        if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect('/loggedin')
        else:
	        return render(request,'registration/login.html',
	                      {'error_value': 'Invalid username or password'})



def loggedin(request):
	if not request.user.is_authenticated():
        	return HttpResponseRedirect('/login')
	else:
        	return render(request,'main/loggedin.html',
                	                  {'full_name': request.user.username})

def logout(request):
        auth.logout(request)
        return HttpResponseRedirect('/login')
