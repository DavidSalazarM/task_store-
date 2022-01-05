from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import Http404, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError



@csrf_exempt
def register(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            user = User.objects.create_user(username = data['username'], password = data['password'],email=None)
            user.save()
            message = "User crated succesfully."
            return JsonResponse({"message":message})
        except IntegrityError:
            message = "User already exists"
            return JsonResponse({"message":message})
    else:
        raise Http404()

@csrf_exempt
@login_required
def hola(request):
    if request.method == 'POST':
        return JsonResponse({"message":"hola"})

