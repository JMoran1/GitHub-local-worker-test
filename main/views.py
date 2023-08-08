from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import LoginForm


@login_required
def home(request):
    return render(request, 'main/home.html')


class CustomLoginView(LoginView):
    template_name = 'main/login.html'
    authentication_form = LoginForm
    redirect_authenticated_user = True

def logout_user(request):
    logout(request)
    return redirect('home')
