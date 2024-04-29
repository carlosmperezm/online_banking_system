from django.shortcuts import render, HttpResponse, render, redirect, reverse
from django.contrib import messages
from .forms import LoginForm
from user.models import User

def home_page(request):
    if not request.session.get('attemps'):
        request.session['attemps'] = 0
    return render(request, 'index.html')



def login(request):
    if request.method == 'GET':
        if not request.session.get('attemps'):
            request.session['attemps'] = 0
        if request.session.get('user'):
            messages.error(request, 'You are already singed in.')
            return redirect('index')
        form = LoginForm()
        context = {'form' : form}
        return render(request, 'login/login.html', context)

    form = LoginForm(request.POST)

    if not form.is_valid():
        return redirect('login')

    if request.session.get('attemps') >= 3 :
        # messages.warning(request, "Too many attemps")
        # return redirect('home_page')
        return render(request, 'errors/attemps_exceed.html')

    username = request.POST['username']
    password = request.POST['password']

    try:
        user = User.objects.get(username = username, password = password)
    except:
        messages.error(request, 'Wrong credentials.')
        request.session['attemps'] += 1
        return redirect('login')

    json_user = {
        'username': user.username,
        'name': user.name,
        'balance': user.balance,
    }
    request.session['user'] = json_user

    return redirect(reverse('index'))

def logout(request):
    if request.session.get('user'):
        request.session.clear()
        messages.success(request, 'You logged out correctly')
    else:
        messages.warning(request, 'You are already logged out')

    return redirect('login')


