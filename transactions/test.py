from datetime import date,timedelta

from django.test import TestCase
from .models import Category,Transaction

# Models
class TransactionModelTests(TestCase):

    def test_was_a_recent_transaction_with_future_dates(self):
        '''was a transaction recent if that have a future date, after to date.today()'''
        category = Category(name='Category of test',description='Category of test description')
        category.save()
        future_date = date.today() + timedelta(days=30)
        future_transaction = category.transaction_set.create(date=future_date,amount=200.50,note='Transaction of test')
        self.assertIs(future_transaction.is_recent_date_of_transaction(),False)

# Views