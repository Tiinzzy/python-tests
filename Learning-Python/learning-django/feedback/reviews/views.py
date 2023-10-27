from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ReviwForm

# Create your views here.


def review(request):
    # if the form is html and made with htm
    # if request.method == "POST":
    #     entered_username = request.POST['username']

    #     if entered_username == "" and len(entered_username) >= 100:
    #         return render(request, "reviews/review.html", {
    #             "has_error": True
    #         })

    #     print(entered_username)
    #     return HttpResponseRedirect("/thank-you")

    # if the form is made with django form class
    if request.method == "POST":
        form = ReviwForm(request.POST)
        
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect("/thank-you")
    else:
        form = ReviwForm()

    return render(request, "reviews/review.html", {
        "form": form
    })


def thank_you(request):
    return render(request, "reviews/thank_you.html")
