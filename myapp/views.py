from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    context = {
        'name':'jj',
        'age': 24,
        'nationality':'spanish',
    }
    return render(request, 'index.html', context)


def counter(request):
    text = request.GET['text']
    amount_of_words = len(text.split())
    context = {
        'text' : text,
        'amount_of_words': amount_of_words,
    }
    return render(request, 'counter.html', context)