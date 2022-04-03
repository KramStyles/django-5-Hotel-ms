from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from .forms import LoginForm, SignUpForm


def home(request):
    pass


def login(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('acc-home')
            else:
                msg = "Invalid Credentials"
        else:
            msg = "Error validating form"
    context = {'form': form, 'msg': msg}
    return render(request, 'account/login.html', context)


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'User created'
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    context = {
        'form': form, 'msg': msg
    }
    return render(request, 'account/register.html', context)
