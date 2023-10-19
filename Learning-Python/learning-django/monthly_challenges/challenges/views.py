from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": 'This is 1st month, January',
    "february": 'This is 2nd month, February',
    "march": 'This is 3rd month, March',
    "april": 'This is 4th month, April',
    "may": 'This is 5th month, May',
    "june": 'This is 6th month, June',
    "july": 'This is 7th month, July',
    "august": 'This is 8th month, August',
    "september": 'This is 9th month, September',
    "october": 'This is 10th month, October',
    "november": 'This is 11th month, November',
    "december": 'This is 12th month, December',
    "test": None
}


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    # old version of rendering
    # for month in months:
    #     capitalized_month = month.capitalize()
    #     months_path = reverse("month-challenge", args=[month])
    #     list_items += f"<li><a href=\"{months_path}\">{capitalized_month}</a></li>"

    # response_data = f"<ul>{list_items}</ul>"
    # HttpResponse(response_data)
    return render(request, "challenges/index.html", {'months': months})


def january(request):
    return HttpResponse("This January!")


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month!")

    forward_or_redirect_month = months[month - 1]
    # it will build a path with /challenge and args adds the name of the month or number
    redirect_path = reverse(
        "month-challenge", args=[forward_or_redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        # f"<h1>{challenge_text}</h1>" old response data but down there is the html template version
        # can also do render or render_to_string

        response_data = render(request, "challenges/challenge.html", {
            'text': challenge_text,
            'month_name': month.capitalize()
        })
        return HttpResponse(response_data)
    except:
        # reponse_data = "<h1>This month is not supported!</h1>"
        # response_data = render_to_string("404.html")
        # HttpResponseNotFound(response_data)

        # if use raise for http404, name the html file 404 and also set debug to false but only for deployment
        raise Http404()
