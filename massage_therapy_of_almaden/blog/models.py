from django.db import models
from django.utils.timezone import now
from ckeditor.fields import RichTextField


class BlogPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = RichTextField()
    published = models.BooleanField(default=False)
    created_at = models.DateField(default=now)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} {self.created_at}'
