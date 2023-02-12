from django.contrib import admin
from django.forms import ModelForm

# Register your models here.
from .models import Article
from django_json_text_widget.common.widgets import JsonLocalizationField



class ArticleForm(ModelForm):
    title = JsonLocalizationField()


class ArticleAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    form = ArticleForm


admin.site.register(Article, ArticleAdmin)
