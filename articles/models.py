from django.db import models


# Объясняем Django из чего состоит приложение, что хранить в БД
class Article(models.Model):  # This is first model (называть в ед числе)
    article_title = models.CharField('название статьи', max_length=200)
    article_text = models.TextField('текст статьи')
    pub_date = models.DateField('дата публикации')


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE) # все комментар на сайте будут привязаны к статьям Article
    author_name = models.CharField('имя автора', max_length=45)
    comment_text = models.CharField('текст комментария', max_length=200)
