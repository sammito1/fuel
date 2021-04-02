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

class ProfileForm(forms.Form):
    full_name = forms.CharField(max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    address_1 = forms.CharField(max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    address_2 = forms.CharField(max_length=200, required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    state = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=[('al', 'AL'), ('la', 'LA'), ('tx', 'TX')])
    zip_code = forms.IntegerField(min_value=10000, max_value=99999,
        widget=forms.NumberInput(attrs={'class': 'form-control'}))