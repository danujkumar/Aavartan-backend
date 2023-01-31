from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import status
import json
import functions

# Create your views here.
@api_view(['POST', 'GET'])
def signup(request, data):
    data = json.loads(data)
    try:
        get = functions.addUser(data)
        if get == 1:
            return HttpResponse(1)
        elif get == 2:
            return HttpResponse(2)
        else:
            return HttpResponse(0)
    except:
        return HttpResponse(0)


@api_view(['POST', 'GET'])
def login(request, data):
    print("HI")
    data = json.loads(data)
    try:
        get = functions.login(data)
        return HttpResponse(get)
    except:
        return HttpResponse(0)
        

@api_view(['POST', 'GET'])
def register(request, data):
    data = json.loads(data)
    print(data)
    try:
        get = functions.register(data)
        return HttpResponse(get)
    except:
        return HttpResponse(0)