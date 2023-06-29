from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    @property
    def balance(self):
        return sum(
            [trx.amount for trx in self.transaction_set.all() if trx.transaction_type]
        ) - sum(
            [trx.amount for trx in self.transaction_set.all() if not trx.transaction_type]
        )

    @property
    def income(self):
        return sum(
            [trx.amount for trx in self.transaction_set.all() if trx.transaction_type]
        )

    @property
    def expense(self):
        return sum(
            [trx.amount for trx in self.transaction_set.all() if not trx.transaction_type]
        )
