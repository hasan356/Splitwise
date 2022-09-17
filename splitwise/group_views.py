from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from splitwise.managers.users_manager import UserManager
from splitwise.managers.group_manager import GroupManager
from splitwise import utils


@csrf_exempt
def create_group(request):
    if request.method == 'POST':
        request_body = utils.parse_request_body(request)
        name = request_body.get('name')
        if not name:
            return HttpResponse("name not present in request body", status=400)
        try:
            GroupManager.create_group(name)
            return HttpResponse("Group has been added", status=200)
        except IntegrityError as e:
            return HttpResponse("Group already exist", status=400)
        except Exception as e:
            return HttpResponse("Failed to create group", status=500)
    return HttpResponse("Only Post method is allowed", status=405)


@csrf_exempt
def assign_user(request):
    if request.method == 'POST':
        request_body = utils.parse_request_body(request)
        email = request_body.get('user_email')
        name = request_body.get('group_name')
        if not email:
            return HttpResponse("email not present in request body", status=400)
        if not name:
            return HttpResponse("name not present in request bod", status=400)

        user = UserManager.get_user_by_email(email)
        if not user:
            return HttpResponse("User does not exist, create user first", status=400)
        group = GroupManager.get_group_by_name(name)
        if not group:
            return HttpResponse("Group does not exist, create group first", status=400)

        try:
            GroupManager.assign_user_to_group(user.id, group.id)
            return HttpResponse("User has been assigned", status=200)
        except IntegrityError as e:
            return HttpResponse("User already present in the group", status=400)
        except Exception as e:
            return HttpResponse("Failed to assign user to group", status=500)
    return HttpResponse("Only Post method is allowed", status=405)