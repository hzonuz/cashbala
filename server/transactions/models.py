from django.db import models
from django.db.models import IntegerChoices

from users.models import User

class TransactionTypes(IntegerChoices):
    EXPENSE = 0
    INCOME = 1


class Category(IntegerChoices):
    FOOD = 0
    TRANSPORTS = 1
    ENTERTAINMENTS = 2
    GROCERIES = 3
    UTILITIES = 4
    OTHER = 5


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="transaction_set")
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    category = models.IntegerField(choices=Category.choices)
    transaction_type = models.IntegerField(choices=TransactionTypes.choices)

    def __str__(self):
        return f"{self.user.username} - {self.amount}"
