from django.shortcuts import render, HttpResponse, redirect
from time import localtime, strftime, gmtime

def index(request):
    time = {
        "time": strftime("%a, %d %b %Y %H:%M:%S", localtime())
    }
    # The above dictionary returns the current local time in this format: abbreviated weekday name, day of the month as number, abbreviated month name, year with century as number, hour as number(24-hour clock): minute as number: second as number)  
    return render(request, "display_time/index.html", time)