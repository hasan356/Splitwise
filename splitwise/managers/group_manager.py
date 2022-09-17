from datetime import datetime
from django.db import IntegrityError
from splitwise.models import Group, UserGroup


class GroupManager:

    @staticmethod
    def get_group_by_name(name):
        try:
            group = Group.objects.get(name=name)
            return group
        except Group.DoesNotExist as e:
            return None
        except Exception as e:
            raise e

    @staticmethod
    def create_group(name):
        try:
            Group.objects.create(name=name)
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    @staticmethod
    def assign_user_to_group(user_id, group_id):
        try:
            UserGroup.objects.create(user_id=user_id, group_id=group_id, joined_on=datetime.now())
        except IntegrityError as e:
            raise e
        except Exception as e:
            print(str(e))
            raise e

    @staticmethod
    def get_users_by_group(group_id):
        email_to_user_map = dict()
        group_users = UserGroup.objects.filter(group_id=group_id).values('user__email', 'user_id')
        for group_user in group_users:
            email_to_user_map[group_user['user__email']] = group_user['user_id']
        return email_to_user_map
