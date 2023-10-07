from django.contrib.auth import get_user_model
from django.db import models

TRUNCATE_LENGTH = 30
User = get_user_model()


class Group(models.Model):
    title = models.CharField('Название группы', max_length=200)
    slug = models.SlugField('Слаг', unique=True)
    description = models.TextField('Описание')

    def __str__(self):
        return self.title[:TRUNCATE_LENGTH]


class Post(models.Model):
    text = models.TextField('Текст поста')
    pub_date = models.DateTimeField(
        'Дата публикации', auto_now_add=True,
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Автор',
    )
    image = models.ImageField(
        'Картинка', upload_to='posts/', null=True, blank=True
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Группа'
    )

    class Meta:
        default_related_name = 'posts'

    def __str__(self):
        return self.text[:TRUNCATE_LENGTH]


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Автор'
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, verbose_name='Пост'
    )
    text = models.TextField('Текст комментария')
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True
    )

    class Meta:
        default_related_name = 'comments'

    def __str__(self):
        return (f'Комментарий от {self.author} к посту "{self.post}" :'
                f' {self.text[:TRUNCATE_LENGTH]}')
