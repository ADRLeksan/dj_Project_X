from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from app.models import users

# Create your views here.
@csrf_exempt
def index(request):
    if request.method == "POST":
        user = users()
        user.login = request.POST['login']
        user.password = request.POST['password']
        user.save()
        return render(request, 'index.html', {'msg': 'регистрация успешна'})
    return render(request, 'index.html', {'msg': 'пройдите регистрацию'})

@csrf_exempt
def sign(request):
    try:
        if request.COOKIES['isAuth'] == 'true':
            return redirect('/user')
    except:
        if request.method == 'POST':
            login: str = request.POST['login']
            password: str = request.POST['password']
            for i in users.objects.all():
                if i.login == login and i.password == password:
                    html = redirect('/user')
                    html.set_cookie('isAuth', 'true')
                return html
            return render(request, 'sign.html', {'msg2': 'Неверный логин или пароль'})
        return render(request, 'sign.html')
    return render(request, 'sign.html')

def mercury(request):
    return render(request, 'mercury.html')

def venus(request):
    return render(request, 'venus.html')

def eath(request):
    return render(request, 'eath.html')

def mars(request):
    return render(request, 'mars.html')

@csrf_exempt
def user(request):
    if request.method == "POST":
        html = redirect('/sign')
        html.delete_cookie('isAuth')
        return html
    try:
        if request.COOKIES['isAuth'] == 'true':
            return render(request, 'user.html')
    except:
        return redirect(request, 'sign.html')
