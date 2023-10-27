from django import forms

class ReviwForm(forms.Form):
    user_name = forms.CharField()