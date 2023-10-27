from django import forms
from .models import Reviw

# class ReviwForm(forms.Form):
#     user_name = forms.CharField(label="Your Name", max_length=100, error_messages={
#         "required": "Your name must not be empty!",
#         "max_length": "PLease enter a shorter name!"
#     })
#     review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=200)
#     rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)


class ReviwForm(forms.ModelForm):
    class Meta:
        model = Reviw
        fields = '__all__'
        # exclude = ['owner_comment']
        labels = {
            "user_name": "Your Name",
            "review_text": 'Your Feedback',
            "rating": "Your Rating"
        }
        error_messages = {
            "user_name": {
                "required" : "Your name must not be empty!",
                "max_length": "PLease enter a shorter name!"
            }
        }
