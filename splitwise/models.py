from django.db import models

# Create your models here.


class User(models.Model):
    email = models.EmailField(unique=True, db_index=True)


class Group(models.Model):
    name = models.CharField(max_length=100, db_index=True, unique=True)


class UserGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    joined_on = models.DateTimeField()

    class Meta:
        unique_together = ('user', 'group')


class Expense(models.Model):
    name = models.CharField(max_length=100)
    created_on = models.DateTimeField(db_index=True)
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    amount = models.DecimalField(decimal_places=2, max_digits=10)


class GroupExpense(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    group = models.ForeignKey(Group, null=True, on_delete=models.SET_NULL)
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
    part_amount = models.DecimalField(decimal_places=2, max_digits=10)
    is_settled = models.BooleanField(db_index=True)

    class Meta:
        unique_together = ('user', 'group', 'expense')

