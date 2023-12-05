from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField


class Profile(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT
    )

    website = models.URLField(blank=True)
    bio = models.CharField(max_length=240, blank=True)

    def __str__(self):
        return self.user.get_username()


class Tag(models.Model):

    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    descriptioni = models.TextField()

    def __str__(self):
        return self.name


class Photo(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='photos/')
    file_url = models.URLField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Generate the file URL based on the uploaded image path
        if self.image:
            self.file_url = self.image.url
        super(Photo, self).save(*args, **kwargs)

    def __str__(self):
        return f"Photo {self.id}"

class Post(models.Model):
    class Meta:
        ordering = ["-publish_date", "-date_modified"]

    title = models.CharField(max_length=255, unique=True)
    subtitle = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    body = RichTextField()
    meta_description = models.CharField(max_length=150, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)

    author = models.ForeignKey(Profile, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, blank=True)
    categories = models.ManyToManyField(Category, blank=True)
