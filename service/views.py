import hashlib
from django.http import Http404, HttpResponseRedirect
from pyexpat import model
from tkinter.messagebox import RETRY
from urllib import response
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from json import dump, dump
from ipware import get_client_ip
# from .model import hosting
from service.model import hosting
import datetime
import json
from django.urls import reverse
import requests
import urllib

from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
import random
import socket
# from .forms import CommentForm


@csrf_exempt
def homepage(request):
    return render(request,'index.html')

# def connect(request,room_id):
        
#     # room_id=ip1+' '+ip2
#         # print(ip1)
#     # for i in ip_list:
#     #     print(i)
#     # if ip_list.count()>1:
#     response=redirect('room_id')
#     return response
ip1=''
ip2=''
def ip_check(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip1 = x_forwarded_for.split(',')[-1].strip()
    else:
        ip1 = request.META.get('REMOTE_ADDR')
    try:
        hosting.objects.get(ip=ip1)
    except hosting.DoesNotExist:             #-----Here My Edit
            ip_address = hosting(status=1,ip=ip1, pub_date=datetime.datetime.now())
            ip_address.save()
            
    try:
        ip_list=hosting.objects.filter(status=1)
        if ip_list:
            ip_list=ip_list.exclude(ip=ip1)
            ip2=random.choice(ip_list)
        
        # connect(request,room_name)
    except:
        print('Error')
    # return render(request,'text.html')
    # return HttpResponse()
    # response = HttpResponse(status=302)
    # response['Location'] = 'redirect/success/'
    # return response
    # return redirect('/success/')
    return HttpResponseRedirect(reverse('room', args=[room_name]))

    # return redirect(reverse("room",kwargs={'instance':str(room_name)}))

# hash_object = hashlib.md5(room_name.encode())
# room_id = hash_object.hexdigest()

    


def page2(request):
    return render(request,'text.html')

def texting(request):
    messages=''
    if request.POST:
        messages=request.POST.get('task')
        print(messages)
        # connect(request)
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
        # req = urllib.request.Request(url, data)
        # response = urllib.request.urlopen(req)
        # result = json.load(response)
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

