# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-02-26 06:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitebase', '0004_auto_20170226_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dealerdata',
            name='upload_date',
            field=models.CharField(db_column='upload_date', default=b'26/02/2017::12:21:42', max_length=32),
        ),
        migrations.AlterField(
            model_name='finalratings',
            name='upload_date',
            field=models.CharField(db_column='upload_date', default=b'26/02/2017::12:21:42', max_length=32),
        ),
        migrations.AlterField(
            model_name='paymentdata',
            name='upload_date',
            field=models.CharField(db_column='upload_date', default=b'26/02/2017::12:21:42', max_length=32),
        ),
        migrations.AlterField(
            model_name='salesdata',
            name='upload_date',
            field=models.CharField(db_column='upload_date', default=b'26/02/2017::12:21:42', max_length=32),
        ),
    ]
