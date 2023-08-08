from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    picture  = models.ImageField(upload_to="img",blank=True,null=True)
    friends = models.ManyToManyField('Friend', related_name="profile_friend")
    
    def __str__(self):
        return self.name
    
    
class Friend(models.Model):
    profile = models.OneToOneField(Profile,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.profile.name
    
class ChatMessage(models.Model):
    body = models.TextField()
    msg_sender = models.ForeignKey(Profile,on_delete=models.CASCADE, related_name="msg_sender")
    msg_receiver = models.ForeignKey(Profile,on_delete=models.CASCADE, related_name="msg_receiver")
    sent = models.BooleanField(default=False)
    time_sent = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.body
    
