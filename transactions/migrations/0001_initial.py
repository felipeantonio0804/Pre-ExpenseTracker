# Generated by Django 4.2.3 on 2023-07-08 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Category Name')),
                ('description', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='date transaction')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('note', models.CharField(max_length=250)),
                ('type', models.IntegerField(choices=[(0, 'Expense'), (1, 'Revenue')], default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='transactions.category')),
            ],
        ),
    ]
