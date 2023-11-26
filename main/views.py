from django.shortcuts import render

from utils.InternalData.main import ClientInternal
from django.conf import settings

import urllib3
import requests
import json

# Create your views here.

def index(request):
    ok = None
    error = None
    if request.method == "POST":
        nume = request.POST["name"]
        prenume = request.POST["prenume"]
        mail = request.POST["email"]
        phone_number = request.POST["phone"]
        message = request.POST["message"]
        captcha_response = request.POST["g-recaptcha-response"]
        
        url = settings.URL_CAPTCHA_VERIFY
        values = {
            'secret': settings.SECRET_KEY_CAPTCHA,
            'response': captcha_response,
            'remoteip': ClientInternal.getIPv4(request)     
        }
        
        verify_rs = requests.get(url, params = values, verify = True)
        verify_rs = verify_rs.json()
        status = verify_rs.get("success", False)
        
        if not status:
            error = "Completeaza Captcha"
            return render(request, "landing.html", { 'ok_response' : ok, "error" : error})
        
        ok = "Raspunsul dumneavoastra a fost inregistrat"
        
    return render(request, "landing.html", { 'ok_response' : ok, "error" : error})

#TODO: make a page that checks the user email before sending the data
def check_code(request, data):
    pass