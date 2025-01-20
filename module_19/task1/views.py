from django.shortcuts import render
from .forms import UserRegister
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'masloDzen.html')

def price(request):
    context  = {
        'price': ['Подсолнечное масло (250 мл.) - 280 руб.',
          'Льняное масло (250 мл.) - 310 руб.',
          'Масло грецкого ореха (250 мл.) - 750 руб.',
          'Масло конопляного семени (250 мл.) - 950 руб.']
    }
    return render(request, 'prices_maslo.html', context)

def disc(request):
    return render(request, 'description_maslo.html')


users = ['Lada', 'Nik', 'Varvara']

# Create your views here.
def sign_up_by_django(request):
    info = {}
    if request.method =='POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password == repeat_password and age >= 18 and username not in users:
                users.append(username)
                print(users)
                return HttpResponse(f'Приветствуем, {username}!')
            elif password != repeat_password:
                info['error']='Пароли не совпадают'
                print(info)
                return HttpResponse(f'Пароли не совпадают')
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
                print(info)
                return HttpResponse(f'Вы должны быть старше 18')
            elif username in users:
                info['error'] = 'Пользователь уже существует'
                print(info)
                return HttpResponse(f'Пользователь уже существует')
    else:
        form = UserRegister()
        context = {'info': info, 'form': form}
        return render(request, 'registration_page.html', context)

def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))

        print(f'Пользователь: {username}')
        print(f'Пароль: {password}')
        print(f'Повтор пароля: {repeat_password}')
        print(f'Возвраст: {age}')

        if password == repeat_password and age >= 18 and username not in users:
            users.append(username)
            print(users)
            return HttpResponse(f'Приветствуем, {username}!')
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
            print(info)
            return HttpResponse(f'Пароли не совпадают')
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'
            print(info)
            return HttpResponse(f'Вы должны быть старше 18')
        elif username in users:
            info['error'] = 'Пользователь уже существует'
            print(info)
            return HttpResponse(f'Пользователь уже существует')
    return render(request, 'registration_page.html', info)
