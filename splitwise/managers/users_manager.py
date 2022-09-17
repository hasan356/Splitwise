from splitwise.models import User
from django.db import IntegrityError


class UserManager:

    @staticmethod
    def add_user(email):
        try:
            return User.objects.create(email=email)
        except IntegrityError as e:
            raise e

    @staticmethod
    def get_user_by_email(email):
        try:
            user = User.objects.get(email=email)
            return user
        except User.DoesNotExist as e:
            return None