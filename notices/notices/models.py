B1;3409;0cfrom django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

class Notices(models.Model):
    receiver_labels = (
        ("E4", "Final Year Students"),
        ("E3", "Third Year Students"),
        ("E2", "Second Year Students"),
        ("All", "All Students"),
    )
    
    title = models.CharField(max_length=100)
    sender = models.ForeignKey(User)
    sentat = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=True)
    receiver = models.CharField(max_length=3,choices=receiver_labels)
    attachment = models.FileField(upload_to='notice_attachments/', blank=True, null=True)
    
    def __unicode__(self):
        return self.title
        

class RolePermissions(models.Model):
    title = models.CharField(max_length=20, unique=True)

    def __unicode__(self):
        return self.title

  
class Roles(models.Model):
    title = models.CharField(max_length=20, unique=True)
    permissions = models.ManyToManyField(RolePermissions)

    def __unicode__(self):
        return self.title
                
class Profile(models.Model):
    
    gender_labels = (
        ("M", "Male"),
        ("F", "Female"),
    )
    
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, unique=True)
    roles = models.ManyToManyField(Roles)
    gender = models.CharField(max_length=1,choices=gender_labels)
    dob = models.DateTimeField(null=True)
    phone_regex = RegexValidator(regex=r'^\d{11}$', message="Mobile No format error")
    mobile = models.CharField(max_length=11,validators=[phone_regex],null=True)
    
    department_labels = (
        ("CSE", "Computer Science and Engineering"),
        ("MME", "Metiral and Matalurgical Engineering"),
        ("CE", "Civil Engineering"),
    )
    
    department = models.CharField(max_length=3,choices=department_labels)
    

    
    def __unicode__(self):
        return self.user.username

