# Generated by Django 3.0.7 on 2020-06-09 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gstbillingapp', '0010_auto_20200319_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='books_reflected',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='inventory_reflected',
            field=models.BooleanField(default=True),
        ),
    ]
