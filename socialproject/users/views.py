from django.shortcuts import render

from .form import LoginForm


# Create your views here.
def user_login(request):
    form = LoginForm(request.POST)
    return render(request, 'users/login.html', {'form': form})