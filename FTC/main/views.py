from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from matplotlib import pylab
from .models import Modules, Questions, UserProfile
import numpy as np
from .forms import UserProfileForm, QuestionForm, ModuleForm


def MakePieChart(request):
        # make a square figure and axes
        pylab.figure(1, figsize=(6, 6))
        username = request.user.username

        # The slices will be ordered and plotted counter-clockwise.
        Gebruiker = request.user.userprofile
        labels = 'Studie', 'Werk', 'Studentenleven'
        fracs = [Gebruiker.weging_stud, Gebruiker.weging_toek,Gebruiker.weging_soc]
        colors = ['gold', 'lightskyblue', 'lightcoral']

        pylab.pie(fracs,
                  labels=labels,
                  colors=colors,
                  shadow=False,
                  startangle=90)

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
        Gebruiker = request.user.userprofile
        if not request.user.is_authenticated():
                return HttpResponseRedirect('/login')
        else:
                Gebruiker = request.user.userprofile
                firstname = Gebruiker.firstname

                # Determine the position of the buttons
                x_origin = 300-10
                y_origin = 300-15
                r = 180
                rad_per = 2*np.pi / 100             # 2 pi / 100 %
                start = .5 * np.pi
                reduce_r = 0.6

                # Button studie toekomst
                theta_stud_toek = start + Gebruiker.weging_stud * rad_per
                x_stud_toek = int(r * np.cos(theta_stud_toek) + x_origin)
                y_stud_toek = int(-1 * r * np.sin(theta_stud_toek) + y_origin)

                # Button toekomst student
                theta_toek_soc = start + (Gebruiker.weging_toek + Gebruiker.weging_stud) * rad_per
                x_toek_soc = int(r * np.cos(theta_toek_soc) + x_origin)
                y_toek_soc = int(-1 * r * np.sin(theta_toek_soc) + y_origin)

                # Button student studie
                theta_soc_stud = start
                x_soc_stud = int(r * np.cos(theta_soc_stud) + x_origin)
                y_soc_stud = int( -1* r * np.sin(theta_soc_stud) +  y_origin)

                # Button studie
                theta_stud = start + (Gebruiker.weging_stud * rad_per * 0.5)
                x_stud = int(reduce_r * r * np.cos(theta_stud) + x_origin)
                y_stud = int(reduce_r * -1 * r * np.sin(theta_stud) + y_origin)

                # Button toekomst
                theta_toek = start + Gebruiker.weging_stud * rad_per + (Gebruiker.weging_toek * rad_per * 0.5)
                x_toek = int(reduce_r * r * np.cos(theta_toek) + x_origin)
                y_toek = int(reduce_r * -1 * r * np.sin(theta_toek) + y_origin)

                # Button student
                theta_soc = start + (Gebruiker.weging_stud + Gebruiker.weging_toek) * rad_per + (Gebruiker.weging_soc * 0.5 * rad_per)
                x_soc = int(reduce_r * r * np.cos(theta_soc) + x_origin)
                y_soc = int(-1 * reduce_r * r * np.sin(theta_soc) + y_origin)

                username = request.user.username
                firstname = request.user.userprofile.firstname
                bank = request.user.userprofile.bank
                graphic = MakePieChart(request)
                modules = UserProfile.objects.get(firstname=firstname)
                modules = modules.modules.all()
                form = 'main/loggedin.html'
                response = {'full_name': username, 'graphic': graphic, 'bank': bank, 'firstname':firstname, 'x_soc_stud':  x_soc_stud, 'y_soc_stud': y_soc_stud,
                            'x_stud_toek':  x_stud_toek, 'y_stud_toek': y_stud_toek, 'x_toek_soc':  x_toek_soc, 'y_toek_soc': y_toek_soc, 'x_stud': x_stud, 'y_stud': y_stud,
                            'x_toek': x_toek, 'y_toek': y_toek, 'x_soc': x_soc, 'y_soc': y_soc,
                            'modules': modules}
                return render(request, form, response)


def logout(request):
        auth.logout(request)
        return HttpResponseRedirect('/login')


def vragen(request):
        Gebruiker = request.user.userprofile
        firstname = Gebruiker.firstname
        form = 'main/vragen.html'

        question_form = []
        for i in range(12):
                question_form.append(QuestionForm(prefix=str(i), auto_id='id_%s'))

        if request.method == "POST":
                A = Gebruiker
                Aquest = A.questions.all()
                for i in range(12):
                        question_data = QuestionForm(request.POST, prefix=str(i))
                        temp = Questions.objects.create(
                                question =  question_data['question'].value(),
                                answers =  question_data['answers'].value(),
                                gebied =  question_data['gebied'].value())
                        temp.save()
                        A.questions.add(temp)
                return HttpResponseRedirect('/login')

        stud_lijst = Gebruiker.questions.all().filter(gebied="studie")
        stud_lijst = stud_lijst.order_by('-timestamp')[:4]
        toek_lijst = Gebruiker.questions.all().filter(gebied="toekomst")
        toek_lijst = toek_lijst.order_by('-timestamp')[:4]
        soc_lijst = Gebruiker.questions.all().filter(gebied="sociaal")
        soc_lijst = soc_lijst.order_by('-timestamp')[:4]

        response = {'stud_lijst': stud_lijst,
                    'toek_lijst': toek_lijst,
                    'soc_lijst': soc_lijst,
                    'firstname': firstname}
        i = 0
        for items in question_form:
                response['qform' + str(i)] = items
                i += 1

        return render(request, form, response)


def temp(request):
    form = UserProfileForm()
    firstname = request.user.userprofile.firstname
    response = {'form': form, 'firstname': firstname}
    return render(request, 'main/temp.html', response)

def weging(request):
    Gebruiker = request.user.userprofile
    firstname = Gebruiker.firstname
    weging_stud = Gebruiker.weging_stud
    weging_toek = Gebruiker.weging_toek
    weging_soc = Gebruiker.weging_soc

    form = 'main/weging.html'
    response = {'firstname':firstname,
        'weging_stud':weging_stud, 'weging_toek':weging_toek, 'weging_soc':weging_soc,
        }

    return render(request, form, response)
