from datetime import date,timedelta
from django.db import models

class Category(models.Model):
    name = models.CharField('Category Name', max_length=50)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class TypeTransaction(models.IntegerChoices):
    EXPENSE = 0, 'Expense'
    REVENUE = 1, 'Revenue'

class Transaction(models.Model):
    category = models.ForeignKey('Category', on_delete=models.RESTRICT)
    date = models.DateField('date transaction')
    amount = models.DecimalField(max_digits=5,decimal_places=2)
    note = models.CharField(max_length=250)
    type = models.IntegerField(default=TypeTransaction.EXPENSE, choices=TypeTransaction.choices)
    counter = models.IntegerField(default=0)

    def __str__(self):
        if (self.type == TypeTransaction.EXPENSE):
            return "Gasto, {} {}".format(self.note,self.amount)
        elif(self.type == TypeTransaction.REVENUE):
            return "Ingreso, {} {}".format(self.note,self.amount)
        
    def is_recent_date_of_transaction(self):
        '''Return if the transaction date is less than 5 days ago'''
        return date.today() >= self.date >= date.today() - timedelta(days=5)    
