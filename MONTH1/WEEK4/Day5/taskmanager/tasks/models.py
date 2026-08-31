from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Status(models.TextChoices):
    ACTIVE="active","Active"
    COMPLETED="completed","Completed"
    ARCHIVED="archived","Archived"

# Create your models here.
class Project(models.Model):
    title= models.CharField(max_length=200)
    description=models.TextField(blank=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="projects",
    )

    status=models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.ACTIVE
    )
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering=["-created_at"]

class Profile(models.Model):
    user=models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile"
        )
    bio=models.TextField(blank=True)
    phone_number=models.CharField(max_length=20,blank=True)

    def __str__(self):
        return self.user.username




    