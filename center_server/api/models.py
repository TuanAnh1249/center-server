from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False, blank=True, null=True)


    def __str__(self):
        return self.title

class DLModel(models.Model):
    file = models.FileField(blank=False, null=False)
    version = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.version
    