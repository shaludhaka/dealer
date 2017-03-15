from django.conf.urls import url
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', IndexView.as_view(),name = 'index'),

]

