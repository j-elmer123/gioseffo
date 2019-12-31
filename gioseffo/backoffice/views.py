from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect


def login_view(request):
    print(request.POST)
    form = AuthenticationForm(data=request.POST or None)

    form.fields['username'].widget.attrs['class'] = "form-control"
    form.fields['username'].widget.attrs['type'] = "text"
    form.fields['username'].widget.attrs['placeholder'] = "Username"

    form.fields['password'].widget.attrs['class'] = "form-control"
    form.fields['password'].widget.attrs['type'] = "password"
    form.fields['password'].widget.attrs['placeholder'] = "Password"

    if form.is_valid():
        login(request, form.get_user())
        return redirect('backoffice:index')
    else:
        invalid_data = request.method == 'POST'

    context_data = {
        'form': form,
        'invalid_data': invalid_data,
        'title': 'Login'
    }
    return render(request, 'backoffice/login_view.html', context_data)


def logout_view(request):
    logout(request)
    return redirect('backoffice:login_view')


def index(request):
    return render(request, 'backoffice/index.html')
