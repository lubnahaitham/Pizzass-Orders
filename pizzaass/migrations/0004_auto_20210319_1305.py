# Generated by Django 2.2.14 on 2021-03-19 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaass', '0003_auto_20210319_1302'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pizza_rest',
            old_name='info_customer',
            new_name='orders_id',
        ),
    ]