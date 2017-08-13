from django.db import models
from django.conf import settings


PRODUCT_TYPE = (
    ('driver_uniform','Driver Uniform'),
    ('superviser_uniform','Superviser Uniform'),
    ('cleaner_uniform','Cleaner Uniform'),
    ('salower_kamiz','Salower Kamiz'),
    ('orna','Orna'),
    ('shoes_black','Shoes Black'),
    ('bata_pump_shoes','Bata Pump Shoes'),
    ('rubber_shoes','Rubber Shoes'),
    ('shocks_nylon','Socks Nylon'),
    ('jursey_pull_over','Jursey Pull Over'),
    ('cardigan','Cardigan'),
    ('jacket_supervisor','Jacket Supervisor'),
    ('tie_black','Tie Black'),
    ('id_color','ID Color'),
    ('rain_coat','Rain Coat'),
    ('gumboot','Gumboott'),
    ('torch_elect','Torch Elect'),
)

PRODUCT_SUPPLIER = (
    ('bata','Bata'),
    ('apex', 'Apex'),
    ('red','RED'),
    ('orange','ORANGE'),
    ('black','BLACK'),
)

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
