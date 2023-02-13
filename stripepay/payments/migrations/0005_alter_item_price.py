# Generated by Django 4.1.6 on 2023-02-10 15:51

import djmoney.models.fields
import djmoney.models.validators
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0004_alter_item_price_alter_item_price_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default_currency='RUB', max_digits=19, validators=[djmoney.models.validators.MinMoneyValidator(1), djmoney.models.validators.MaxMoneyValidator(1000000), djmoney.models.validators.MinMoneyValidator({'RUB': 1}), djmoney.models.validators.MaxMoneyValidator({'RUB': 1000000}), djmoney.models.validators.MinMoneyValidator({'EUR': 1, 'USD': 1}), djmoney.models.validators.MaxMoneyValidator({'EUR': 1, 'USD': 10000})], verbose_name='Стоимость'),
        ),
    ]
