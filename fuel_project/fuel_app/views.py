from django.http import HttpResponseRedirect
from django.shortcuts import render
# Create your views here.

""" 
What are views?

Views are basically just the back-end calculations/data modifications done before a front-end
HTML page is displayed.
"""

# homepage view
def index(request):
    return render(request, 'index.html')

# login view
def login(request):
    return render(request, 'login.html')

# logout view
def logout(request):
    return render(request, 'index.html')

# registration view
def register(request):
    return render(request, 'register.html')

# fuel quote form view
def quote(request):
    """
    suppose you receive data through the form..
    this function should involve validating such data and
    creating variables to manipulate it, returning some sort of values.
    """
    return render(request, 'quote.html')

# pricing module view. NOTE: do not implement yet
def price(request):
    pass

# fuel quote history view
def history(request):
    """
    suppose a client goes to their history page..
    if the db was ready, we'd do a SELECT statement from the DB
    and display the table values in the history table.

    however, no db yet, so try to just pre populate the table
    with some values from this function if possible.
    """

    return render(request, 'history.html')

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
    return render(request, 'profile.html')