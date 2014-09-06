from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import RequestContext, Context
from django.contrib import messages
from models import EmailUser
from django.views.decorators.csrf import csrf_exempt 
from apiUtils import *
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

@csrf_exempt
def sign_up(request):
    email = request.POST['email']
    password = request.POST['password']
    print email + " " + password
    response = ServiceResponse(None)
    

    UserModel = get_user_model()
    if UserModel.objects.filter(email=email).count():
        response.addError("User already exists")
    if len(password) > MAX_PASSWORD_LEN:
        response.addError("Password too long")
    if len(password) < MIN_PASSWORD_LEN:
        response.addError("Password too short")
    if response.isSuccess:
        UserModel.objects.create_user(email, password)
    return response.to_http_response()

@csrf_exempt
def sign_in(request):
    email = request.POST['email']
    password = request.POST['password']
    response = ServiceResponse(None)
    
    user = authenticate(email=email, password=password)    
    if user:
        login(request, user)
        authToken, _ = Token.objects.get_or_create(user=user)
        print authToken
        response.response = authToken.key
    else:
        response.addError("Authentication failure")
    return response.to_http_response()

@csrf_exempt
@api_view(('POST',))
@permission_classes((IsAuthenticated,))
def new_message(request):
    if request.user.is_authenticated():
        print request.user
    response = ServiceResponse(None)
    return response.to_http_response()

