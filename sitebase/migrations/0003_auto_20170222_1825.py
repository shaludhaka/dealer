# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-02-22 12:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitebase', '0002_auto_20170222_1159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='growthrating',
            name='upload_date',
        ),
        migrations.RemoveField(
            model_name='growthrating',
            name='user',
        ),
        migrations.RemoveField(
            model_name='instancesrating',
            name='upload_date',
        ),
        migrations.RemoveField(
            model_name='instancesrating',
            name='user',
        ),
        migrations.RemoveField(
            model_name='osdaysrating',
            name='upload_date',
        ),
        migrations.RemoveField(
            model_name='osdaysrating',
            name='user',
        ),
        migrations.RemoveField(
            model_name='recencyrating',
            name='upload_date',
        ),
        migrations.RemoveField(
            model_name='recencyrating',
            name='user',
        ),
        migrations.RemoveField(
            model_name='repaymentoutstandingratio',
            name='upload_date',
        ),
        migrations.RemoveField(
            model_name='repaymentoutstandingratio',
            name='user',
        ),
        migrations.RemoveField(
            model_name='repaymentoutstandingratiorating',
            name='upload_date',
        ),
        migrations.RemoveField(
            model_name='repaymentoutstandingratiorating',
            name='user',
        ),
        migrations.RemoveField(
            model_name='severityrating',
            name='upload_date',
        ),
        migrations.RemoveField(
            model_name='severityrating',
            name='user',
        ),
        migrations.RemoveField(
            model_name='sumoutstanding',
            name='upload_date',
        ),
        migrations.RemoveField(
            model_name='sumoutstanding',
            name='user',
        ),
        migrations.RemoveField(
            model_name='sumrepayment',
            name='upload_date',
        ),
        migrations.RemoveField(
            model_name='sumrepayment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='u1rating',
            name='upload_date',
        ),
        migrations.RemoveField(
            model_name='u1rating',
            name='user',
        ),
        migrations.RemoveField(
            model_name='u1ratio',
            name='upload_date',
        ),
        migrations.RemoveField(
            model_name='u1ratio',
            name='user',
        ),
        migrations.RemoveField(
            model_name='u2rating',
            name='upload_date',
        ),
        migrations.RemoveField(
            model_name='u2rating',
            name='user',
        ),
        migrations.RemoveField(
            model_name='u2ratio',
            name='upload_date',
        ),
        migrations.RemoveField(
            model_name='u2ratio',
            name='user',
        ),
        migrations.RemoveField(
            model_name='vintagerating',
            name='upload_date',
        ),
        migrations.RemoveField(
            model_name='vintagerating',
            name='user',
        ),
        migrations.AlterField(
            model_name='dealerdata',
            name='upload_date',
            field=models.CharField(db_column='upload_date', default=b'22/02/2017::18:25:22', max_length=32),
        ),
        migrations.AlterField(
            model_name='finalratings',
            name='upload_date',
            field=models.CharField(db_column='upload_date', default=b'22/02/2017::18:25:22', max_length=32),
        ),
        migrations.AlterField(
            model_name='paymentdata',
            name='upload_date',
            field=models.CharField(db_column='upload_date', default=b'22/02/2017::18:25:22', max_length=32),
        ),
        migrations.AlterField(
            model_name='salesdata',
            name='upload_date',
            field=models.CharField(db_column='upload_date', default=b'22/02/2017::18:25:22', max_length=32),
        ),
    ]
