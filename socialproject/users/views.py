from http.client import HTTPResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .form import LoginForm


# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return HTTPResponse("Login Successful")
            else:
                return HTTPResponse("Invalid credentials")
    else:
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})