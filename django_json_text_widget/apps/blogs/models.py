from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class Article(models.Model):
    title = models.JSONField(_('Article title'), default=dict)

    class Meta:
        verbose_name = _('article')
        verbose_name_plural = _('article')
