from datetime import date,timedelta

from django.test import TestCase
from .models import Category,Transaction
from django.urls import reverse

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


def create_transaction(category,date,amount,note):
    '''Create a transaction with the sent parameters, associated to the category'''
    return category.transaction_set.create(date=date,amount=amount,note=note)
   
# Views
class TransactionDetailsViewTests(TestCase):
    def setUp(self):
        self.category = Category(name='Category of test',description='Category of test description')
        self.category.save()

    def test_no_transactions_for_category(self):
        '''If there are no any transaction in the category, an appropiate messages is displayed'''
        response = self.client.get(reverse('transactionsApp:details',args=(self.category.id,)))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'No hay transacciones para esta categoría')
        self.assertQuerysetEqual(response.context['transactions'],[])

    def test_no_watch_future_transaction_for_category(self):
        '''If there is a transaction in the category but with future date from today'''
        future_date = date.today() + timedelta(days=1)
        transaction = create_transaction(self.category,date=future_date,amount=200.50,note='Transaction of test')
        
        response = self.client.get(reverse('transactionsApp:details',args=(self.category.id,)))
        self.assertNotIn(transaction,response.context['transactions'])
        #Execute the validations of no transactions for category
        self.test_no_transactions_for_category()

    def test_watch_past_transaction_for_category(self):
        '''If there is a transaction in the category but with past date from today'''
        past_date = date.today() - timedelta(days=1)
        transaction = create_transaction(self.category,date=past_date,amount=200.50,note='Transaction of test')
        
        response = self.client.get(reverse('transactionsApp:details',args=(self.category.id,)))
        self.assertQuerysetEqual(response.context['transactions'],[transaction])

    def test_watch_past__and_future_transactions_for_category(self):
        '''If there are transactions in the category but with one in the past an other in the future'''
        past_date = date.today() - timedelta(days=1)
        future_date = date.today() + timedelta(days=1)
        transaction1 = create_transaction(self.category,date=past_date,amount=200.50,note='Transaction of test 1')
        transaction2 = create_transaction(self.category,date=future_date,amount=200.50,note='Transaction of test 2')
        
        response = self.client.get(reverse('transactionsApp:details',args=(self.category.id,)))
        self.assertQuerysetEqual(response.context['transactions'],[transaction1])

    def test_watch_past_transactions_for_category(self):
        '''If there are transactions in the category but with past date from today'''
        past_date = date.today() - timedelta(days=1)
        transaction1 = create_transaction(self.category,date=past_date,amount=200.50,note='Transaction of test 1')
        transaction2 = create_transaction(self.category,date=past_date,amount=200.50,note='Transaction of test 2')
        
        response = self.client.get(reverse('transactionsApp:details',args=(self.category.id,)))
        self.assertQuerysetEqual(response.context['transactions'],[transaction1,transaction2])

    def test_watch_future_transactions_for_category(self):
        '''If there are transactions in the category but with future date from today'''
        future_date = date.today() + timedelta(days=1)
        transaction1 = create_transaction(self.category,date=future_date,amount=200.50,note='Transaction of test 1')
        transaction2 = create_transaction(self.category,date=future_date,amount=200.50,note='Transaction of test 2')
        
        response = self.client.get(reverse('transactionsApp:details',args=(self.category.id,)))
        self.assertQuerysetEqual(response.context['transactions'],[])

    

