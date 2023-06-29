from django.test import TestCase

from users.models import User
from transactions.models import Transaction, Category, TransactionTypes


class TransactionModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="12345678"
        )

        self.transaction = Transaction.objects.create(
            user=self.user,
            amount=10000,
            description="test",
            category=Category.FOOD,
            transaction_type=TransactionTypes.EXPENSE,
        )

    def test_transaction_model(self):
        self.assertEqual(self.transaction.user, self.user)
        self.assertEqual(self.transaction.amount, 10000)
        self.assertEqual(self.transaction.description, "test")
        self.assertEqual(self.transaction.category, Category.FOOD)
        self.assertEqual(self.transaction.transaction_type, TransactionTypes.EXPENSE)

    def test_transaction_str(self):
        self.assertEqual(str(self.transaction), f"{self.user.username} - 10000")

    def test_transaction_balance(self):
        self.assertEqual(self.user.balance, 10000)
        self.assertEqual(self.user.income, 0)
        self.assertEqual(self.user.expense, 10000)

        Transaction.objects.create(
            user=self.user,
            amount=10000,
            description="test",
            category=Category.FOOD,
            transaction_type=TransactionTypes.INCOME,
        )

        self.assertEqual(self.user.balance, 20000)
        self.assertEqual(self.user.income, 10000)
        self.assertEqual(self.user.expense, 10000)
        