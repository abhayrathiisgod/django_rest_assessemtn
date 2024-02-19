from django.db import models
from django.contrib import admin
# Create your models here.

from django.db import models

class Invoice(models.Model):
    date = models.DateTimeField()
    customer_name = models.CharField(max_length=100)

class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='details', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)

admin.register(Invoice)(admin.ModelAdmin)
admin.register(InvoiceDetail)(admin.ModelAdmin)