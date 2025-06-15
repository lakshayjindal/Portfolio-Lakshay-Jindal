from django.db import models
from django.utils.text import slugify
# Create your models here.
class contactTable(models.Model):
    s_no = models.AutoField(primary_key=True)
    nameC = models.CharField(max_length=256)
    phoneC = models.CharField( max_length=50)
    emailC = models.EmailField( max_length=254)
    isClient = models.BooleanField()

    def __str__(self):
        return f"{"is Client" if self.isClient else "Not a Client"} -> {self.nameC}" 
    
class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.title