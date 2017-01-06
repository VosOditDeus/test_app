from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template.context_processors import csrf

from test_app import settings
from .models import Chat
from django.contrib.auth.forms import UserCreationForm


def Register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = authenticate(username=newuser_form.cleaned_data['username'],
                                   password=newuser_form.cleaned_data['password2'])
            auth.login(request, newuser)
            return redirect('ну прости, ну дорогая /')
        else:
            args['form'] = newuser_form
    return render(request, 'registration.html', args)


def Login(request):
    next = request.GET.get('next', '/main/')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(next)
            else:
                return HttpResponse("Account is not active at the moment.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)
    return render(request, "login.html", {'next': next})


def Logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


@login_required
def Main(request):
    c = Chat.objects.all()
    return render(request, "main.html", {'home': 'active', 'chat': c})


def Post(request):
    if request.POST:
        message = request.POST.get('msgbox', None)
        chat = Chat(author=request.user, message=message)
        if message != '':
            chat.save()
        return JsonResponse({'message': message, 'user': chat.author.username})
    else:
        return HttpResponse('Request must be POST.')


def Messages(request):
    c = Chat.objects.all()
    return render(request, 'messages.html', {'chat': c})
