from splitwise.models import Expense, GroupExpense
from datetime import datetime


class ExpenseManager:

    @staticmethod
    def create_expense(name, created_by, amount):
        return Expense.objects.create(name=name, created_by_id=created_by, amount=amount, created_on=datetime.now())

    @staticmethod
    def create_bulk_group_expense(group_id, expense_id, user_split_amount_map):
        group_expenses = list()
        for user_id, amount in user_split_amount_map.items():
            group_expense = GroupExpense(user_id=user_id, group_id=group_id, expense_id=expense_id, is_settled=False, part_amount=amount)
            group_expenses.append(group_expense)
        GroupExpense.objects.bulk_create(group_expenses)

    @staticmethod
    def get_user_transactions(user_id, is_settled):
        expenses = GroupExpense.objects.filter(user_id=user_id, is_settled=is_settled).values('expense__created_on', 'group__name', 'expense__name',
                                                                                                   'expense__amount', 'part_amount')
        transactions_list = list()
        for expense in expenses:
            transaction = {
                "Date": expense['expense__created_on'].strftime("%d/%B"),
                'Group': expense['group__name'],
                'Expense': expense['expense__name'],
                'Amount': expense['expense__amount'],
                'Pending': expense['part_amount']
            }
            transactions_list.append(transaction)
        return transactions_list
