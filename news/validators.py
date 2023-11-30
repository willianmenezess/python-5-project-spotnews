from django.core.exceptions import ValidationError


def validate_name(value):
    if len(value) == 0 or len(value) >= 200:
        raise ValidationError(
            'Certifique-se de que o valor tenha no máximo 200'
            f' caracteres (ele possui {len(value)}).')


def validate_title(value):
    list_of_words = value.split(" ")
    if len(list_of_words) < 2:
        raise ValidationError('O título deve conter pelo menos 2 palavras.')


def validate_empty(value):
    if len(value) == 0:
        raise ValidationError('O campo não pode estar vazio')
