from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from splitwise.managers.users_manager import UserManager
from splitwise import utils

# Create your views here.

@csrf_exempt
def create_user(request):
    request_body = utils.parse_request_body(request)

    if request.method == 'POST':
        email = request_body.get('email')
        if not email:
            return HttpResponse("email not present in request body", status=400)
        try:
            UserManager.add_user(email)
            return HttpResponse("User has been added", status=200)
        except IntegrityError as e:
            return HttpResponse("Email Already exist", status=400)
        except Exception as e:
            return HttpResponse("Failed to add user", status=500)
    return HttpResponse("Only Post method is allowed", status=405)
