from django.contrib import admin
from django.urls import path, include
from splitwise.user_views import create_user
from splitwise.group_views import create_group, assign_user
from splitwise.expense_views import create_expense, get_user_transactions

urlpatterns = [
    path('user', create_user),
    path('group', create_group),
    path('assign-user', assign_user),
    path('expense', create_expense),
    path('transactions', get_user_transactions)
]
