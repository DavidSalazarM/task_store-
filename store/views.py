from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.db import IntegrityError
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


class Register(APIView):
    def post(self, request, format=None):
        try:
           data = JSONParser().parse(request)
           user = User.objects.create_user(username = data['username'], password = data['password'],email=None)
           Token.objects.create(user=user)
           user.save()
           message = "User crated succesfully."
           return JsonResponse({"message":message})
        except IntegrityError:
           message = "User already exists"
           return JsonResponse({"message":message})


class AuthenticateUser(APIView):
    def post(self, request):
        data = JSONParser().parse(request)
        user = authenticate(username=data['username'], password=data['password'])
        if user:
            token = Token.objects.get(user=user.id)
            access_token = token.key
            return JsonResponse({"access_token":access_token})
        else:
            message = "Incorrect user or password"
            return JsonResponse({"message":message})



