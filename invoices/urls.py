from django.urls import re_path
from django.contrib import admin
from invoices import views

urlpatterns = [
    #re_path('admin/', admin.site.urls),
    re_path(r'^invoices/$', views.invoice_list),
    re_path(r'^invoices/(?P<pk>[0-9]+)/$', views.invoice_detail),
]