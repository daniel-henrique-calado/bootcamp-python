"""
Anomaly transaction data - A transaction is considered suspicious if 
the amount is greater than $ 10,000 or if it occurs outside of 
business hours (before 9 AM or after 6 PM).

Suspicious transaction -  {'amount': 12000, 'hour': 20} 
"""

TRANSACTION_LIMIT = 10000
BUSINESS_HOUR_INIT = 9
BUSINESS_HOUR_END = 18

try:
    transaction = {'amount': 10000, 'hour': 10}

    if BUSINESS_HOUR_INIT < transaction['hour'] > BUSINESS_HOUR_END or transaction['amount'] > TRANSACTION_LIMIT:
        raise ValueError("Suspicious transaction.")
    
    print("Normal transaction.")
except ValueError as e:
    print(e)