from django.core.validators import validate_slug
from django.core.exceptions import ValidationError, PermissionDenied


def safe_slug(slug):
    try:
        validate_slug(slug)
    except ValidationError:
        raise PermissionDenied("Invalid slug.")
