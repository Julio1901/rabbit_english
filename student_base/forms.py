from django import forms

class WordForm(forms.Form):
    word = forms.CharField(label="Type the word here", max_length=50)
    translate = forms.CharField(label="Type the translate here", max_length=50)


