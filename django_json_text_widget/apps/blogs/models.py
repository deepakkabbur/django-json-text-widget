from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.JSONField('Article title', default=dict)

    class Meta:
        verbose_name = "article"
        verbose_name_plural = "articles"
