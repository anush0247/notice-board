from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.core.validators import RegexValidator

class UserManager(BaseUserManager):
    def create_user(self, rid, email, date_of_birth, gender, first_name, dept, year, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        if not first_name:
            raise ValueError('Users must have a first name')
            
        user = self.model(
            rid = rid,
            email =self.normalize_email(email),
            date_of_birth = date_of_birth,
            gender = gender,
            first_name = first_name,
            dept = dept,
            year = year,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, rid, email, date_of_birth, gender, first_name, dept, year, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            rid,
            email,
            password=password,
            date_of_birth=date_of_birth,
            gender = gender,
            first_name = first_name,
            dept = dept,
            year = year,
        )
        
        user.is_admin = True
        user.save(using=self._db)
        return user


class RUser(AbstractBaseUser):
	
    rid = models.CharField(
        verbose_name = "University ID",
        unique = True,
        max_length = 40
    )
    
    first_name = models.CharField(
        max_length=100,
        verbose_name = "First Name",
    )
    
    last_name = models.CharField(
        max_length=100,
        verbose_name = "Last Name",
        null=True
    )

    email = models.EmailField(
        verbose_name='Email address',
        max_length=255,
        unique=True
    )

    date_of_birth = models.DateField(
        verbose_name = "Date of Birth",
    )
    
    profile_pic = models.FileField(
        upload_to='profile_pic/%Y/%m/%d',
        blank=True,
        null=True,
        verbose_name="Profile Picture",
        default = 'profile_pic/default.jpg',
    )

    gender_labels = (
        ("M", "Male"),
        ("F", "Female"),
    )
    
    gender = models.CharField(
        max_length=1,
        choices=gender_labels,
        verbose_name = "Gender",
    )
    
    phone_regex = RegexValidator(
        regex=r'^[0]?[789]{1}\d{9}$',
        message="Mobile No format error"
    )

    mobile = models.CharField(
        max_length=11,
        validators=[phone_regex],
        null=True,
        verbose_name = "Mobile No",
    )
    
    department_labels = (
        ("CSE", "Computer Science and Engineering"),
        ("MME", "Metiral and Matalurgical Engineering"),
        ("CE", "Civil Engineering"),
    )
    
    dept = models.CharField(
        max_length=3,
        choices=department_labels,
        verbose_name="Department Name"
    )

    batch_labels = (
        ("E4", "Engg Final Year"),
        ("E3", "Engg Third Year"),
        ("E2", "Engg Second Year"),
        ("E1", "Engg First Year"),
    )

    batch = models.CharField(
        max_length=2,
        choices=batch_labels,
        verbose_name="Batch",
    )

    year = models.IntegerField(
        max_length = 4,
        verbose_name = "Year"
    )
    
    is_active = models.BooleanField(
        default=True,
        verbose_name = "Is Active User",
    )
    
    is_admin = models.BooleanField(
        default=False,
        verbose_name = "Is Admin",
    )
    
    is_student = models.BooleanField(
        default=True,
        verbose_name = "Is Student",
    )
    
    is_alumini = models.BooleanField(
        default=False,
        verbose_name = "Is Alumini",
    )
    
    objects = UserManager()

    USERNAME_FIELD = 'rid'
    REQUIRED_FIELDS = ['date_of_birth','gender','email','first_name','dept','year']

    def get_full_name(self):
        return "%s %s" %(self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name

    def __str__(self):              # __unicode__ on Python 2
        return self.rid

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user an admin"
        # Simplest possible answer: All admins are staff
        return self.is_admin

