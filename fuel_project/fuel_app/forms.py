from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, label='',
        widget=forms.TextInput(attrs={'class': 'form-group form-control', 'placeholder':'Username'}))
    password = forms.CharField(max_length=256, label='',
        widget=forms.TextInput(attrs={'class': 'form-group form-control', 'placeholder':'Password'}))

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=20, label='',
        widget=forms.TextInput(attrs={'class': 'form-group form-control', 'placeholder':'Username'}))
    password = forms.CharField(max_length=256, label='',
        widget=forms.TextInput(attrs={'class': 'form-group form-control', 'placeholder':'Password'}))
    confirm_password = forms.CharField(max_length=256, label='',
        widget=forms.TextInput(attrs={'class': 'form-group form-control', 'placeholder':'Confirm password'}))