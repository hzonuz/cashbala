def get_total_income(user, start_date, end_date):
    return sum([trx.amount for trx in
                user.transaction_set.filter(transaction_type=True, date__gte=start_date, date__lte=end_date)])


def get_total_expense(user, start_date, end_date):
    return sum([trx.amount for trx in
                user.transaction_set.filter(transaction_type=False, date__gte=start_date, date__lte=end_date)])


def get_total_balance(user, start_date, end_date):
    return get_total_income(user, start_date, end_date) - get_total_expense(user, start_date, end_date)
