from django.shortcuts import render, redirect
from .forms import UserForm


def create_user(request):
    if request.method == 'POST':
        new_user = UserForm(request.POST)
        if new_user.is_valid():
            new_user.save()
            return redirect('user_index')
        else:
            return redirect('create_user')

    else:
        form = UserForm()
        context = {'form': form}
        return render(request, 'user/user_form.html', context)

def user_index(request):
    return render(request, 'user/index.html')

