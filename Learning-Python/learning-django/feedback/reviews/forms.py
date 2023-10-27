from django import forms


class ReviwForm(forms.Form):
    user_name = forms.CharField(label="Your Name", max_length=100, error_messages={
        "required": "Your name must not be empty!",
        "max_length": "PLease enter a shorter name!"
    })
