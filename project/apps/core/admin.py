from django.contrib.admin import register
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin


UserModel = get_user_model()


@register(UserModel)
class UserAdmin(DjangoUserAdmin):
    """User Admin for Custom User"""
