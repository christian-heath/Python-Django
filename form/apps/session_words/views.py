from django.shortcuts import render, HttpResponse, redirect
from time import localtime, strftime

def index(request):
    return render(request, "session_words/index.html")

def add(request):
    if request.method == 'POST':
        if 'words' not in request.session:
            request.session['words']=[]
        temp_list = request.session['words']
        if 'big_font' in request.POST:
            showbig = '25pt'
        else:
            showbig = '12pt'
        temp_list.append({"word": request.POST['word'], "color": request.POST['color'], "showbig": showbig, "time": strftime("%a, %d %b %Y %H:%M:%S", localtime())})
        request.session['words'] = temp_list
        return redirect('/session_words')
    else:
        return redirect('/session_words')

def clear(request):
    del request.session['words']
    return redirect('/session_words')