import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from splitwise.managers.users_manager import UserManager
from splitwise.managers.expense_manager import ExpenseManager
from splitwise.services.expense_service import ExpenseService
from splitwise.managers.group_manager import GroupManager
from splitwise import utils


@csrf_exempt
def create_expense(request):
    if request.method == 'POST':
        request_body = utils.parse_request_body(request)
        group_name = request_body.get('group_name')
        split_type = request_body.get('expense_type')
        amount = request_body.get('amount')
        created_by = request_body.get('created_by')
        name = request_body.get('name')

        if not name:
            return HttpResponse("expense name is needed in request body", status=400)
        if not group_name:
            return HttpResponse("group name is needed in request body", status=400)
        if not split_type:
            return HttpResponse("split type is needed in request body", status=400)
        if not amount:
            return HttpResponse('amount is needed in request body', status=400)
        if not created_by:
            return HttpResponse('created by is needed in request body', status=400)
        if split_type not in ['EQUAL', 'EXACT']:
            return HttpResponse('Invalid split type', status=400)
        group = GroupManager.get_group_by_name(group_name)
        if not group:
            return HttpResponse("Group does not exist, create group first", status=400)

        user = UserManager.get_user_by_email(created_by)
        if not user:
            return HttpResponse("Created By User does not exist, create user first", status=400)

        try:
            email_user_map = GroupManager.get_users_by_group(group.id)
            split_amount_map = dict()
            if split_type == 'EXACT':
                split_map = request_body.get('split_map')
                if not split_map or type(split_map) != dict:
                    return HttpResponse('Split map not present in request body it should be dictionary', status=400)
                split_amount_map = ExpenseService.validate_and_create_exact_split_map(split_map, email_user_map, amount, created_by)
            elif split_type == 'EQUAL':
                split_amount_map = ExpenseService.create_split_amount_body(amount, email_user_map, created_by)

            expense = ExpenseManager.create_expense(name, user.id, amount)
            ExpenseManager.create_bulk_group_expense(group.id, expense.id, split_amount_map)
            return HttpResponse("Expense has been created", status=200)
        except Exception as e:
            return HttpResponse(str(e), status=500)

    return HttpResponse("Only Post method is allowed", status=405)


@csrf_exempt
def get_user_transactions(request):
    if request.method == 'GET':
        email = request.GET.get('email')
        status = request.GET.get('status', 'pending')

        if not email:
            return HttpResponse("email should be present in params", status=400)
        user = UserManager.get_user_by_email(email)
        if not user:
            return HttpResponse("invalid email present in params", status=400)

        if status not in ['pending', 'settled']:
            return HttpResponse("status should be either pending or settled", status=400)

        try:
            transactions = ExpenseManager.get_user_transactions(user.id, status == 'settled')
            return HttpResponse(json.dumps(transactions, cls=utils.decimal_encoder), status=200)
        except Exception as e:
            print(str(e))
            return HttpResponse("failed to fetch transactions", status=500)
