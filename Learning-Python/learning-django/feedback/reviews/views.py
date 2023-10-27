from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View

from .forms import ReviwForm
from .models import Reviw

# Create your views here.


class ReviewView(View):
    def get(self, request):
        form = ReviwForm()
        return render(request, "reviews/review.html", {
            "form": form
        })

    def post(self, request):
        existing_data = Reviw.objects.get(pk=1)
        form = ReviwForm(request.POST, instance=existing_data)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")

        return render(request, "reviews/review.html", {
            "form": form
        })


# def review(request):
#     # if the form is html and made with htm
#     # if request.method == "POST":
#     #     entered_username = request.POST['username']

#     #     if entered_username == "" and len(entered_username) >= 100:
#     #         return render(request, "reviews/review.html", {
#     #             "has_error": True
#     #         })

#     #     print(entered_username)
#     #     return HttpResponseRedirect("/thank-you")

#     # if the form is made with django form class
#     if request.method == "POST":
#         existing_data = Reviw.objects.get(pk=1)
#         form = ReviwForm(request.POST, instance=existing_data)

#         if form.is_valid():
#             # no need to validate if use model form to create a form
#             # review = Reviw(
#             #     user_name=form.cleaned_data['user_name'],
#             #     review_text=form.cleaned_data['review_text'],
#             #     rating=form.cleaned_data['rating'])
#             review.save()
#             return HttpResponseRedirect("/thank-you")
#     else:
#         form = ReviwForm()

#     return render(request, "reviews/review.html", {
#         "form": form
#     })


def thank_you(request):
    return render(request, "reviews/thank_you.html")
