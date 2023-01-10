<<<<<<< Updated upstream
from collections import defaultdict
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings

class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save()

        return user
    def create_superuser(self, email, password, name):
        user = self.create_user(
            email,
            password=password,
            name=name,
        )
        user.is_staff = True
        user.is_superuser=True
        user.save(using=self._db)
        return user

class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    hostel = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name
    
    def __str__(self):
        return str(self.email)

class MealCancledManager(models.Manager):
    def get_queryset(self):
        return super(MealCancledManager, self).get_queryset()
    
 
class MealManager(models.Manager):
    def get_queryset(self):
        return super(MealManager, self).get_queryset() 
             
class Meals(models.Model):
    CHOICES = (
    ("BreakFast", "BreakFast"),
    ("Lunch", "Lunch"),
    ("Dinner", "Dinner"),)
    CHOICES2 = (
    ("Monday", "Monday"),
    ("Tuesday", "Tuesday"),
    ("Wednesday", "Wednesday"),
    ("Thrusday", "Thrusday"),
    ("Friday", "Friday"),
    ("Saturday", "Saturday"),
    ("Sunday", "Sunday"),)
    hostel = models.CharField(max_length=255)
    day = models.CharField(max_length=255, choices=CHOICES2)
    meal_time = models.CharField(max_length=255, choices=CHOICES, default="")
    meal = models.CharField(max_length=255)
    object = MealManager()
    published = MealManager() 
     
    def __str__(self):
        return str(self.meal)

  
    
class Meal_Cancled(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL ,on_delete=models.CASCADE,default="")
    date_time=models.DateTimeField()
    meal = models.ForeignKey(Meals ,on_delete=models.CASCADE,default="")
    object = MealCancledManager()
    published = MealCancledManager() 
     
    def __str__(self):
=======
from collections import defaultdict
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings

class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save()

        return user
    def create_superuser(self, email, password, name):
        user = self.create_user(
            email,
            password=password,
            name=name,
        )
        user.is_staff = True
        user.is_superuser=True
        user.save(using=self._db)
        return user

class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    hostel = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name
    
    def __str__(self):
        return str(self.email)

class MealCancledManager(models.Manager):
    def get_queryset(self):
        return super(MealCancledManager, self).get_queryset()
    
 
class MealManager(models.Manager):
    def get_queryset(self):
        return super(MealManager, self).get_queryset() 
             
class Meals(models.Model):
    CHOICES = (
    ("BreakFast", "BreakFast"),
    ("Lunch", "Lunch"),
    ("Dinner", "Dinner"),)
    CHOICES2 = (
    ("Monday", "Monday"),
    ("Tuesday", "Tuesday"),
    ("Wednesday", "Wednesday"),
    ("Thrusday", "Thrusday"),
    ("Friday", "Friday"),
    ("Saturday", "Saturday"),
    ("Sunday", "Sunday"),)
    hostel = models.CharField(max_length=255)
    day = models.CharField(max_length=255, choices=CHOICES2)
    meal_time = models.CharField(max_length=255, choices=CHOICES, default="")
    meal = models.CharField(max_length=255)
    object = MealManager()
    published = MealManager() 
     
    def __str__(self):
        return str(self.meal)

  
    
class Meal_Cancled(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL ,on_delete=models.CASCADE,default="")
    date_time=models.DateTimeField()
    meal = models.ForeignKey(Meals ,on_delete=models.CASCADE,default="")
    object = MealCancledManager()
    published = MealCancledManager() 
     
    def __str__(self):
>>>>>>> Stashed changes
        return str(self.user)