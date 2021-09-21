import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.TextField(blank=True)
    ranid = models.CharField(
        max_length=100, default=uuid.uuid4, editable=False, null=True, blank=True
    )

    def __str__(self):
        return str(self.user)


class Post(models.Model):
    class PubPostObject(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    class DraftPostObject(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='draft')

    options = (('draft', 'Draft'), ('published', 'Published'))

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255)
    body = models.TextField(blank=True)
    # comment = models.ForeignKey(
    #     Comments, on_delete=models.CASCADE, blank=True, null=True
    # )
    published = models.DateTimeField(default=timezone.now, editable=False)
    status = models.CharField(max_length=10, choices=options, default='published')
    ranid = models.CharField(
        max_length=100, default=uuid.uuid4, editable=False, null=True, blank=True
    )
    objects = models.Manager()
    pubpost = PubPostObject()
    draftpost = DraftPostObject()

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return f'{self.title} | {str(self.author)}'
