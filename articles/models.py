import datetime
from django.db import models

from django.utils import timezone


# Объясняем Django из чего состоит приложение, что хранить в БД
class Article(models.Model):  # This is first model (называть в ед числе)
    article_title = models.CharField('название статьи', max_length=200)
    article_text = models.TextField('текст статьи')
    pub_date = models.DateField('дата публикации')

    def __str__(self):
        return self.article_title

    # покажет отображалась ли статья недавно (напр 7 дней назад)
    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))


class Comment(models.Model):
    article = models.ForeignKey(Article,
                                on_delete=models.CASCADE)  # все комментар на сайте будут привязаны к статьям Article
    author_name = models.CharField('имя автора', max_length=45)
    comment_text = models.CharField('текст комментария', max_length=200)

    def __str__(self):
        return self.author_name
