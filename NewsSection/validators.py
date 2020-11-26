from django.core.exceptions import ValidationError

allowed_symbols = {chr(x) for x in range(0, 127)}


def only_english_validator(txt):
    for x in txt:
        if x not in allowed_symbols:
            raise ValidationError('Please Type in English')
    return txt

