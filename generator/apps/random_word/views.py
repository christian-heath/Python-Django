from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    if 'num' not in request.session:
        request.session['num'] = 0
    request.session['num'] = request.session['num']+1
    request.session['word'] = get_random_string(length=14)
    return render(request, "random_word/index.html")

def new(request):
    return redirect('/')

def reset(request):
    del request.session['num']
    return redirect('/')