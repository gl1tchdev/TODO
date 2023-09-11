from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}))


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control form-control-lg'}))
    new_password = forms.CharField(label='New password', widget=forms.PasswordInput(attrs={'class': 'form-control '
                                                                                                    'form-control-lg'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control '
                                                                                            'form-control-lg'}))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'class': 'form-control '
                                                                                                    'form-control-lg'}))


    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class UpdateUserForm(UserRegistrationForm):
    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].required = False
        self.fields['email'].required = False
        self.fields['new_password'].required = False

