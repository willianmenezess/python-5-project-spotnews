from django.core.exceptions import ValidationError


def validate_name(value):
    if len(value) == 0 or len(value) >= 200:
        raise ValidationError(
            'Certifique-se de que o valor tenha no máximo 200'
            f' caracteres (ele possui {len(value)}).')
