# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals
import dateutil.parser
from django.db import models
import time


class SalesData(models.Model):

    index = models.AutoField(primary_key= True)
    dealerid = models.CharField(db_column='dealerId', blank=True,db_index=True,max_length = 32,null=True)  # Field name made lowercase.
    sale_date = models.DateTimeField(blank=True, null=True)
    quantity = models.FloatField(blank=True, null=True)
    sales_value = models.FloatField(blank=True, null=True)
    month = models.BigIntegerField(blank=True, null=True)
    date = models.BigIntegerField(blank=True, null=True)
    year = models.BigIntegerField(blank=True, null=True)
    upload_date = models.CharField(db_column='upload_date', default=time.strftime('%d/%m/%Y::%H:%M:%S'),max_length = 32)
    user = models.CharField(blank=True, null=True,max_length = 32)

    class Meta:
        managed = True
        db_table = 'sales_data'


class FinalRatings(models.Model):

    index = models.AutoField(primary_key=True)
    dealerid = models.CharField(db_column='dealerId', blank=True,db_index=True,max_length = 32,null=True)  # Field name made lowercase.
    vintage_rating = models.BigIntegerField(blank=True, null=True)
    severity_rating = models.BigIntegerField(blank=True, null=True)
    growth_rating = models.BigIntegerField(blank=True, null=True)
    u1_rating = models.BigIntegerField(blank=True, null=True)
    u2_rating = models.BigIntegerField(blank=True, null=True)
    recency_rating = models.FloatField(blank=True, null=True)
    os_days_rating = models.BigIntegerField(blank=True, null=True)
    instances_rating = models.BigIntegerField(blank=True, null=True)
    repayment_outstanding_ratio_rating = models.BigIntegerField(blank=True, null=True)
    final_rating = models.FloatField(blank=True, null=True)
    upload_date = models.CharField(db_column='upload_date', default=time.strftime('%d/%m/%Y::%H:%M:%S'),max_length = 32)
    user = models.CharField(blank=True, null=True,max_length = 32)


    class Meta:
        managed = True
        db_table = 'final_ratings'


class DealerData(models.Model):
    index = models.AutoField(primary_key=True)
    week_date = models.CharField(blank=True,max_length = 32)
    week_trend = models.BigIntegerField(blank=True, null=True)
    company_code = models.BigIntegerField(blank=True, null=True)
    account_group = models.CharField(db_column='account_group', blank=True, null=True,max_length = 32)  # Field renamed to remove unsuitable characters.
    category = models.CharField(blank=True, null=True,max_length = 32)
    customer_code = models.CharField(blank=True,db_index=True,max_length = 32,null=True)
    credit_limit = models.CharField(blank=True, null=True,max_length = 32)
    outstanding_amount = models.CharField(blank=True, null=True,max_length = 32)
    not_due_amount = models.CharField(blank=True, null=True,max_length = 32)
    number_0_30_days_os = models.CharField(db_column='0_30_Days_OS', blank=True, null=True,max_length = 32)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_31_60_days_os = models.CharField(db_column='31_60_Days_OS', blank=True, null=True,max_length = 32)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_61_90_days_os = models.CharField(db_column='61 _90_Days_OS', blank=True, null=True,max_length = 32)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_91_120_days_os = models.CharField(db_column='91_120_Days_OS', blank=True, null=True,max_length = 32)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_121_180_days_os = models.CharField(db_column='121_180_Days_OS', blank=True, null=True,max_length = 32)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_181_365_days_os = models.CharField(db_column='181_365_Days_OS', blank=True, null=True,max_length = 32)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    greater_than_365_days_os = models.CharField(db_column='greater_than_365_Days_OS', blank=True, null=True,max_length = 32)  # Field name made lowercase.
    overdue_amount = models.CharField(blank=True, null=True,max_length = 32)
    less_than_180_days_overdue = models.CharField(db_column='less_than_180_Days_Overdue', blank=True, null=True,max_length = 32)  # Field name made lowercase.
    greater_than_180_days_overdue = models.CharField(db_column='greater_than_180_Days_Overdue', blank=True, null=True,max_length = 32)  # Field name made lowercase.
    security_deposit = models.CharField(blank=True, null=True,max_length = 32)
    no_of_days_os = models.CharField(db_column='No_of_Days_OS', blank=True, null=True,max_length = 32)  # Field name made lowercase.
    upload_date = models.CharField(db_column='upload_date', default=time.strftime('%d/%m/%Y::%H:%M:%S'),max_length = 32)
    user = models.CharField(blank=True, null=True,max_length = 32)


    class Meta:
        managed = True
        db_table = 'dealer_data'


class GrowthRating(models.Model):
    index = models.AutoField(primary_key=True)
    dealerid = models.CharField(db_column='dealerId', blank=True,db_index=True,max_length = 32,null=True)  # Field name made lowercase.
    ratio = models.FloatField(blank=True, null=True)
    rating = models.BigIntegerField(blank=True, null=True)
    # upload_date = models.CharField(db_column='upload_date', default=time.strftime('%d/%m/%Y::%H:%M:%S'),max_length = 32)
    # user = models.CharField(blank=True, null=True,max_length = 32)


    class Meta:
        managed = True
        db_table = 'growth_rating'


class InstancesRating(models.Model):
    index = models.AutoField(primary_key=True)
    customer_code = models.CharField(blank=True,db_index=True,max_length = 32,null=True)
    ratio = models.FloatField(blank=True, null=True)
    rating = models.BigIntegerField(blank=True, null=True)
    # upload_date = models.CharField(db_column='upload_date', default=time.strftime('%d/%m/%Y::%H:%M:%S'),max_length = 32)
    # user = models.CharField(blank=True, null=True,max_length = 32)


    class Meta:
        managed = True
        db_table = 'instances_rating'


# class OsDays(models.Model):
#     index = models.AutoField(primary_key=True)
#     customer_code = models.CharField(blank=True,db_index=True,max_length = 32)
#     os_days = models.FloatField(blank=True, null=True)
#     upload_date = models.CharField(db_column='upload_date', default=time.strftime('%d/%m/%Y::%H:%M:%S'))
#     user = models.CharField(blank=True, null=True)
#
#
#     class Meta:
#         managed = True
#         db_table = 'os_days'


class OsDaysRating(models.Model):
    index = models.AutoField(primary_key=True)
    customer_code = models.CharField(blank=True,db_index=True,max_length = 32,null=True)
    ratio = models.FloatField(blank=True, null=True)
    rating = models.BigIntegerField(blank=True, null=True)
    # upload_date = models.CharField(db_column='upload_date', default=time.strftime('%d/%m/%Y::%H:%M:%S'),max_length = 32)
    # user = models.CharField(blank=True, null=True,max_length = 32)


    class Meta:
        managed = True
        db_table = 'os_days_rating'


class PaymentData(models.Model):
    index = models.AutoField(primary_key=True)
    dealerid = models.CharField(db_column='dealerId', blank=True, null=True,db_index=True,max_length = 32)  # Field name made lowercase.
    payment_date = models.CharField(blank=True,max_length = 32)
    amount = models.FloatField(blank=True, null=True)
    date = models.BigIntegerField(blank=True, null=True)
    month = models.BigIntegerField(blank=True, null=True)
    year = models.BigIntegerField(blank=True, null=True)
    week_trend = models.BigIntegerField(blank=True, null=True)
    upload_date = models.CharField(db_column='upload_date', default=time.strftime('%d/%m/%Y::%H:%M:%S'),max_length = 32)
    user = models.CharField(blank=True, null=True,max_length = 32)


    class Meta:
        managed = True
        db_table = 'payment_data'


class RecencyRating(models.Model):
    index = models.AutoField(primary_key=True)
    dealerid = models.CharField(db_column='dealerId', blank=True,db_index=True,max_length = 32,null=True)  # Field name made lowercase.
    ratio = models.FloatField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    # upload_date = models.CharField(db_column='upload_date', default=time.strftime('%d/%m/%Y::%H:%M:%S'),max_length = 32)
    # user = models.CharField(blank=True, null=True,max_length = 32)


    class Meta:
        managed = True
        db_table = 'recency_rating'


class RepaymentOutstandingRatio(models.Model):
    index = models.AutoField(primary_key=True)
    dealerid = models.BigIntegerField(db_column='dealerId', blank=True, null=True,db_index=True,max_length = 32)  # Field name made lowercase.
    customer_code = models.CharField(blank=True,db_index=True,max_length = 32,null=True)
    week_trend = models.BigIntegerField(blank=True, null=True)
    ratio = models.FloatField(blank=True, null=True)
    # upload_date = models.CharField(db_column='upload_date', default=time.strftime('%d/%m/%Y::%H:%M:%S'),max_length = 32)
    # user = models.CharField(blank=True, null=True,max_length = 32)


    class Meta:
        managed = True
        db_table = 'repayment_outstanding_ratio'


class RepaymentOutstandingRatioRating(models.Model):
    index = models.AutoField(primary_key=True)
    customer_code = models.CharField(blank=True,db_index=True,max_length = 32,null=True)
    ratio = models.FloatField(blank=True, null=True)
    rating = models.BigIntegerField(blank=True, null=True)
    # upload_date = models.CharField(db_column='upload_date', default=time.strftime('%d/%m/%Y::%H:%M:%S'),max_length = 32)
    # user = models.CharField(blank=True, null=True,max_length = 32)


    class Meta:
        managed = True
        db_table = 'repayment_outstanding_ratio_rating'


class SeverityRating(models.Model):
    index = models.AutoField(primary_key=True)
    dealerid = models.CharField(db_column='dealerId', blank=True,db_index=True,max_length = 32,null=True)  # Field name made lowercase.
    ratio = models.FloatField(blank=True, null=True)
    rating = models.BigIntegerField(blank=True, null=True)
    # upload_date = models.CharField(db_column='upload_date', default=time.strftime('%d/%m/%Y::%H:%M:%S'),max_length = 32)
    # user = models.CharField(blank=True, null=True,max_length = 32)


    class Meta:
        managed = True
        db_table = 'severity_rating'


class SumOutstanding(models.Model):
    index = models.AutoField(primary_key=True)
    customer_code = models.CharField(blank=True,db_index=True,max_length = 32,null=True)
    week_trend = models.BigIntegerField(blank=True, null=True)
    balance = models.FloatField(blank=True, null=True)
    # upload_date = models.CharField(db_column='upload_date', default=time.strftime('%d/%m/%Y::%H:%M:%S'),max_length = 32)
    # user = models.CharField(blank=True, null=True,max_length = 32)


    class Meta:
        managed = True
        db_table = 'sum_outstanding'


class SumRepayment(models.Model):
    index = models.AutoField(primary_key=True)
    dealerid = models.CharField(db_column='dealerId', blank=True, null=True,db_index=True,max_length = 32)  # Field name made lowercase.
    week_trend = models.BigIntegerField(blank=True, null=True)
    payment = models.FloatField(blank=True, null=True)
    # upload_date = models.CharField(db_column='upload_date', default=time.strftime('%d/%m/%Y::%H:%M:%S'),max_length = 32)
    # user = models.CharField(blank=True, null=True,max_length = 32)


    class Meta:
        managed = True
        db_table = 'sum_repayment'


class U1Rating(models.Model):
    index = models.AutoField(primary_key=True)
    customer_code = models.CharField(blank=True,db_index=True,max_length = 32,null=True)
    ratio = models.FloatField(blank=True, null=True)
    rating = models.BigIntegerField(blank=True, null=True)
    # upload_date = models.CharField(db_column='upload_date', default=time.strftime('%d/%m/%Y::%H:%M:%S'),max_length = 32)
    # user = models.CharField(blank=True, null=True,max_length = 32)


    class Meta:
        managed = True
        db_table = 'u1_rating'


class U1Ratio(models.Model):
    index = models.AutoField(primary_key=True)
    customer_code = models.CharField(blank=True,db_index=True,max_length = 32,null=True)
    ratio = models.FloatField(blank=True, null=True)
    # upload_date = models.CharField(db_column='upload_date', default=time.strftime('%d/%m/%Y::%H:%M:%S'),max_length = 32)
    # user = models.CharField(blank=True, null=True,max_length = 32)

    class Meta:
        managed = True
        db_table = 'u1_ratio'


class U2Rating(models.Model):
    index = models.AutoField(primary_key=True)
    customer_code = models.CharField(blank=True,db_index=True,max_length = 32,null=True)
    ratio = models.FloatField(blank=True, null=True)
    rating = models.BigIntegerField(blank=True, null=True)
    # upload_date = models.CharField(db_column='upload_date', default=time.strftime('%d/%m/%Y::%H:%M:%S'),max_length = 32)
    # user = models.CharField(blank=True, null=True,max_length = 32)

    class Meta:
        managed = True
        db_table = 'u2_rating'


class U2Ratio(models.Model):
    index=models.AutoField(primary_key=True)
    customer_code = models.CharField(blank=True,db_index=True,max_length = 32,null=True)
    ratio = models.FloatField(blank=True, null=True)
    # upload_date = models.CharField(db_column='upload_date', default=time.strftime('%d/%m/%Y::%H:%M:%S'),max_length = 32)
    # user = models.CharField(blank=True, null=True,max_length = 32)

    class Meta:
        managed = True
        db_table = 'u2_ratio'


class VintageRating(models.Model):
    index= models.AutoField(primary_key=True)
    dealerid = models.CharField(db_column='dealerId', blank=True,db_index=True,max_length = 32,null=True)  # Field name made lowercase.
    ratio = models.FloatField(blank=True, null=True)
    rating = models.BigIntegerField(blank=True, null=True)
    # upload_date = models.CharField(db_column='upload_date', default=time.strftime('%d/%m/%Y::%H:%M:%S'),max_length = 32)
    # user = models.CharField(blank=True, null=True,max_length = 32)

    class Meta:
        managed = True
        db_table = 'vintage_rating'


