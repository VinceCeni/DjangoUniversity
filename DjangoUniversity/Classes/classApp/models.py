from django.db import models

class djangoClasses(models.Model):
    courseName = models.CharField(max_length=60, default="", blank=True, null=False)
    instructorName = models.CharField(max_length=60, default="", blank=True, null=False)
    courseNumber = models.FloatField(default=0, null=False)

    objects = models.Manager()

    def __str__(self):
        return self.courseName

# Create your models here.
