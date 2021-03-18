from django import forms

class LoginForm(forms.Form):
<<<<<<< HEAD
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
=======
"""

class QuoteForm(forms.Form):
    gallons = forms.IntegerField(label="gallons", min_value=0, required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}), error_messages={'required': "Please enter a valid number."})
    delivery_date = forms.DateField(label="delivery-date", required=True, widget=forms.DateInput(attrs={'class': 'form-control'}, error_messages={'required': "Please select a date."})
>>>>>>> ddf3f6cb3d412016fb5970eca33636bf72f4a883
