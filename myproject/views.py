# myproject/views.py
from django.shortcuts import render
import urllib.parse
from django.shortcuts import redirect
from django.conf import settings

def home(request):
    return render(request, 'home.html')

def cv_view(request):
    return render(request, 'cv.html')

def google_login_redirect(request):
    google_auth_url = "https://accounts.google.com/o/oauth2/auth"
    
    params = {
        "client_id": settings.SOCIALACCOUNT_PROVIDERS['google']['APP']['client_id'],
        "redirect_uri": "https://rogerwu-website.onrender.com/accounts/google/login/callback/",
        "response_type": "code",
        "scope": "email profile",
    }

    auth_url = f"{google_auth_url}?{urllib.parse.urlencode(params)}"
    return redirect(auth_url)