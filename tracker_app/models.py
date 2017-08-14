from django.db import models
from django.conf import settings


class ProductSupplier(models.Model):
    supplier_name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.supplier_name


class Product(models.Model):
    product_name = models.CharField(max_length=20)
    supplier = models.ForeignKey(ProductSupplier, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name


class Issue(models.Model):
    employee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE)
    product_supplier = models.ForeignKey(ProductSupplier, related_name='supplier', on_delete=models.CASCADE)
    issue_date = models.DateTimeField('date issued')
    return_date = models.DateTimeField('date to return the product')
    is_returned = models.BooleanField(default=False)
