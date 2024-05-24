from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

monthly_challenge = {
    "january": "read a new book",
    "february": "write a daily journal",
    "march": "walk 10,000 steps daily",
    "april": "practice meditation",
    "may": "learn a new skill",
    "june": "drink 8 glasses of water daily",
    "july": "cook a new recipe weekly",
    "august": "declutter your space",
    "september": "start a workout routine",
    "october": "participate in a community event",
    "november": "limit screen time",
    "december": "reflect on the past year"
}

def index(request):
    months= list(monthly_challenge.keys())
    return render(request, "challenges/index.html",{
        "months":months
    })
    

def monthly_challenges_int(request, response,month):
    months = list(monthly_challenge.keys())
    if month > len(months) or month < 1:
        raise Http404("Invalid month number")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenges(request, month):
    try:
        month = month.lower()
        challenge_text = monthly_challenge[month]
        return render(request, "challenges/challenges.html",{
            "month":month.capitalize(),
            "text":challenge_text
        })
    except KeyError:
        raise Http404()
