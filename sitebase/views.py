from django.views.generic import TemplateView, FormView ,ListView
from .models import SalesData,FinalRatings,DealerData,PaymentData
from django.shortcuts import render, redirect
from django.views.decorators.clickjacking import xframe_options_exempt
from django.contrib import messages
from braces.views import LoginRequiredMixin
from utils import *
import csv
from django.core.paginator import EmptyPage, PageNotAnInteger
from django.http import StreamingHttpResponse
from django.db.models import Q
from digg_paginator import DiggPaginator as Paginator

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        dealerId = self.request.GET.get('dealer-id', '')
        date_of_upload = self.request.GET.get('selected-date', '')
        user = self.request.user
        upload_dates = FinalRatings.objects.order_by().values_list('upload_date', flat=True).distinct()

        context['dates']=upload_dates
        print date_of_upload
        if dealerId and date_of_upload and user:
            try:
                dealer = FinalRatings.objects.get(Q(dealerid=dealerId),Q(upload_date=date_of_upload),Q(user=user))
                context['dealer'] = dealer
                context['errormsg'] = ''
            except FinalRatings.DoesNotExist:
                #raise Http404
                messages.error(self.request, "Dealer ID does not exist.")
        elif dealerId and not date_of_upload:
            messages.error(self.request, "Please enter the date of record upload")
        elif date_of_upload and not dealerId:
            messages.error(self.request, "Please enter a valid Dealer ID")

        return context


def uploadview(request):

    user = str(request.user)
    print user
    print 'RECEIVED REQUEST: ' + request.method
    status = ''

    if request.method == 'POST':

        salesfile = request.FILES['file1']
        dealerfile = request.FILES['file2']
        paymentfile = request.FILES['file3']
        uploaddatetime=time.strftime('%d/%m/%Y::%H:%M:%S')
        print uploaddatetime
        frame_dealer_complete = read_csv(dealerfile)
        frame_payment_complete = read_csv(paymentfile)
        frame_sales = read_csv(salesfile)

        if validate_sales_data(frame_sales) and validate_dealer_data(frame_dealer_complete) and validate_payment_data(frame_payment_complete) :

                try:

                    print "validated"
                    status = "uploaded successfully...final rating values will be updated after few minutes"
                    print "calculating week trend"
                    print frame_payment_complete['payment_date']
                    frame_payment_complete['week_trend'] = to_datetime(frame_payment_complete['payment_date']).dt.week
                    print "calling task"
                    print type(frame_sales)
                    print type(frame_dealer_complete)
                    print type(frame_payment_complete)
                    print type(user)
                    print type(uploaddatetime)
                    compute_values.delay(frame_sales.to_dict(),frame_dealer_complete.to_dict(),frame_payment_complete.to_dict(),user,uploaddatetime)
                    print("SENT IN BACKGROUND")

                except Exception as e:
                    print e
                    status = 'Failed to parse '
                    return render(request, 'upload.html', {'status': status})
        else:
                return render(request, 'upload.html', {'status': 'Invalid file format '})

    else:
        pass

    return render(request, 'upload.html', {"status":status})


def displayallratings(request):

  date_of_upload = request.GET.get('selected-date', '')
  print "The upload date is %s"%(date_of_upload)
  dealerdata = FinalRatings.objects.filter(upload_date=date_of_upload)
  page = request.GET.get('page', 1)
  paginator = Paginator(dealerdata, 20 , body=6, padding=2)

  try:
     dealers = paginator.page(page)
  except PageNotAnInteger:
      dealers = paginator.page(1)
  except EmptyPage:
      dealers = paginator.page(paginator.num_pages)

  resp =  render(request,"allrating.html",{'dealers':dealers})
  return resp

class DealersListView(ListView):
    model = FinalRatings
    paginate_by = 30
    template_name = 'test.html'


def export_to_csv(request, queryset, fields):

 pseudo_buffer = Echo()
 writer = csv.writer(pseudo_buffer)
 headers = ["DealerId","Vintage","Severity","Growth","Util by Credit Limit","Util by Security dep","Recency",
            "Num of days outstanding","Instance","OS to repayment"]
 writer.writerow(headers)


 response = StreamingHttpResponse((writer.writerow([getattr(object,field) for field in fields]) for object in queryset),content_type="text/csv")
 response['Content-Disposition'] = 'attachment; filename="final_ratings_report.csv"'
 return response


def download(request):

    data = FinalRatings.objects.all()
    return export_to_csv(request, data, fields= ('dealerid','vintage_rating','severity_rating','growth_rating','u1_rating',
                                                 'u2_rating','recency_rating','os_days_rating','instances_rating','repayment_outstanding_ratio_rating','final_rating'))



def compare(request):

    dealerid1_obj=''
    dealerid2_obj=''
    upload_dates = FinalRatings.objects.order_by().values_list('upload_date', flat=True).distinct()
    dates = upload_dates
    dealerid1=request.GET.get('dealer-id1','')
    dealerid2 = request.GET.get('dealer-id2', '')
    print dealerid2
    print dealerid1
    upload_date = request.GET.get('selected-date','')
    user = request.user
    if dealerid1 and dealerid2 and upload_date and user:
        try:
            dealerid1_obj = FinalRatings.objects.get(Q(dealerid=dealerid1), Q(upload_date=upload_date), Q(user=user))
            dealerid2_obj = FinalRatings.objects.get(Q(dealerid=dealerid2), Q(upload_date=upload_date), Q(user=user))
            print dealerid1_obj.dealerid
            print dealerid2_obj.dealerid
        except FinalRatings.DoesNotExist:
            # raise Http404
            messages.error(request, "Dealer ID does not exist.")
    elif dealerid1 and dealerid2 and not upload_date:
        messages.error(request, "Please enter the date of record upload")
    elif upload_date and not dealerid1 or dealerid2:
        messages.error(request, "Please enter both Dealer IDs")


    return render(request,'compare.html',{'dates':dates,'dealerid1_obj':dealerid1_obj,'dealerid2_obj':dealerid2_obj})

@xframe_options_exempt
def bi_view(request):
    return render(request, 'index2.html', locals())


class BIView(TemplateView):
    template_name = 'index2.html'