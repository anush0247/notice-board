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


