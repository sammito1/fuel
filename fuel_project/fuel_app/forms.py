from django import forms

"""
class LoginForm(forms.Form):
"""

class QuoteForm(forms.Form):
    gallons = forms.IntegerField(label="gallons", min_value=0, required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}), error_messages={'required': "Please enter a valid number."})
    delivery_date = forms.DateField(label="delivery-date", required=True, widget=forms.DateInput(attrs={'class': 'form-control'}, error_messages={'required': "Please select a date."})