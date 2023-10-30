from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView

from .forms import ReviewForm
from .models import Review

# Create your views here.


class ReviewView(FormView):
    form_class = ReviewForm 
    template_name = "reviews/review.html"
    success_url = "/thank-you"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    # def get(self, request):
    #     form = ReviewForm()
    #     return render(request, "reviews/review.html", {
    #         "form": form
    #     })

    # def post(self, request):
    #     form = ReviewForm(request.POST)

    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect("/thank-you")

    #     return render(request, "reviews/review.html", {
    #         "form": form
    #     })


class ThanYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "We Recieved Your Review!"
        return context


class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    # to only get a sample of quesries with a filter
    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt=4)
    #     return data

class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review



    # only if it is templateview extension
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     review_id = kwargs["id"]
    #     selected_review = Reviw.objects.get(pk=review_id)
    #     context["review"] = selected_review
    #     return context

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


# def thank_you(request):
#     return render(request, "reviews/thank_you.html")
