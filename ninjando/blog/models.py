from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Category(models.Model):
    name = models.CharField("Category", max_length=50)
    published = models.BooleanField("Publish?", default=True)
    parent = models.ForeignKey(
        'self',
        verbose_name ="Parental Category",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children')

    class Meta:
        verbose_name = "Category"    
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField("Tag", max_length=50, unique=True, null=True)
    
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
        "Publication date",
        default= timezone.now,
        blank=True,
        null=True,
    
    image = models.ImageField("Image"), upload_to="blog/", blank=True)
    tag = models.ManyToManyField(Tag, verbose_name="Ter", blank=True)
    category = models.ForeignKey(
        Category,
        verbose_name = "Category",
        blank = True,
        null = True,
        on_delete=models.SET_NULL
    )
    published = models.BooleanField("Publish?", default=True)
    viewed = models.IntegerField("Visa", default=0)

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"
        ordering = ["-created_date"]

    def get_category_description(self):
        return self.category.description

    def get_count_comments(self):
        return f"{self.comments.all().count()}"

    def get_comments(self):
        return self.comments.filter(parent=None)

    def __str__(self):
        return self.title


class Comment(models.Model ):
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, verbose_name="News", related_name="Comments", on_delete=models.CASCADE
    )
    parent = models.ForeignKey(
        "self",
        verbose_name="Parent Comment",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='children'
    )

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return "{} - {}".format(self.user, self.post)
