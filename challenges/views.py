from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
# from django.template.loader import render_to_string
# Create your views here.

monthly_challenges = {
    "january": "this is january",
    "february": "this is February",
    "march": "this is march",
    "april": "this is april",
    "may": "this is may",
    "june": "this is june",
    "julay": "this is julay",
    "desumber": None
}


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound('Invalid month')

    redirect_month = months[month-1]
    ect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(ect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {"text": challenge_text, 'month_name': month})
        # return HttpResponse(challenge_text)
    except:
        raise Http404()
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound( response_data)


def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })
