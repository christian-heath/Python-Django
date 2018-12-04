from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, "surveys/index.html")

def process(request):
    if request.method == "POST":
        errors = False
        if len(request.POST['name']) < 0:
            errors = True
        if len(request.POST['comment']) < 0:
            errors = True
        if len(request.POST['comment']) > 155:
            errors = True
        if errors == True:
            return redirect('/')
        elif errors == False:
            if 'num' not in request.session:
                request.session['num'] = 0
            request.session['num'] = request.session['num']+1
            request.session['name'] = request.POST['name']
            request.session['favorite_language'] = request.POST['favorite_language']
            request.session['dojo_location'] = request.POST['dojo_location']
            request.session['comment'] = request.POST['comment']
            request.session['logged'] = True
            return redirect('/result')
    else: return redirect('/')

def result(request):
    if 'logged' not in request.session:
        return redirect('/')
    else:
        del request.session['logged']
        return render(request, 'surveys/result.html')