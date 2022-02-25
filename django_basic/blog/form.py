from django import forms

class HeadlineSearch(forms.Form):
    post_headline = forms.CharField(required=False)