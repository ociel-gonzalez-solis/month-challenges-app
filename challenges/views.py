from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenge = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at leat 20 mins every day!",
    "march": "Learn Django for at least 20 min every day",
    "april": "Eat no meat for the entire month!",
    "may": "Eat no meat for the entire month!",
    "june": "Eat no meat for the entire month!",
    "july": "Eat no meat for the entire",
    "august": "Eat no meat for the entire month!",
    "september": "Eat no meat for the entire month!",
    "october": "Eat no meat for the entire",
    "november": "Learn Django for at least 20 min every day",
    "december": None
}

# Create your views here.


def index(req):
    months = list(monthly_challenge.keys())

    return render(req, 'challenges/index.html', {
        "months": months
    })


def challenges_by_number(req, month):
    months = list(monthly_challenge.keys())
    if month > len(months):
        return HttpResponseNotFound("This is not a valid month")

    forward_month = months[month - 1]
    redirect_path = reverse("mc", args=[forward_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenges(req, month):
    try:
        message = monthly_challenge[month]
        return render(req, "challenges/challenge.html", {
            "text": message,
            "month_name": month
        })
    except:
        raise Http404()
