from django.shortcuts import render, HttpResponse, redirect
from user.models import User
from django.contrib import messages

def index(request):
    user = request.session.get('user')
    if not user:
        messages.warning(request, "You must signing in first.")
        return redirect('login')
    context = {'user':user}
    return render(request, 'transactions/index.html',context )


def view_balance(request):
    user_json = request.session.get('user')
    if not user_json:
        messages.warning(request, "You must signing in first.")
        return redirect('login')
    username = user_json['username']
    user = User.objects.get(username = username)
    context = {'user': user}
    return render(request, 'transactions/view_balance.html',context )


def withdraw(request):
    user_json = request.session.get('user')
    if not user_json:
        messages.warning(request, "You must signing in first.")
        return redirect('login')

    if request.method == 'POST':
        amount = request.POST['amount']
        username = user_json['username']
        user = User.objects.get(username = username)
        new_balance = user.balance - float(amount)
        user.balance = new_balance
        user.save()

        return redirect('index')

    context = {'user': user_json}
    return render(request, 'transactions/withdraw.html',context)


def transfer(request):
    user_json = request.session.get('user')

    if not user_json:
        messages.warning(request, "You must signing in first.")
        return redirect('login')

    if request.method == 'POST':
        amount = request.POST['amount']
        username = user_json['username']
        username = user_json['username']
        user = User.objects.get(username = username)
        new_balance = user.balance - float(amount)
        user.balance = new_balance
        user.save()

        try:
            recipient_username = request.POST['recipient_username']
            recipient = User.objects.get(username = recipient_username)
            new_balance = recipient.balance + float(amount)
            recipient.balance = new_balance
            recipient.save()
        except:
            pass
        messages.success(request, 'Trasaction processed')

        return redirect('index')

    context = {'user': user_json}
    return render(request,'transactions/transfer.html',context)


def deposit(request):
    user_json = request.session.get('user')
    if not user_json:
        messages.warning(request, "You must signing in first.")
        return redirect('login')

    if request.method == 'POST':
        username = user_json['username']
        amount = request.POST['amount']
        user = User.objects.get(username = username)
        new_balance = user.balance + float(amount)
        user.balance = new_balance

        user.save()
        return redirect('index')

    context = {'user': user_json}
    return render(request,'transactions/deposit.html',context)

