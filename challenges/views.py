from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.

monthly_challenges = {
    "january": "this is january",
    "february": "this is February",
    "march": "this is march",
    "april": "this is april",
    "may": "this is may",
    "june": "this is june",
    "julay": "this is julay"
}


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound('Invalid month')

    redirect_month = months[month]
    return HttpResponseRedirect("/challenges/"+redirect_month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound(" we are not support this month")
