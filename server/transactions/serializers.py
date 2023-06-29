from rest_framework import serializers

from transactions.models import Transaction, Category
from transactions.utils import get_total_income, get_total_expense, get_total_balance


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'


class ReportSerializer(serializers.Serializer):
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    total_income = serializers.SerializerMethodField()
    total_expense = serializers.SerializerMethodField()
    total_balance = serializers.SerializerMethodField()

    def get_total_income(self, obj):
        return get_total_income(self.context['user'], obj['start_date'], obj['end_date'])

    def get_total_expense(self, obj):
        return get_total_expense(self.context['user'], obj['start_date'], obj['end_date'])

    def get_total_balance(self, obj):
        return get_total_balance(self.context['user'], obj['start_date'], obj['end_date'])

