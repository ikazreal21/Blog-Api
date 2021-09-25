import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from cloudinary.models import CloudinaryField

from PIL import Image, ImageOps
from io import BytesIO
from django.core.files import File


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
    published = models.DateTimeField(default=timezone.now, editable=False)
    status = models.CharField(max_length=10, choices=options, default='published')
    # Need to Compress image for Fast Loading
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    ranid = models.CharField(
        max_length=100, default=uuid.uuid4, editable=False, null=True, blank=True
    )
    objects = models.Manager()
    pubpost = PubPostObject()
    draftpost = DraftPostObject()

    # def save(self, *args, **kwargs):
    #     instance = super(Post, self).save(*args, **kwargs)
    #     img = Image.open(instance.image.path)
    #     img.save(instance.image.path, quality=70, optimize=True)
    #     return instance

    # def save(self, *args, **kwargs):
    #     im = Image.open(self.image)
    #     im = im.convert("RGB")
    #     im = ImageOps.exif_transpose(im)
    #     im_io = BytesIO()
    #     im.save(im_io, "JPEG", quality=70)
    #     print(self.image)
    #     new_image = File(im_io, name=self.image)
    #     self.image = new_image
    #     super().save(*args, **kwargs)

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return f'{self.title} | {str(self.author)}'


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, null=True, blank=True, related_name='comment'
    )
    comment = models.TextField(blank=True)
    ranid = models.CharField(
        max_length=100, default=uuid.uuid4, editable=False, null=True, blank=True
    )
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return f'{str(self.user)} | {self.ranid}'
