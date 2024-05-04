from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    date_created = models.DateField(auto_now_add=True)
    time_spent = models.FloatField()
    task = models.TextField(max_length=100)

    def __str__(self):
        return f"{self.user, self.date_created, self.time_spent, self.task}"
    
    def datecreated(self):
        return self.date_created.strftime('%B %d %Y')
    

    

