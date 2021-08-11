from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.fields import  SlugField
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import to_language
from mptt.models import MPTTModel, TreeForeignKey
from django.dispatch import receiver
from django.db.models.signals import post_save

from backend.comments.models import AbstractComment 
from backend.utils.send_mail import send_mail_user_post


class Blogcategory(MPTTModel):
    name = models.CharField("Category", max_length=50)
    published = models.BooleanField("Publish?", default=True)
    parent = TreeForeignKey (
        'self',
        verbose_name ="Parental Category",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children')

    slug = models.SlugField(max_length=100, blank=True, null=True, unique=True)    

    description = models.TextField("Description", max_length=300, default="")

    def  get_absolute_url(self):
        return reverse("list_category", kwargs={"category": self.slug})

    class Meta:
        verbose_name = "Category"    
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    class Tag(models.Model):
        name = models.CharField("Tag", max_length=50, unique=True, null=True)
        slug = models.SlugField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.name

class Post(models.Model):

    author = models.ForeignKey (
        User,
        verbose_name ="Author",
        on_delete=models.CASCADE )

    title = models.CharField('Tema', max_length=500)    
    mini_text = models.TextField('Resume', max_length=5000)
    text = models.TextField('full content', max_length=10000000)
    created_date = models.DateTimeField('Creation Date', auto_now_add=True )    
    published_date = models.DateTimeField(
        "Publication date"
        default=timezone.now,
        blank=True,
        null=True
        )        
    image = models.ImageField("Image"), upload_to="blog/", blank=True)
    tag = models.ManyToManyField(Tag, verbose_name="Ter", blank=True)
    