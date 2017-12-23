# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-19 17:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0002_auto_20171219_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='beard_model',
            field=models.CharField(choices=[('admiral', 'адмирал'), ('woodchoper', 'лесоруб'), ('polar', 'полярник'), ('merchant', 'боярин'), ('elder', 'мудрец')], default='admiral', max_length=100, verbose_name='модель бороды'),
        ),
    ]
