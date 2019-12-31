from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect


def login_view(request):
    auth_form = AuthenticationForm(data=request.POST or None)
    if auth_form.is_valid():
        login(request, auth_form.get_user())
        return redirect('backoffice:index')
    else:
        invalid_data = request.method == 'POST'

    context_data = {
        'form': auth_form,
        'invalid_data': invalid_data,
        'title': 'Login'
    }
    return render(request, 'backoffice/login_view.html', context_data)


def logout_view(request):
    logout(request)
    return redirect('backoffice:login_view')


def index(request):
    return render(request, 'backoffice/index.html')
