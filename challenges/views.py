from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
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
    "december": "Learn Django at least 20 minutes every day !",
}


def index(request):
    list_items = ""
    months = list(monthly_challenges_list.keys())
    for month in months:
        capitalize_month = month.capitalize()
        redirect_url = reverse('monthly-challenges', args=[month])
        list_items += f'<li><a href="{redirect_url}">{capitalize_month}</a></li>'
    response_data = f"<ul> {list_items} </ul>"
    return HttpResponse(response_data)


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
        return HttpResponse(challenge_text)
    except KeyError:
        HttpResponseNotFound("This month is not supported")
