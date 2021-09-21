import uuid
from django.db import models
from django.contrib.auth.models import User


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.TextField(blank=True)
    ranid = models.CharField(
        max_length=100, default=uuid.uuid4, editable=False, null=True, blank=True
    )

    def __str__(self):
        return str(self.user)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255)
    body = models.TextField(blank=True)
    comment = models.ForeignKey(
        Comments, on_delete=models.CASCADE, blank=True, null=True
    )
    ranid = models.CharField(
        max_length=100, default=uuid.uuid4, editable=False, null=True, blank=True
    )

    def __str__(self):
        return self.title + "|" + str(self.user)
