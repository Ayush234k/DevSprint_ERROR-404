<<<<<<< Updated upstream
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import authentication, permissions

from .serializers import Meal_CancledSerializer,UserCreateSerializer,Meal_Serializer
from .models import Meal_Cancled as Meal_Cancled,UserAccount
from .models import Meals as Meals
from rest_framework.permissions import IsAuthenticated

class hello_world(APIView):
    def post(self,request):
        return Response(request.data["test"])

class User(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserCreateSerializer
    def get_queryset(self):
        queryset = UserAccount.objects.all().order_by('id')
        return queryset
        
import datetime


class Meal_CancledView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = Meal_CancledSerializer
    def get_queryset(self):
        queryset = Meal_Cancled.object.all()
        return queryset
    
    def create(self, request, *args, **kwargs):
        post_data = request.data
        user = UserAccount.objects.get(id=post_data['id'])
        mealcancled = Meal_Cancled.object.create(user_id=user, date_time=datetime.datetime.now(), meal=post_data['meal'])
        mealcancled.save()
        serializer = Meal_CancledSerializer(mealcancled)
        return Response(serializer.data)
from django.shortcuts import get_object_or_404    
class MView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = Meal_Serializer
    def get_queryset(self):
        queryset = Meals.object.all()
        return queryset  
    def retrieve(self, request,**kwargs):
        queryset = Meals.object.filter(meal=kwargs)
        user = get_object_or_404(queryset, meal=kwargs)
        serializer = Meal_Serializer(user)
        return Response(serializer.data)
=======
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import authentication, permissions

from .serializers import Meal_CancledSerializer,UserCreateSerializer,Meal_Serializer
from .models import Meal_Cancled as Meal_Cancled,UserAccount
from .models import Meals as Meals
from rest_framework.permissions import IsAuthenticated

class hello_world(APIView):
    def post(self,request):
        return Response(request.data["test"])

class User(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserCreateSerializer
    def get_queryset(self):
        queryset = UserAccount.objects.all().order_by('id')
        return queryset
        
import datetime


class Meal_CancledView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = Meal_CancledSerializer
    def get_queryset(self):
        queryset = Meal_Cancled.object.all()
        return queryset
    
    def create(self, request, *args, **kwargs):
        post_data = request.data
        user = UserAccount.objects.get(id=post_data['id'])
        mealcancled = Meal_Cancled.object.create(user_id=user, date_time=datetime.datetime.now(), meal=post_data['meal'])
        mealcancled.save()
        serializer = Meal_CancledSerializer(mealcancled)
        return Response(serializer.data)
from django.shortcuts import get_object_or_404    
class MView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = Meal_Serializer
    def get_queryset(self):
        queryset = Meals.object.all()
        return queryset  
    def retrieve(self, request,**kwargs):
        queryset = Meals.object.filter(meal=kwargs)
        user = get_object_or_404(queryset, meal=kwargs)
        serializer = Meal_Serializer(user)
        return Response(serializer.data)
>>>>>>> Stashed changes
   