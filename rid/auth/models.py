from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.core.validators import RegexValidator

class UserManager(BaseUserManager):
    def create_user(self, rid, date_of_birth, gender, first_name,last_name, dept,batch, year, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not first_name:
            raise ValueError('Users must have a first name')

        if not year:
            raise ValueError('Users must have a valid year')
        
            
        user = self.model(
            rid = rid,
            date_of_birth = date_of_birth,
            gender = gender,
            first_name = first_name,
            last_name = last_name,
            dept = dept,
            batch = batch,
            year = year,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_supeRidUser(self, rid, date_of_birth, gender, first_name, last_name, dept, batch, year, password):
        """
        Creates and saves a supeRidUser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            rid,
            password=password,
            date_of_birth=date_of_birth,
            gender = gender,
            first_name = first_name,
            last_name = last_name,
            dept = dept,
            batch = batch,
            year = year,
        )
        
        user.is_admin = True
        user.save(using=self._db)
        return user


class RidUser(AbstractBaseUser):
	
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
        null=True,
        default="",
    )

    date_of_birth = models.DateField(
        verbose_name = "Date of Birth",
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
    
    
    department_labels = (
        ("CSE", "Computer Science"),
        ("MME", "Metrial & Matlurgical"),
        ("CE",  "Civil"),
        ("CHE", "Chemical"),
        ("ECE", "Electronics & Communication"),
        ("ME",  "Mechanical"),
        ("MNG", "Management"),
        ("MAT", "Maths"),
        ("PHY", "Physics"),
        ("CH",  "Chemistry"),
        ("BIO", "Biology"),
        ("LBA", "Libaral Arts"),
        ("IT",  "Information Technolgoy"),
        ("ADM", "Administration"),
    )
    
    dept = models.CharField(
        max_length=3,
        choices=department_labels,
        verbose_name="Dept. Name",
    )

    batch_labels = (
        ("E4", "Final Year, Engg"),
        ("E3", "Third Year, Engg"),
        ("E2", "Second Year, Engg"),
        ("E1", "First Year, Engg"),
        ("P1", "First Year, PUC"),
        ("P2", "Second Year, PUC"),
        ("MT", "Mentor"),
        ("FA", "Faculty"),
        ("ST", "Office Staff"),
        ("LA", "Lab Assistant"),
        ("AL", "Alumini")
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
    
    
    objects = UserManager()

    USERNAME_FIELD = 'rid'
    REQUIRED_FIELDS = ['first_name','last_name','date_of_birth','gender','dept','year','batch']

    def __unicode__(self):
        return unicode(self.rid)

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

class Area(models.Model):
    title = models.CharField(max_length=20, unique=True)

    def __unicode__(self):
        return self.title

class Skill(models.Model):
    title = models.CharField(max_length=20, unique=True)

    def __unicode__(self):
        return self.title

class RolePermission(models.Model):
    title = models.CharField(max_length=20, unique=True)

    def __unicode__(self):
        return self.title


class Role(models.Model):
    title = models.CharField(max_length=20, unique=True)
    permissions = models.ManyToManyField(RolePermission)
    
    def __unicode__(self):
        return self.title


        
class Profile(models.Model):

    phone_regex = RegexValidator(
        regex=r'^[0]?[789]{1}\d{9}$',
        message="Mobile No format error"
    )

    mobile = models.CharField(
        max_length=11,
        validators=[phone_regex],
        null=True,
        blank = True,
        verbose_name = "Mobile No",
    )

    url = models.URLField(
        max_length=40,
        null = True,
        blank = True,
        verbose_name = "Website / URL",
    )

    profile_pic = models.FileField(
        upload_to='profile_pic/%Y/%m/%d',
        blank=True,
        null=True,
        verbose_name="Profile Picture",
        default = 'profile_pic/default.jpg',
    )

    
    email = models.EmailField(
        verbose_name='Email address',
        max_length=255,
        blank = True,
    )

    summary = models.TextField(
        verbose_name="Summary",
        blank=True
    )

    areas = models.ManyToManyField(Areas)
    skills = models.ManyToManyField(Skills)
    
    user = models.OneToOneField(RidUser, unique=True)

    def __unicode__(self):
        return unicode(self.user)


def create_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = Profile.objects.get_or_create(user=instance)

from django.db.models.signals import post_save
post_save.connect(create_profile, sender=RidUser)

class UserRole(models.Model):

    role = models.ForeignKey(Role)

    is_verified = models.BooleanField(
        default=False,
        verbose_name = "Is Admin Verified",
    )
    
    user = models.ForeignKey(RidUser)

    def __unicode__(self):
        return unicode(self.user)
    

class Education(models.Model):
    school = models.CharField(
        verbose_name = "School / College / University",
        max_length = 128,
        null = False,
    )

    period = models.CharField(
        verbose_name = "Time Period of Education",
        max_length = 10,
        null = True,
        blank = True,
    )

    degree = models.CharField(
        verbose_name = "Degree ",
        max_length = 128,
        null = True,
        blank = True,
    )
    
    stream = models.CharField(
        verbose_name = "Field of Study",
        max_length = 10,
        null = True,
        blank = True,
    )

    grade = models.FloatField(
        verbose_name = "Grade",
        null = True,
        blank = True,
    )

    user = models.ForeignKey(RidUser)

    def __unicode__(self):
        return unicode(self.user)

    
class Experience(models.Model):
    
    organization = models.CharField(
        verbose_name = "Organization Name",
        max_length = 128,
        null = True,
        blank = True,
    )

    title = models.CharField(
        verbose_name = "Title or Position",
        max_length = 128,
        null = True,
        blank = True,
    )

    location = models.CharField(
        verbose_name = "Location",
        max_length = 128,
        null = True,
        blank = True,
    )

    period = models.CharField(
        verbose_name = "Time Period",
        max_length = 128,
        null = True,
        blank = True,
    )

    description = models.TextField(
        verbose_name = "Description",
        null = True,
        blank = True,
    )
    
    user = models.ForeignKey(RidUser)
    def __unicode__(self):
        return unicode(self.user)

    
class Achievement(models.Model):

    issuer = models.CharField(
        verbose_name = "Issuing Organization",
        max_length = 128,
        null = True,
        blank = True,
    )

    title = models.CharField(
        verbose_name = "Title or Position",
        max_length = 128,
        null = True,
        blank = True,
    )

    location = models.CharField(
        verbose_name = "Location",
        max_length = 128,
        null = True,
        blank = True,
    )

    period = models.CharField(
        verbose_name = "Time Period",
        max_length = 128,
        null = True,
        blank = True,
    )

    description = models.TextField(
        verbose_name = "Description",
        null = True,
        blank = True,
    )
    
    user = models.ForeignKey(RidUser)

    def __unicode__(self):
        return unicode(self.user)
