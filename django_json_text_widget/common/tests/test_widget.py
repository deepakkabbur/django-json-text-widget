import pytest
from django.forms import forms

from django_json_text_widget.common.widgets import JsonLocalizationField


class ArticleForm(forms.Form):
    title = JsonLocalizationField(required=True)


@pytest.mark.parametrize(
    'title, validity',
    [({"title_en": "article title"}, True),
     ({"title_fr": "article title in french"}, False)
     ]
)
def test_should_validate_required_field(title, validity):
    form = ArticleForm(data=title)
    assert form.is_valid() is validity


@pytest.mark.parametrize(
    'title, validity, valid_languages',
    [({
          "title_en": "article title",
          "title_fr": "article title in french",
          "title_es": "article title in spanish"},
      True,
      ['_en', '_fr'],
    ), ]
)
def test_should_load_only_configured_languages(title, validity, valid_languages):
    form = ArticleForm(data=title)
    assert form.is_valid() is validity
    assert len(form.fields['title'].fields) == 2
    assert len(form.fields['title'].widget.widgets) == 2
    assert form.fields['title'].widget.widgets_names == valid_languages
