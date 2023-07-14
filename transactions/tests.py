from datetime import date,timedelta

from django.test import TestCase
from .models import Category,Transaction

# Models
class TransactionModelTests(TestCase):

    def setUp(self):
        self.category = Category(name='Category of test',description='Category of test description')
        self.category.save()
        #By default today, but modify the attribute for each test
        self.transaction = self.category.transaction_set.create(date=date.today(),amount=200.50,note='Transaction of test')

    def test_was_a_recent_transaction_with_future_dates(self):
        '''was a transaction recent if that have a future date, after to date.today()'''
        future_date = date.today() + timedelta(days=30)
        self.transaction.date = future_date
        self.assertIs(self.transaction.is_recent_date_of_transaction(),False)

    def test_was_a_recent_transaction_with_recent_dates(self):
        '''was a transaction recent if that have a recent date'''
        recent_date = date.today() - timedelta(days=4)
        self.transaction.date = recent_date
        self.assertIs(self.transaction.is_recent_date_of_transaction(),True)

    def test_was_a_recent_transaction_with_past_dates(self):
        '''was a transaction recent if that have a past date'''
        past_date = date.today() - timedelta(days=30)
        self.transaction.date = past_date
        self.assertIs(self.transaction.is_recent_date_of_transaction(),False)
        
# Views