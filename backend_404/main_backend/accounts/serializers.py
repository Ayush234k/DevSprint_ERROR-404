<<<<<<< Updated upstream
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Meal_Cancled, Meals
User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'name','hostel', 'password')
        depth=1
        
class Meal_CancledSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal_Cancled
        fields = "__all__"

class Meal_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Meals
=======
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Meal_Cancled, Meals
User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'name','hostel', 'password')
        depth=1
        
class Meal_CancledSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal_Cancled
        fields = "__all__"

class Meal_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Meals
>>>>>>> Stashed changes
        fields = "__all__"