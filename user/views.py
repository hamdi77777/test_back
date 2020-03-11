from django.shortcuts import render 
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from  user.models import User
from  user.serializers import UserSerializer 
 
 
@csrf_exempt
def users_list(request):
    if request.method == 'GET':
         users = User.objects.all()
         users_serializer =  UserSerializer(users, many=True)
         return JsonResponse(users_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'

@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        #clients_data = JSONParser().parse(request) 
        user_data = {'id':5,'firstname':'salma','email': 'asma@gmail.com','password':'458745'}
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def user_del(request, pk):
    if request.method == 'DELETE':
        user = User.objects.get(pk=pk)
        user.delete()
        # Client.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
@csrf_exempt
def user_role(request, pk):
    if request.method == 'POST':
        user = User.objects.get(pk=pk)
        #role_data = JSONParser().parse(request) 
        user.role="admin"
        user.save()
        # Client.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

