from django.db import models
from django.contrib.auth import get_user_model

from djmoney.models.fields import MoneyField
from djmoney.models.validators import MaxMoneyValidator, MinMoneyValidator


# User = get_user_model()

class Item(models.Model):
    name = models.CharField(
        verbose_name='Наименование',
        max_length=200,
        blank=False
    )
    description = models.TextField(
        verbose_name='Описание товара',
        max_length=250,
    )
    price = MoneyField(
        verbose_name='Стоимость',
        max_digits=19,
        decimal_places=2,
        default_currency='RUB',
        blank=False,
        validators=[
            MinMoneyValidator(1),
            MaxMoneyValidator(1000000),
            MinMoneyValidator({'RUB': 1}),
            MaxMoneyValidator({'RUB': 1000000}),
            MinMoneyValidator({'EUR': 1, 'USD': 10000}),
            MaxMoneyValidator({'EUR': 1, 'USD': 10000}),
        ]
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['id']

    def __str__(self) -> str:
        return f'{self.name}, {self.price}'
