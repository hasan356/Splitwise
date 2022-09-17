import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setuProject.settings')
django.setup()

from splitwise.managers.users_manager import UserManager
from splitwise.managers.group_manager import GroupManager
from django.db import IntegrityError


if __name__ == '__main__':
    while True:
        print("Choose one of the following actions (0-3)")
        print("1.Add user\n2.Add group\n3.Assign user to group\n4.Press 0 for exit")
        action = input()
        number = int(action)
        match number:
            case 0:
                print("Exiting the app")
                break
            case 1:
                print("Enter the email of the user")
                email = input()
                try:
                    UserManager.add_user(email)
                    print("{} has been added".format(email))
                except IntegrityError as e:
                    print("User already exist with this email")
            case 2:
                print("Enter the group name for the user")
                name = input()
                GroupManager.create_group(name)
                print("Group {} has been created".format(name))
