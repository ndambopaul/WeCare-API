from django.conf import settings
from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers


def is_invalid_password(password, repeat_password, user=None):
    """
    check passwords strength and equality
    :param password: string
    :param repeat_password: string
    :param user: User object
    :return error message or None:
    """

    error_messages = {
        "not_match": _("Password and Repeat Password fields must match."),
        "user_match": _("Password can't be match to username."),
        "old_match": _("Password can't be match to old one."),
    }

    if not password or (not password and not repeat_password):
        return

    error_message = ""

    try:
        password_validation.validate_password(
            password=password,
        )
    except serializers.ValidationError as e:
        error_message = e.messages

    if error_message:
        return serializers.ValidationError(error_message)

    if password != repeat_password:
        return serializers.ValidationError(error_messages["not_match"])

    if user is not None:
        if password == str(user):
            return serializers.ValidationError(error_messages["user_match"])
        if user.check_password(password):
            return serializers.ValidationError(error_messages["old_match"])


def check_valid_password(data, user=None):
    invalid_password_message = is_invalid_password(
        data.get("password"), data.get("repeat_password"), user=user
    )

    if invalid_password_message:
        raise serializers.ValidationError(invalid_password_message)


def is_real_email(email_address):
    import requests

    response = requests.get(
        "https://isitarealemail.com/api/email/validate",
        params={"email": email_address},
        headers={"Authorization": "Bearer " + settings.IS_REAL_EMAIL_KEY},
    )

    status = response.json()["status"]
    if status == "valid":
        return True, "email is valid"
    elif status == "invalid":
        return False, "email is invalid."
    return False, "email was unknown"
