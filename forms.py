from django import forms

class RecipeSearchForm(forms.Form):
    query = forms.CharField(max_length=255)
