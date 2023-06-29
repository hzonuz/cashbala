from datetime import timedelta

from django.test import TestCase
from rest_framework.authtoken.models import Token

from users.models import User
from transactions.models import Transaction, Category, TransactionTypes
from transactions.utils import get_total_income, get_total_expense, get_total_balance


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
        self.today = self.transaction.date.date()
        self.tomorrow = self.today + timedelta(days=1)

    def test_transaction_model(self):
        self.assertEqual(self.transaction.user, self.user)
        self.assertEqual(self.transaction.amount, 10000)
        self.assertEqual(self.transaction.description, "test")
        self.assertEqual(self.transaction.category, Category.FOOD)
        self.assertEqual(self.transaction.transaction_type, TransactionTypes.EXPENSE)

    def test_transaction_str(self):
        self.assertEqual(str(self.transaction), f"{self.user.username} - 10000")

    def test_transaction_balance(self):
        self.assertEqual(self.user.balance, -10000)
        self.assertEqual(self.user.income, 0)
        self.assertEqual(self.user.expense, 10000)

        Transaction.objects.create(
            user=self.user,
            amount=10000,
            description="test",
            category=Category.FOOD,
            transaction_type=TransactionTypes.INCOME,
        )

        self.assertEqual(self.user.balance, 0)
        self.assertEqual(self.user.income, 10000)
        self.assertEqual(self.user.expense, 10000)

    def test_total_income(self):
        Transaction.objects.create(
            user=self.user,
            amount=10000,
            description="test",
            category=Category.FOOD,
            transaction_type=TransactionTypes.INCOME,
        )

        self.assertEqual(get_total_income(self.user, self.today, self.tomorrow), 10000)

    def test_total_expense(self):
        Transaction.objects.create(
            user=self.user,
            amount=10000,
            description="test",
            category=Category.FOOD,
            transaction_type=TransactionTypes.EXPENSE,
        )

        self.assertEqual(get_total_expense(self.user, self.today, self.tomorrow), 20000)

    def test_total_balance(self):
        Transaction.objects.create(
            user=self.user,
            amount=10000,
            description="test",
            category=Category.FOOD,
            transaction_type=TransactionTypes.INCOME,
        )

        self.assertEqual(get_total_balance(self.user, self.today, self.tomorrow), 0)


class TestReport(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="12345678"
        )

        self.token = Token.objects.create(user=self.user)

        self.transaction = Transaction.objects.create(
            user=self.user,
            amount=10000,
            description="test",
            category=Category.FOOD,
            transaction_type=TransactionTypes.EXPENSE,
        )
        self.today = self.transaction.date.date()
        self.tomorrow = self.today + timedelta(days=1)

    def test_report(self):
        response = self.client.get("/trx/report/v0/",
                                   {"start_date": self.today, "end_date": self.tomorrow},
                                   HTTP_AUTHORIZATION=f"Token {self.token.key}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["total_income"], 0)
        self.assertEqual(response.data["total_expense"], 10000)
        self.assertEqual(response.data["total_balance"], -10000)
