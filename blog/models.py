from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=100)
    url = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = "Категории"


class Tag(models.Model):
    title = models.CharField(max_length=100)
    url = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = "Теги"


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    url = models.SlugField(max_length=100, unique=True)
    text = models.TextField(verbose_name="Текст")
    created_up = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Создан")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category', verbose_name='Категирии')
    tag = models.ManyToManyField(Tag, related_name='tag', verbose_name='Тег')
    draft = models.BooleanField('Черновик', default=False)

    def get_absolute_url(self):
        return reverse("post", kwargs={"slug": self.url})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = "Посты"
