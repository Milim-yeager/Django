from django.db import models

class Profile(models.Model):
    name = models.CharField()
    email = models.EmailField()
    phone = models.CharField()
    summary = models.TextField()
    skills = models.TextField()
    experience = models.TextField()
    education = models.TextField()


    def __str__(self) -> str:
        return self.name