from django.core.exceptions import ValidationError
from django.test import TestCase
from NewsSection.forms import NewsForm
from NewsSection.validators import only_english_validator


class TestValidator(TestCase):

    def test_only_english_validator_with_valid_should_return_true(self):
        txt = 'sdasdaadsjk,copoqwkemkc31289073-213sdaf.as;dasd;das'
        actual = only_english_validator(txt=txt)
        self.assertIsNotNone(actual)

    def test_only_english_validator_with_kirilic_should_raise_validation_error(self):
        txt= 'дсакиоадсжокяпвелмцоасодк'
        with self.assertRaises(ValidationError) as context:
            context = only_english_validator(txt=txt)
        self.assertTrue('Please Type in English' in context.exception)


