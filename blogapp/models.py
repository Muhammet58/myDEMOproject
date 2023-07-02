from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Blogs(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images")
    description = RichTextField(models.TextField)
    is_active = models.BooleanField(default=True)
    is_home = models.BooleanField()
    is_blog = models.BooleanField()
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=False, unique=True, blank=True, editable=False, db_index=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"
