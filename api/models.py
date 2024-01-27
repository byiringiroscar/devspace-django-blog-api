from django.db import models
import uuid
import uuid as uuid_lib

# Create your models here.


class Blog(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False
    )
    title = models.CharField(max_length=100)
    blog_image = models.ImageField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Blog'

    def __str__(self):
        return self.title

