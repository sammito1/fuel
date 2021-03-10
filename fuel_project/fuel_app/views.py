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
    return render(request, 'quote.html')

# pricing module view
def price(request):
    pass

# fuel quote history view
def history(request):
    return render(request, 'history.html')

# profile management view
def profile(request):
    """
    Feature ideas:
    1. Display the profile information
    2. Edit the profile information directly in the same page
    """
    return render(request, 'profile.html')