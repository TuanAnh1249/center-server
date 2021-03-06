from django.db import models

# Create your models here.
class File(models.Model):
    file = models.FileField(blank=False, null=False)
    version = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.version
    