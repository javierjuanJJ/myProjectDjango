from django.contrib import messages, auth
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from django.http import HttpResponse

from myapp.models import Feature


# Create your views here.

def index(request):
    # feature1=Feature()
    # feature1.id = 0
    # feature1.name = 'Fast'
    # feature1.details = 'Our service'
    # feature1.is_true = True
    #
    # feature2 = Feature()
    # feature2.id = 0
    # feature2.name = 'Fast'
    # feature2.details = 'Our service'
    # feature2.is_true = True
    #
    # feature3 = Feature()
    # feature3.id = 0
    # feature3.name = 'Fast'
    # feature3.details = 'Our service'
    # feature3.is_true = True
    #
    # feature4 = Feature()
    # feature4.id = 0
    # feature4.name = 'Fast'
    # feature4.details = 'Our service'
    # feature4.is_true = True
    #
    # features=[feature1,feature2,feature3,feature4]
    features = Feature.objects.all()
    context = {
        'features': features,
    }
    return render(request, 'index.html', context)

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already exists')
                return redirect('/register')

            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('/register')
            else:
                user = User.objects.create_user(username=username,email=email,password=password1)
                user.save()
                return redirect('/login')
        else:
            messages.info(request, 'Password not the same')
            return redirect('/register')
    else:
        context = {}
        return render(request, 'register.html', context)

def login(request):

    context = {}

    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']

        user = auth.authenticate(username=username,password=password1)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials invalid')
            return redirect('/login')
    else:
        return render(request, 'login.html',context)


def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    context = {
        'text' : text,
        'amount_of_words': amount_of_words,
    }
    return render(request, 'counter.html', context)


def logout(request):
    auth.logout(request)
    return redirect('/')