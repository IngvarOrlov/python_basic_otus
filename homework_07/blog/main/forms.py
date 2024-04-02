from django import forms


class PostForm(forms.Form):
    name = forms.CharField()
    title = forms.CharField()
    body = forms.CharField()
