from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import Http404, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser



@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        if User.objects.get(username=data['username']):
            message = "User already exists"
            return JsonResponse({"message":message})
        user = User.objects.create_user(username = data['username'], password = data['password'],email=None)
        user.save()
        message = "User crated succesfully."
        return JsonResponse({"message":message})
    else:
        raise Http404()

