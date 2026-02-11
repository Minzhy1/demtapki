from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.db.models import Q
from .models import User, Tovar

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(login=username)

            if user.password == password:
                request.session['user_id'] = user.id
                request.session['user_role'] = user.role.title
                request.session['user_role_id'] = user.role_id
                request.session['user_fio'] = user.fio

                if user.role_id == 1:
                    return redirect('admin_page')
                elif user.role_id == 2:
                    return redirect('manager_page')
                elif user.role_id == 3:
                    return redirect('client_page')
                else:
                    return redirect('guest_page')

            else:
                return render(request, 'avt.html', {'error': 'Неверный пароль'})

        except User.DoesNotExist:
            return render(request, 'avt.html', {'error': 'Пользователь не найден'})

    return render(request, 'avt.html')


def admin_page(request):
    return render(request, 'admin.html')


def manager_page(request):
    return render(request, 'manager.html')


def client_page(request):
    return render(request, 'client.html')


def guest_page(request):
    tovars = Tovar.objects.all().order_by('id')
    for tovar in tovars:
        if tovar.discount > 0:
            tovar.discounted_price = tovar.price * (1 - tovar.discount / 100)
        else:
            tovar.discounted_price = tovar.price
    return render(request, 'guest.html', {'tovars': tovars})


def logout_user(request):
    logout(request)
    return redirect('home')