from rest_framework import serializers
from invoices.models import Invoice , InvoiceDetail


class InvoiceSerializer(serializers.ModelSerializer):
    #customer_name = serializers.CharField()

    class Meta:
        model = Invoice
        fields = ('customer_name', 'date')

class InvoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetail
        fields = '__all__'