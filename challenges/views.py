from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


# def january(request):
#     return HttpResponse("this works !")


# def february(request):
#     return HttpResponse("this works on February !")

def monthly_challenge(request, month):
    reply_text = None
    if month == "january":
        reply_text = "this is january month"
    elif month == "february":
        reply_text = "this is february month"
    elif month == "march":
        reply_text = "this is march"
    else:
        return HttpResponseNotFound(" we are not support this month")

    return HttpResponse(reply_text)
