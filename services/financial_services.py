import decimal


def calc_customers_balance(deposits, withdrawals):
    previous_balance = decimal.Decimal(0.00)
    unique_customers = {}
    for deposit in deposits:
        customer_name = deposit['customerName']
        amount = decimal.Decimal(deposit['amount'], )
        time = deposit['time']
        if customer_name in unique_customers:
            unique_customers[customer_name] += amount
        else:
            unique_customers[customer_name] = previous_balance + amount

    for withdrawal in withdrawals:
        customer_name = withdrawal['customerName']
        amount = decimal.Decimal(withdrawal['amount'])
        category = withdrawal['category']
        time = deposit['time']
        if customer_name in unique_customers:
            unique_customers[customer_name] -= amount
        else:
            unique_customers[customer_name] = previous_balance - amount
    return unique_customers
