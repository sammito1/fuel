from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, label='',
        widget=forms.TextInput(attrs={'class': 'form-group form-control', 'placeholder':'Username'}),
        error_messages={'required': "Enter a valid username"})
    password = forms.CharField(max_length=256, label='',
        widget=forms.TextInput(attrs={'class': 'form-group form-control', 'placeholder':'Password'}),
        error_messages={'required': 'Enter a valid password'})

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=20, label='',
        widget=forms.TextInput(attrs={'class': 'form-group form-control', 'placeholder':'Username'}),
        error_messages={'required': 'Please enter a valid username'})
    password = forms.CharField(max_length=256, label='',
        widget=forms.TextInput(attrs={'class': 'form-group form-control', 'placeholder':'Password'}))
    confirm_password = forms.CharField(max_length=256, label='',
        widget=forms.TextInput(attrs={'class': 'form-group form-control', 'placeholder':'Confirm password'}))

class QuoteForm(forms.Form):
    gallons = forms.IntegerField(label='Gallons Requested', min_value=0, required=True,
        widget=forms.NumberInput(attrs={'class': 'form-group form-control col-3', 'placeholder': 0}),  
        error_messages={'required': "Please enter a valid number of gallons."})
    address = forms.CharField(max_length=95, label='Delivery Address',
        widget=forms.TextInput(attrs={'class': 'form-group form-control col-3', 'placeholder':'Address'}),
        error_messages={'required': 'Please enter a valid address'})
    delivery_date = forms.DateField(label='Delivery Date', required=True, 
        widget=forms.DateInput(attrs={'class': 'form-group form-control col-3', 'type': 'date'}), 
        error_messages={'required': "Please select a date."})