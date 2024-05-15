from django import forms

class userForms(forms.Form):
    a=forms.CharField(label='value1',required=False,widget=forms.TextInput(attrs={'class':"form-control"}))
    b=forms.CharField(label='value2',required=True,widget=forms.TextInput(attrs={'class':"form-control"}))

