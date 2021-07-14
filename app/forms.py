from django import forms

class EmailForm(forms.Form):
    text = forms.CharField( widget=forms.Textarea )
    