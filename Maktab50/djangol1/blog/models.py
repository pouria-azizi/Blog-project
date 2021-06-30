from django.db import models


class Post(models.Model):
    created_data = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)
    title = models.CharField(verbose_name='عنوان پست', max_length=100)
    creator = models.ForeignKey('auth.User', verbose_name='کاربر', on_delete=models.PROTECT)
    content = models.TextField(verbose_name='متن')
    intro_image = models.ImageField(verbose_name='عکس مقدمه پست', blank=True, null=True)
    likes = models.IntegerField(default=0)
    categories = models.ManyToManyField('blog.Category')

    def __str__(self):
        return f'{self.title}'


class Category(models.Model):
    """
    Categories for postsf
    """
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=20, unique=True, null=True, blank=False)

    def __str__(self):
        return self.name
