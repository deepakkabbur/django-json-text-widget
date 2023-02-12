import logging

from django.forms import MultiWidget, TextInput, MultiValueField, CharField
from django.template.defaultfilters import upper

from django_json_text_widget.config.settings import LANGUAGES, LANGUAGE_CODE

logger = logging.getLogger(__name__)


class JsonLocalizationWidget(MultiWidget):
    template_name = "widgets/json_localization_template.html"

    def decompress(self, value):
        return list(value.values())

    def __init__(self, attrs=None):
        _widgets = {}
        for language in self.get_supported_languages():
            _widgets[language] = TextInput(attrs={'name': language, 'id': language,
                                                  "placeholder": f'Please enter title in {upper(language)} language'})
        super(JsonLocalizationWidget, self).__init__(_widgets, attrs)

    def get_supported_languages(self):
        return list(dict(LANGUAGES).keys())


class JsonLocalizationField(MultiValueField):
    """
    Custom field to renderJSON primary keys into text input
    """
    widget = JsonLocalizationWidget

    def __init__(self, **kwargs):
        # Define one message for all fields.
        error_messages = {
            'incomplete': f'{upper(LANGUAGE_CODE)} is must be required,.',
        }

        fields = tuple(map(
            lambda w: CharField(label=w, required=(w == LANGUAGE_CODE)),
            self.get_supported_languages())
        )

        super().__init__(
            error_messages=error_messages, fields=fields,
            require_all_fields=False, **kwargs
        )

    def compress(self, data_list):
        return dict(zip(self.get_supported_languages(), data_list))

    def get_supported_languages(self):
        return list(dict(LANGUAGES).keys())
