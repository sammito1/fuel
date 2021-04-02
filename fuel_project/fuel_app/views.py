from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.forms import modelform_factory

from .forms import LoginForm, RegistrationForm, QuoteForm, ProfileForm
from .models import Quote

# Create your views here.

""" 
What are views?

Views are basically just the back-end modules that perform 
calculations/data modifications done before a front-end HTML page is displayed (viewed).
"""

# homepage view
def index(request):
    return render(request, 'index.html')

# login view
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')
        """ still missing some authentication that will be implemented along with database""" 
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# logout view
""" can't really do much here until database is implemented
def logout(request):
    return render(request, 'index.html')
"""

# registration view
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

# fuel quote form view
def quote(request):
    """
    suppose you receive data through the form..
    this function should involve validating such data and
    creating variables to manipulate it, returning some sort of values.
    """
    QuoteForm = modelform_factory(Quote, fields=('user', 'price', 'date', 
    'address', 'gallons', 'total_price',))
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/history')
        else:
            form = QuoteForm()
    else:
        form = QuoteForm()
    return render(request, 'quote.html', {'form': form})

# pricing module view. NOTE: do not implement yet
"""
def price(request):
    pass
"""

# fuel quote history view
def history(request):
    """
    suppose a client goes to their history page..
    if the db was ready, we'd do a SELECT statement from the DB
    and display the table values in the history table.

    however, no db yet, so try to just pre populate the table
    with some values from this function if possible.
    """
    fuel_quote = Quote.objects.all()
    return render(request, 'history.html', {'fuel_quote': fuel_quote})

# profile management view
def profile(request):
    """
    suppose a client wants to view their profile.
    when they go to the profile page, they should be able to:
    1. Display the profile information
    2. Edit the profile information directly in the same page
    this function should validate their info and make sure it fits our requirements
    BEFORE submitting to the db (which is not implemented yet)
    """
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/profile')
    else:
        form = ProfileForm()
    return render(request, 'profile.html', {'form': form})