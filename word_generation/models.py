from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class testResults(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    WPM = models.IntegerField()
    accuracy = models.FloatField()
    timeTaken = models.CharField(max_length = 10)
    testDone = models.DateTimeField()