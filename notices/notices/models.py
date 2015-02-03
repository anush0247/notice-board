from django.db import models
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
        
        
#class Roles(models.Model):
#    title = models.CharField(max_length=20)
 #   members = models.ManyToManyField(User)
#
 #   def __unicode__(self):
  #      return self.title

#class RoleMaping(models.Model):
 #   user = models.ForeignKey(User)
  #  
   # roles = models.ForeignKey(Roles)
#
 #   def __unicode__(self):
  #      return "%s is %s" %(self.user, self.roles)
#
#class RolePermissions(models.Model):
 #   name = models.CharField(max_length=50)
  #  roles = models.ManyToManyField(Roles)

class RolePermissions(models.Model):
    title = models.CharField(max_length=20, unique=True)

    def __unicode__(self):
        return self.title

  
class Roles(models.Model):
    title = models.CharField(max_length=20, unique=True)
    #members = models.ManyToManyField(User)
    permissions = models.ManyToManyField(RolePermissions)

    def __unicode__(self):
        return self.title
                
class Profile(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, unique=True)
    roles = models.ManyToManyField(Roles)

    def __unicode__(self):
        return self.name
    
