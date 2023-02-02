from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import status
import json
import functions

def index(request):
    return HttpResponse(200)

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
def blindCode(request, data):
    data = json.loads(data)
    print(data)
    try:
        get = functions.blindCode(data)
        return HttpResponse(get)
    except:
        return HttpResponse(0)

@api_view(['POST', 'GET'])
def bow(request, data):
    data = json.loads(data)
    print(data)
    try:
        get = functions.bow(data)
        return HttpResponse(get)
    except:
        return HttpResponse(0)

@api_view(['POST', 'GET'])
def hydrolift(request, data):
    data = json.loads(data)
    try:
        get = functions.hydrolift(data)
        return HttpResponse(get)
    except:
        return HttpResponse(0)

@api_view(['POST', 'GET'])
def shipwreck(request, data):
    data = json.loads(data)
    try:
        get = functions.shipwreck(data)
        return HttpResponse(get)
    except:
        return HttpResponse(0)


@api_view(['POST', 'GET'])
def scavengerhunt(request, data):
    data = json.loads(data)
    try:
        get = functions.scavengerhunt(data)
        return HttpResponse(get)
    except:
        return HttpResponse(0)


@api_view(['POST', 'GET'])
def codetag(request, data):
    data = json.loads(data)
    try:
        get = functions.codetag(data)
        return HttpResponse(get)
    except:
        return HttpResponse(0)

@api_view(['POST', 'GET'])
def treasurehunt(request, data):
    data = json.loads(data)
    try:
        get = functions.treasurehunt(data)
        return HttpResponse(get)
    except:
        return HttpResponse(0)

@api_view(['POST', 'GET'])
def animatrix(request, data):
    data = json.loads(data)
    try:
        get = functions.animatrix(data)
        return HttpResponse(get)
    except:
        return HttpResponse(0)
    
@api_view(['POST', 'GET'])
def robotrek(request, data):
    data = json.loads(data)
    try:
        get = functions.robotrek(data)
        return HttpResponse(get)
    except:
        return HttpResponse(0)

@api_view(['POST', 'GET'])
def circutrix(request, data):
    data = json.loads(data)
    try:
        get = functions.circutrix(data)
        return HttpResponse(get)
    except:
        return HttpResponse(0)

@api_view(['POST', 'GET'])
def valorant(request, data):
    data = json.loads(data)
    try:
        get = functions.valorant(data)
        return HttpResponse(get)
    except:
        return HttpResponse(0)

@api_view(['POST', 'GET'])
def bbs(request, data):
    data = json.loads(data)
    try:
        get = functions.bbs(data)
        return HttpResponse(get)
    except:
        return HttpResponse(0)

@api_view(['POST', 'GET'])
def openmic(request, data):
    data = json.loads(data)
    try:
        get = functions.openmic(data)
        return HttpResponse(get)
    except:
        return HttpResponse(0)

@api_view(['POST', 'GET'])
def clickovartan(request, data):
    data = json.loads(data)
    try:
        get = functions.clickovartan(data)
        return HttpResponse(get)
    except:
        return HttpResponse(0)
    
@api_view(['POST', 'GET'])
def speedcubing(request, data):
    data = json.loads(data)
    try:
        get = functions.speedcubing(data)
        return HttpResponse(get)
    except:
        return HttpResponse(0)