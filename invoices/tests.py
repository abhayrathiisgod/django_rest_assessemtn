from django.test import TestCase

# Create your tests here.

# tests.py

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Invoice, InvoiceDetail

class InvoiceAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.invoice_data = {
            'date': '2024-02-18',
            'customer_name': 'Test Customer',
            'details': [
                {
                    'description': 'Test Description',
                    'quantity': 2,
                    'unit_price': '10.00',
                    'price': '20.00'
                }
            ]
        }

    def test_create_invoice(self):
        response = self.client.post('/invoices/', self.invoice_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Invoice.objects.count(), 1)
        self.assertEqual(InvoiceDetail.objects.count(), 1)
