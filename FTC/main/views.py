from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from matplotlib import pylab


def MakePieChart(username):
        # make a square figure and axes
        pylab.figure(1, figsize=(6, 6))

        # The slices will be ordered and plotted counter-clockwise.
        labels = 'Studie', 'Werk', 'Student'
        fracs = [40, 30, 30]
        colors = ['gold', 'lightskyblue', 'lightcoral']

        pylab.pie(fracs,
                  labels=labels,
                  colors=colors,
                  shadow=False,
                  startangle=90)
        # The default startangle is 0, which would start
        # the Frogs slice on the x-axis.  With startangle=90,
        # everything is rotated counter-clockwise by 90 degrees,
        # so the plotting starts on the positive y-axis.

        pylab.savefig('./main/static/main/user_piecharts/' + username + '.png')
        pylab.close()
        string = 'main/user_piecharts/' + username + '.png'
        return string

# ===========  start for views


def login(request):
        if request.user.is_authenticated():
                return HttpResponseRedirect('/loggedin')
        else:
                username = request.POST.get('username', "")
                password = request.POST.get('password', "")
                if username != "":
                        user = auth.authenticate(username=username,
                                                 password=password)
                        if user is not None:
                                auth.login(request, user)
                                return HttpResponseRedirect('/loggedin')
                        else:
                                error = 'invalide username or password!'
                                form = 'registration/login.html'
                                return render(request,
                                              form,
                                              {'error_value': error})
                else:
                        form = 'registration/login.html'
                        error = ''
                        return render(request, form, {'error_value': error})


def loggedin(request):
        if not request.user.is_authenticated():
                return HttpResponseRedirect('/login')
        else:
                username = request.user.username
                graphic = MakePieChart(username)
                form = 'main/loggedin.html'
                response = {'full_name': username, 'graphic': graphic}
                return render(request, form, response)


def logout(request):
        auth.logout(request)
        return HttpResponseRedirect('/login')
