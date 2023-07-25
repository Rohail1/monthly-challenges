from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

monthly_challenges_list = {
    "janurary": "Eat no meat for a month",
    "february": "Walk for at least 20 minutes every day !",
    "march": "Learn Django at least 20 minutes every day !",
    "april": "Eat no meat for a month",
    "may": "Walk for at least 20 minutes every day !",
    "june": "Learn Django at least 20 minutes every day !",
    "july": "Eat no meat for a month",
    "august": "Walk for at least 20 minutes every day !",
    "september": "Learn Django at least 20 minutes every day !",
    "october": "Eat no meat for a month",
    "november": "Walk for at least 20 minutes every day !",
    "december": None,
}


def index(request):
    months = list(monthly_challenges_list.keys())
    context = {
        "months": months
    }
    return render(request, "challenges/index.html", context)


def monthly_challenges_by_number(request, month):
    if month > len(monthly_challenges_list):
        return HttpResponseNotFound("This is invalid Month")
    months = list(monthly_challenges_list.keys())
    forward_month = months[month - 1]
    redirect_url = reverse('monthly-challenges', args=[forward_month])
    return HttpResponseRedirect(redirect_url)


def monthly_challenges(request, month):
    try:
        challenge_text = monthly_challenges_list[month]
        context = {
            'text': challenge_text,
            'month': month
        }
        return render(request, "challenges/challenge.html", context)
    except KeyError:
        raise Http404()
    except Exception as ex:
        print(ex)
        return HttpResponseNotFound("<h1>Internal Server Error</h1>")
