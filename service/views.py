from django.http.response import JsonResponse
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from json import dump
from django.urls import reverse
import requests
import urllib
from django.shortcuts import render
from django.conf import settings
from django.contrib import messages

@csrf_exempt
def homepage(request):
    return render(request,'index.html')

def ip_check(request):
    room_name=1
    return redirect(reverse("room",kwargs={'instance':str(room_name)}))

def page2(request):
    return render(request,'text.html')

def texting(request):
    messages=''
    if request.POST:
        messages=request.POST.get('task')
        return JsonResponse({'messages':messages})
    return render(request,'text.html')

def text(request):
    login(request)
    return render(request,'text.html')


@csrf_protect
def login(request):
    if request.method == 'POST':
        ''' Begin reCAPTCHA validation '''
        recaptcha_response = request.POST.get('g-recaptcha-response')
        values = {
        'secret' : settings.GOOGLE_RECAPTCHA_SECRET_KEY,
        'response' :  recaptcha_response
        }
        data = urllib.parse.urlencode(values).encode("utf-8")
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()

        print(settings.GOOGLE_RECAPTCHA_SECRET_KEY,recaptcha_response)
        ''' End reCAPTCHA validation '''

        if result['success']:
            print('success')
            return True
        else:
            print('fail')
            messages.error(request, 'Invalid reCAPTCHA. Please try again.')
            return False
        
    else:
        return render(request,'text.html')

