from django import forms


class searchForm(forms.Form):
    query = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
