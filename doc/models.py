from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from datetime import datetime


# Create your models here.

class USERPROFILEMANAGER(BaseUserManager):
    """Manage user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError("User must enter a valid email address")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        """For converting password to hash"""
        user.save()

        return user


    def create_superuser(self, email, name, password):
        """Create a new super user"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save()

        return user


class USERPROFILE(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = USERPROFILEMANAGER()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name


    def __str__(self):
        """Return string representation of our user"""
        return self.email


class PATIENTDETAILS(models.Model):
    """This class is for patient details form"""
    patient_id = models.AutoField(primary_key=True)
    date_time = datetime.now()
    first_name = models.CharField(max_length=125, default="")
    last_name = models.CharField(max_length=125, default="")
    full_name = models.CharField(max_length=250, default="")
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=15, default="")
    age = models.IntegerField(default=0)
    sex = models.CharField(max_length=6, default="")
    address_line1 = models.CharField(max_length=255, default="")
    address_line2 = models.CharField(max_length=255, default="")
    city = models.CharField(max_length=255, default="")
    state = models.CharField(max_length=255, default="")
    country = models.CharField(max_length=255, default="")
    postal_Code = models.CharField(max_length=6, default="")
    disease = models.CharField(max_length=255, default="")
    prescription = models.CharField(max_length=500, default="")
    prescription_date = models.DateField()


    def __str__(self):
        """Return string representation of our user"""
        return self.full_name
