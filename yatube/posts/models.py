from turtle import title
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model() 

class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    group = models.ForeignKey(
        # Название модели В кавычнках, потому что когда интерпретатор будет
        # выполнять этот код он еще не будет знать о Group, т.к. он объявлен
        # ниже. Но Django добрый, он позволяет обойти это
        # окаймляя модель в кавычки.
        'Group',
        # Разрешает этому полю быть пустым или быть None (null=True)
        blank=True,
        null=True,
        # Это поле обязательное, без него будет ошибка.
        # Оно говорит что делать с Group, при удалении Post.
        on_delete=models.CASCADE,
        related_name='posts',
    )

class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, verbose_name="URL")
    description = models.TextField()

    def __str__(self) -> str:
        return self.title
        
# Create your models here.
