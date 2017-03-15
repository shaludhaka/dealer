from __future__ import absolute_import, unicode_literals
from pandas import *
import math, datetime
from numpy import *
from sqlalchemy import *
from sqlalchemy.orm.session import sessionmaker
import time
import os
from celery.task import task
import celery

host='127.0.0.1'
user='root'
password=''
dbname='Primary_Dalmia'

_session=None
# _engine=create_engine('mysql+mysqldb://%s:%s@%s/%s'%(user,password,host,dbname))
_engine=create_engine('mysql+mysqldb://%s:@%s/%s'%(user,host,dbname))
Session=sessionmaker(bind=_engine,autocommit=True,autoflush=True)


def session():

    if not _session:
        open_session()
    return _session


def open_session():

    global _session
    _session = Session()


conn = session()


def final_u1(u1):

    if u1 >= 1.5:
        final_u1 = 5
    elif u1 >= 1.3 and u1< 1.5:
        final_u1 = 4
    elif u1 >= 1.15 and u1 < 1.3:
        final_u1 = 3
    elif u1 >= 1 and u1 < 1.15:
        final_u1 = 2
    else:
        final_u1 = 1
    return final_u1


def final_u2(u2):

    if u2 >= 1.5:
        final_u2 = 5
    elif u2 >= 1.3 and u2< 1.5:
        final_u2 = 4
    elif u2 >= 1.15 and u2 < 1.3:
        final_u2 = 3
    elif u2 >= 1 and u2 < 1.15:
        final_u2 = 2
    else:
        final_u2 = 1
    return final_u2


def final_osratio(ratio):

    if ratio >= 141:
        final_r = 5
    elif ratio >= 82 and ratio < 141:
        final_r = 4
    elif ratio >= 52 and ratio < 82:
        final_r = 3
    elif ratio >= 22 and ratio < 51:
        final_r = 2
    else:
        final_r = 1
    return final_r


def final_ru_ratio(repay_util):

    if repay_util >= 1:
        final_ru = 5
    elif repay_util >= .8 and repay_util < 1:
        final_ru = 4
    elif repay_util >= .5 and repay_util < .8:
        final_ru = 3
    elif repay_util >= .2 and repay_util < .5:
        final_ru = 2
    else:
        final_ru = 1
    return final_ru


def parse_num(num):

    if ',' in str(num):
     digit = float(num.replace(',', ''))
     return digit
    else :
        return float(num)


def multiplier(num):
    return num * 30


def final_growth(g):

    if g > 4.0:
        final_g = 1
    elif g >= 1.5 and g < 4.0:
        final_g = 2
    elif g >= 0.5 and g < 2.0:
        final_g = 3
    elif g >= 0 and g < 0.5:
        final_g = 4
    else:
        final_g = 5
    return final_g


def final_vintage(vintage):

    if vintage > 0.8:
        final_v = 1
    elif vintage >= 0.6 and vintage < 0.8:
        final_v = 2
    elif vintage >= 0.4 and vintage < 0.6:
        final_v = 3
    elif vintage >= 0.2 and vintage < 0.4:
        final_v = 4
    else:
        final_v = 5
    return final_v


def final_severity(severity):

    if severity > 0.25:
        final_s = 5
    elif severity >= 0.06 and severity < 0.25:
        final_s = 4
    elif severity >= 0.03 and severity < 0.05:
        final_s = 3
    elif severity >= 0.01 and severity < 0.03:
        final_s = 2
    else:
        final_s = 1
    return final_s


def final_recency(recency):

    if recency >= 4:
        final_rec = 5
    elif recency >= 2.5 and recency < 4:
        final_rec = 4
    elif recency >= 1 and recency < 2.5:
        final_rec = 3
    elif recency >= 0.8 and recency < 1:
        final_rec = 2
    else:
        final_rec = 1

    return final_rec



def final_instance(instance):

    if instance >= 0.25:
        final_i = 5
    elif instance >= 0.1 and instance < 0.25:
        final_i = 4
    elif instance >= 0.06 and instance < 0.13:
        final_i = 3
    elif instance >= 0.03 and instance < 0.06:
        final_i = 2
    else:
        final_i = 1

    return final_i


def num_of_weeks(end_date,start_date):

    start_date = datetime.date(start_date.year,start_date.month,start_date.day)
    #start_date_monday = (start_date - datetime.timedelta(days=start_date.weekday()))
    end_date = datetime.date(end_date.year,end_date.month,end_date.day)
    num_of_weeks = math.ceil((end_date - start_date).days / 7.0)
    return num_of_weeks


@task
def compute_values(frame_sales,frame_dealer_complete,frame_payment_complete,user,uploaddatetime):


    frame_sales = DataFrame(frame_sales)
    frame_dealer_complete = DataFrame(frame_dealer_complete)
    frame_payment_complete = DataFrame(frame_payment_complete)
    print "In the task function"
    load_sales_data(frame_sales,user,uploaddatetime)
    load_dealer_data(frame_dealer_complete,user,uploaddatetime)
    load_payment_data(frame_payment_complete,user,uploaddatetime)
    r_versus_o(user, uploaddatetime, frame_dealer_complete, frame_payment_complete)
    final_rating_data(user, uploaddatetime)
    print "filled r_versus_o and final_rating_data"


def validate_sales_data(frame_sales):

      global flag_sales
      flag_sales=True
      try:
        print "in sales validation"
        frame_sales_complete = frame_sales
        valid_columns = list(frame_sales_complete.columns)
        print valid_columns
        valid_columns = map(lambda x:x.lower().strip(),valid_columns)
        schema_headers = ['dealerid','sale_date','quantity','sales_value','month','date','year']
        if len(valid_columns) == 7 and valid_columns == schema_headers:
              return True
        else:
              print("invalid")
              return False

      except Exception as e:
          print e


def load_sales_data(frame_sales_complete,user,uploaddatetime):

       try:
            print("valid")
            frame_sales_complete['user'] = user
            frame_sales_complete['upload_date']=uploaddatetime
            frame_sales_complete.to_sql(name='sales_data', con=_engine, if_exists='append',index=False)
            vintage_rating(frame_sales_complete,user,uploaddatetime)
            growth_rating(frame_sales_complete,user,uploaddatetime)

       except Exception as e:
           print e



def validate_dealer_data(frame_dealer_complete):

     global flag_dealer
     flag_dealer=True
     try:
        print "in dealer validation"
        valid_columns = list(frame_dealer_complete.columns)
        valid_columns = map(lambda x:x.lower().strip(),valid_columns)
        schema_headers = ['week_date','week_trend','company_code','account_group','category','customer_code','credit_limit',
                          'outstanding_amount','not_due_amount','0_30_days_os','31_60_days_os','61 _90_days_os','91_120_days_os',
                          '121_180_days_os','181_365_days_os','greater_than_365_days_os','overdue_amount','less_than_180_days_overdue',
                          'greater_than_180_days_overdue','security_deposit','no_of_days_os']

        if len(valid_columns) == 21 and valid_columns == schema_headers:
            return True
        else:
            print("invalid")
            return False
     except Exception as e:
         print e


def load_dealer_data(frame_dealer_complete,user,uploaddatetime):

    try:
        frame_dealer_complete['upload_date'] = uploaddatetime
        frame_dealer_complete['user'] = user
        print frame_dealer_complete[:3]
        frame_dealer_complete.to_sql(name='dealer_data', con=_engine, if_exists='append', index=False)
        deliquent_severity(frame_dealer_complete, user, uploaddatetime)
        instances_rating(frame_dealer_complete, user, uploaddatetime)
        o_vs_sd(frame_dealer_complete, user, uploaddatetime)
        o_vs_cr(frame_dealer_complete, user, uploaddatetime)
        os_days(frame_dealer_complete, user, uploaddatetime)
    except Exception as e:
        print e

def validate_payment_data(frame_payment_complete):

    try:
        print "in payment validation"
        valid_columns = list(frame_payment_complete.columns)
        valid_columns = map(lambda x:x.lower().strip(),valid_columns)
        schema = ['dealerid','payment_date','amount','date', 'month','year']

        if len(valid_columns) == 6 and valid_columns == schema:
            return True
        else:
            print("invalid")
            return False
    except Exception as e:
        print e


def load_payment_data(frame_payment_complete,user,uploaddatetime):

   try:

        frame_payment_complete['upload_date'] = uploaddatetime
        frame_payment_complete['user'] = user
        frame_payment_complete['week_trend'] = to_datetime(frame_payment_complete['payment_date']).dt.week
        frame_payment_complete.to_sql(name='payment_data', con=_engine, if_exists='append', index=False)
        print("valid")
   except Exception as e:
       print e



def v_ratio(val,total_weeks):

    return round(math.ceil(float(val.days) / float(7.0)) / float(total_weeks), 2)


def vintage_rating(frame,user,uploaddatetime):

    e_date=str(frame[['sale_date']].max().values[0])
    end_date=Timestamp(e_date).to_pydatetime()
    s_date=str(frame[['sale_date']].min().values[0])
    start_date=Timestamp(s_date).to_pydatetime()
    total_weeks= num_of_weeks(end_date,start_date)
    max_frame=frame.groupby(['dealerId'],as_index=False)['sale_date'].max()
    max_frame['sale_date'] = to_datetime(max_frame['sale_date'].apply(Timestamp))
    min_frame=frame.groupby(['dealerId'],as_index=False)['sale_date'].min()
    min_frame['sale_date']=to_datetime(min_frame['sale_date'].apply(Timestamp))
    values=max_frame
    values['sale_date']=max_frame['sale_date']-min_frame['sale_date']
    values['ratio'] = values['sale_date'].apply(v_ratio,total_weeks=total_weeks)
    values['rating'] = values['ratio'].apply(final_vintage)
    values.drop('sale_date',inplace=True,axis=1)
    values.drop_duplicates(inplace=True)
    values['dealerId'] = to_numeric(values['dealerId'])
    values.set_index(['dealerId'], inplace=True)
    values.to_sql('vintage_rating' , con =_engine ,if_exists='replace')


def growth_rating(frame,user,uploaddatetime):

    sales_frame = frame.groupby(['dealerId', 'month'], as_index=False)['sales_value'].sum()
    pct_changes = sales_frame['sales_value'].pct_change()
    sales_frame['Pct_changes'] = pct_changes.values
    sales_frame.fillna(0)
    mean_growth_sales = sales_frame.groupby(['dealerId'], as_index=False)['Pct_changes'].mean().rename(columns={'Pct_changes':'ratio'})
    mean_growth_sales['rating']=mean_growth_sales['ratio'].apply(final_growth)

    mean_growth_sales.drop_duplicates(inplace=True)
    mean_growth_sales = mean_growth_sales.replace(inf, nan)
    mean_growth_sales['dealerId'] = to_numeric(mean_growth_sales['dealerId'])
    mean_growth_sales.set_index(['dealerId'], inplace=True)
    mean_growth_sales.to_sql('growth_rating',con = _engine, if_exists='replace')


def deliquent_severity(frame,user,uploaddatetime):

    frame = rename_frame(frame)
    negative_data = frame._get_numeric_data()
    print "NUMERIC DATA"
    print negative_data[:2]
    negative_data[negative_data < 0] = 0
    frame['outstanding_amount'] = frame['outstanding_amount'].apply(parse_num)
    frame[frame['outstanding_amount'] < 0] = 0
    sub_frame = frame.filter(['customer_code', 'week_trend', 'DPD1', 'DPD2', 'DPD3', 'DPD4', 'outstanding_amount'],
                             axis=1)
    sub_frame['severity'] = sub_frame.apply(cal_severity, axis=1)
    print "after"
    sub_frame = sub_frame.groupby(['customer_code', 'week_trend'], as_index=False)['severity'].sum()
    print "before"
    recency_frame = sub_frame.filter(['customer_code', 'week_trend', 'severity'], axis=1).rename(
        columns={'customer_code': 'dealerId'})

    sub_frame = sub_frame.groupby(['customer_code'], as_index=False)['severity'].mean().rename(
        columns={'severity': 'ratio',
                 'customer_code': 'dealerId'})
    sub_frame.fillna(0, inplace=True)
    sub_frame['rating'] = sub_frame['ratio'].apply(final_severity)
    sub_frame.drop_duplicates(inplace=True)
    sub_frame['dealerId'] = to_numeric(sub_frame['dealerId'])
    sub_frame.set_index(['dealerId'], inplace=True)
    sub_frame.to_sql("severity_rating", con=_engine, if_exists='replace')
    recency_rating(recency_frame,user,uploaddatetime)


def recency_rating(frame_severity,user,uploaddatetime):

    print "In recency rating"
    sorted_frame = frame_severity.sort_values(by='week_trend', ascending=False)
    sorted_frame = sorted_frame.groupby(["dealerId", 'week_trend'], as_index=False)['severity'].sum()
    print sorted_frame
    print "rows with 2   ,,,,,,,,,,,,,,,"
    sorted_frame = sorted_frame.groupby(["dealerId"]).filter(lambda x: len(x) >= 8)

    sorted_frame = sorted_frame.groupby('dealerId', as_index=False)['severity'].sum()
    print sorted_frame[:2]
    sorted_frame['Rating'] = 1
    print sorted_frame[:2]
    latest_4_severities = sorted_frame.groupby('dealerId').tail(4)
    latest_4_severities = latest_4_severities.groupby('dealerId', as_index=False)['severity'].sum().filter(
        ['dealerId', 'severity'], axis=1)
    temp = sorted_frame.groupby("dealerId", as_index=False).apply(lambda x: x.iloc[:-4])
    last_5_8_severities = temp.groupby('dealerId').tail(4).groupby('dealerId', as_index=False)['severity'].sum().filter(
        ['dealerId', 'severity'], axis=1)
    last_5_8_severities[last_5_8_severities['severity'] <= 0] = 0.1
    print "resultant frame"
    latest_4_severities['average'] = latest_4_severities['severity'] / last_5_8_severities['severity']
    resultant_frame = latest_4_severities
    resultant_frame.drop(['severity'], inplace=True, axis=1)
    print resultant_frame
    resultant_frame['rating'] = resultant_frame['average'].apply(final_recency)
    resultant_frame.rename(columns={'average': 'ratio'}, inplace=True)
    resultant_frame.fillna(0, inplace=True)
    print resultant_frame[:2]
    print resultant_frame.count()
    resultant_frame.drop_duplicates(inplace=True)
    resultant_frame['dealerId'] = to_numeric(resultant_frame['dealerId'])
    resultant_frame.set_index(['dealerId'], inplace=True)
    resultant_frame.to_sql("recency_rating", con=_engine, if_exists='replace')


def instances_rating(frame,user,uploaddatetime):

    frame = rename_frame(frame)
    #-------------Calculate instances-------------
    frame_dpds=frame.filter(['DPD1','DPD2','DPD3','DPD4'],axis=1)
    frame['count'] = (frame_dpds > 0).sum(1)
    frame_a=frame.groupby(['customer_code'],as_index=False)['count'].sum()
    print frame_a
    frame_b=frame.groupby(['customer_code'],as_index=False)['week_trend'].count()
    print frame_b
    print (frame_dpds.astype(bool).sum(axis=1))
    frame_a['ratio'] = frame_a['count'].divide(frame_b['week_trend'])
    frame_a.drop(['count'],axis=1,inplace=True)
    frame_a['rating']=frame_a['ratio'].apply(final_instance)

    frame_a.drop_duplicates(inplace=True)
    print frame_a
    frame_a['customer_code'] = to_numeric(frame_a['customer_code'])
    frame_a.set_index(['customer_code'], inplace=True)
    frame_a.to_sql("instances_rating",con = _engine ,if_exists = 'replace')


def cal_severity(val):

    sums = (val[2])*0.1 + (val[3])*0.2 + (val[4])*0.3 + \
                   (val[5])*0.4
    outstand = float(val[6])
    if outstand <= 0:
        outstand = 0.1
    severity = sums / outstand
    return severity


def rename_frame(frame):

    print frame [:1]
    frame=frame.fillna(0)
    frame['DPD0'] = frame['0_30_Days_OS'].apply(parse_num)
    frame['DPD1'] = frame['31_60_Days_OS'].apply(parse_num)
    frame['DPD2'] = frame['61 _90_Days_OS'].apply(parse_num)
    frame['91_120_Days_OS'] = frame['91_120_Days_OS'].apply(parse_num)
    frame['121_180_Days_OS'] = frame['121_180_Days_OS'].apply(parse_num)
    frame['DPD3'] = frame['91_120_Days_OS']+frame['121_180_Days_OS']
    frame['181_365_Days_OS'] = frame['181_365_Days_OS'].apply(parse_num)
    frame["greater_than_365_Days_OS"] = frame["greater_than_365_Days_OS"].apply(parse_num)
    frame['less_than_180_Days_Overdue'] = frame['less_than_180_Days_Overdue'].apply(parse_num)
    frame['greater_than_180_Days_Overdue'] = frame['greater_than_180_Days_Overdue'].apply(parse_num)
    frame['DPD4'] = frame['181_365_Days_OS']+frame["greater_than_365_Days_OS"]+frame['less_than_180_Days_Overdue']+\
                    frame['greater_than_180_Days_Overdue']
    #print frame[:5]
    frame=frame.drop(['0_30_Days_OS','31_60_Days_OS','61 _90_Days_OS','91_120_Days_OS','121_180_Days_OS','181_365_Days_OS',"greater_than_365_Days_OS",
                      'less_than_180_Days_Overdue','greater_than_180_Days_Overdue'],axis=1)
    frame['outstanding_amount'] = frame['outstanding_amount'].apply(parse_num)


    return frame

def o_vs_sd(frame,user,uploaddatetime):


    frame=frame.filter(['outstanding_amount','security_deposit','customer_code','week_trend'],axis=1)
    frame['outstanding_amount'] = frame['outstanding_amount'].apply(parse_num)
    frame['security_deposit'] = frame['security_deposit'].apply(parse_num)
    frame.fillna(0,inplace=True)
    frame['security_deposit'].replace(0,0.1,inplace=True)
    print frame['security_deposit'][:10]
    frame_sd=frame.groupby(['customer_code','week_trend'],as_index=False)['outstanding_amount','security_deposit'].sum()
    frame_sd['ratio'] = frame_sd['outstanding_amount'] / frame_sd['security_deposit']
    frame_final = frame_sd.groupby('customer_code',as_index=False)['ratio'].mean()
    print frame_final[:10]
    frame_final = frame_final.replace([np.inf, -np.inf], np.nan)
    frame_final.fillna(0,inplace=True)
    frame_final['rating']=frame_final['ratio'].apply(final_u2)
    frame_final.drop_duplicates(inplace=True)
    frame_final['customer_code'] = to_numeric(frame_final['customer_code'])
    frame_final.set_index(['customer_code'], inplace=True)
    frame_final.to_sql(name="u2_rating", con=_engine, if_exists='replace')


def o_vs_cr(frame,user,uploaddatetime):

    frame=frame.filter(['customer_code','outstanding_amount','credit_limit','week_trend'],axis=1)
    frame['outstanding_amount'] = frame['outstanding_amount'].apply(parse_num)
    frame['credit_limit'] = frame['credit_limit'].apply(parse_num)
    frame.fillna(0, inplace=True)
    frame['credit_limit'].replace(0, 0.1, inplace=True)
    frame_outstand=frame.groupby(['customer_code','week_trend'],as_index=False)['outstanding_amount','credit_limit'].sum()
    frame_outstand['ratio'] = frame_outstand['outstanding_amount'] / frame_outstand['credit_limit']
    frame_final = frame_outstand.groupby('customer_code',as_index=False)['ratio'].mean()
    frame_final['rating']=frame_final['ratio'].apply(final_u1)
    frame_final.drop_duplicates(inplace=True)
    frame_final['customer_code'] = to_numeric(frame_final['customer_code'])
    frame_final.set_index(['customer_code'], inplace=True)
    frame_final.to_sql(name="u1_rating", con=_engine, if_exists='replace')


def os_days(frame,user,uploaddatetime):

    frame=frame.filter(['customer_code','No_of_Days_OS','week_trend'],axis=1)
    frame.fillna(0,inplace=True)
    frame.sort_values(by='customer_code',inplace=True)
    frame['No_of_Days_OS'] = frame['No_of_Days_OS'].apply(parse_num)
    frame=frame.groupby(['week_trend','customer_code'],as_index=False)['No_of_Days_OS'].sum()
    frame = frame.groupby(['customer_code'],as_index=False)['No_of_Days_OS'].mean()
    print frame[:4]
    frame['No_of_Days_OS'] = frame['No_of_Days_OS'].apply(multiplier)
    frame.rename(columns={'No_of_Days_OS':'ratio'},inplace=True)
    frame['rating'] = frame['ratio'].apply(final_osratio)
    frame['customer_code'] = to_numeric(frame['customer_code'])
    frame.set_index(['customer_code'], inplace=True)
    frame.to_sql('os_days_rating',con = _engine ,if_exists = 'replace')


def r_versus_o(user,uploaddatetime,frame_dealer,frame_payment):

    print ("In r_versus_o")
    curr_date = uploaddatetime
    # frame_dealer = read_sql(
    #     "select customer_code,week_trend,outstanding_amount,upload_date,user from dealer_data where upload_date='{0}' and user='{1}'".format(
    #         curr_date, user), con=_engine)
    # frame_payment = read_sql(
    #     "select dealerId,week_trend,amount,upload_date,user from payment_data where upload_date='{0}' and user='{1}'".format(
    #         curr_date, user), con=_engine)
    frame_dealer = frame_dealer.filter(['customer_code','week_trend','outstanding_amount'],axis=1)
    frame_payment = frame_payment.filter(['dealerId','week_trend','amount'],axis=1)
    frame_dealer.fillna(0, inplace=True)
    frame_dealer['outstanding_amount'] = frame_dealer['outstanding_amount'].apply(parse_num)
    summed_frame_dealer = frame_dealer.groupby(['customer_code', 'week_trend'], as_index=False)[
        'outstanding_amount'].sum()
    summed_frame_dealer.rename(
        columns={'customer_code': 'customer_code', 'week_trend': 'week_trend', 'outstanding_amount': 'balance'},
        inplace=True)
    summed_frame_payment = frame_payment.groupby(['dealerId', 'week_trend'], as_index=False)['amount'].sum()
    summed_frame_payment.rename(columns={'dealerId': 'dealerId', 'week_trend': 'week_trend', 'amount': 'payment'},
                                inplace=True)

    summed_frame_dealer['customer_code'] = to_numeric(summed_frame_dealer['customer_code'])
    summed_frame_dealer.set_index(['customer_code'],inplace=True)
    summed_frame_payment['dealerId'] = to_numeric(summed_frame_payment['dealerId'])
    summed_frame_payment.set_index(['dealerId'],inplace=True)
    print "Writing data to sql"

    summed_frame_payment.to_sql(name='sum_repayment', con=_engine, if_exists='replace')
    summed_frame_dealer.to_sql(name='sum_outstanding', con=_engine, if_exists='replace')
    query = "select so.customer_code,sr.week_trend,sr.payment/so.balance as ratios from sum_repayment as " \
            "sr join sum_outstanding  as so on sr.week_trend=so.week_trend where  sr.dealerId=so.customer_code "
    frame = read_sql(query, con=_engine)
    print frame[:2]
    frame = frame.groupby(['customer_code'], as_index=False)['ratios'].mean()
    frame.rename(columns={'ratios': 'ratio'}, inplace=True)
    print frame[:2]
    frame['rating'] = frame['ratio'].apply(final_ru_ratio)
    frame['customer_code'] = to_numeric(frame['customer_code'])
    frame.set_index(['customer_code'],inplace=True)
    frame.to_sql('repayment_outstanding_ratio_rating', con=_engine, if_exists='replace')

    print frame[:4]

def final_rating_data(user,uploaddatetime):

    curr_date= uploaddatetime
    print "In final_rating_data"
    query="select  vintage_rating.dealerId as dealerId , vintage_rating.rating as vintage_rating ,severity_rating.rating as severity_rating ,\
  growth_rating.rating as growth_rating ,u1_rating.rating as u1_rating ,u2_rating.rating as u2_rating , recency_rating.rating as recency_rating ,\
  os_days_rating.rating as os_days_rating , instances_rating.rating as instances_rating , repayment_outstanding_ratio_rating.rating as\
  repayment_outstanding_ratio_rating from vintage_rating join severity_rating on vintage_rating.dealerId=severity_rating.dealerId join growth_rating on\
  severity_rating.dealerId = growth_rating.dealerId join u1_rating on growth_rating.dealerId = u1_rating.customer_code join u2_rating on u1_rating.customer_code = u2_rating.customer_code\
  join recency_rating on u2_rating.customer_code = recency_rating.dealerId join instances_rating on recency_rating.dealerId = instances_rating.customer_code join os_days_rating on\
  instances_rating.customer_code = os_days_rating.customer_code join repayment_outstanding_ratio_rating on os_days_rating.customer_code = " \
  "repayment_outstanding_ratio_rating.customer_code"

    frame=read_sql(query,con=_engine)
    print frame[:2]
    frame['final_rating'] = frame['vintage_rating'].apply(lambda x :x *0.05)+frame['severity_rating'].apply(lambda x :x *0.16)+frame['growth_rating'].apply(lambda x :x *0.1)+\
                            frame['u1_rating'].apply(lambda x :x *0.06)+frame['u2_rating'].apply(lambda x :x *0.12)+frame['recency_rating'].apply(lambda x :x *0.12)+\
                             frame['os_days_rating'].apply(lambda x :x *0.12)+frame['instances_rating'].apply(lambda x :x *0.12)+frame['repayment_outstanding_ratio_rating'].apply(lambda x :x *0.15)
    frame['user']=user
    frame['upload_date']=uploaddatetime
    frame.drop_duplicates(inplace=True)
    frame.to_sql('final_ratings',con=_engine,if_exists='append',index=False)


class Echo(object):
    """An object that implements just the write method of the file-like
    interface.
    """

    def write(self, value):
        """Write the value by returning it, instead of storing in a buffer."""
        return value