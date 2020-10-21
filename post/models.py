from django.db import models
from authentication.models import User
# Create your models here.
class question(models.Model):
    topic = models.CharField(max_length=1000)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    pubdate = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.topic

class answer(models.Model):
    content = models.TextField()
    ques = models.ForeignKey(question,on_delete=models.CASCADE)
    writer = models.ForeignKey(User,on_delete=models.CASCADE) 
    pubdate = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.content