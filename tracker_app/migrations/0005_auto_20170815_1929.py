# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker_app', '0004_auto_20170810_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='product',
            field=models.ForeignKey(to='tracker_app.Product', related_name='product'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='product_supplier',
            field=models.ForeignKey(to='tracker_app.ProductSupplier', related_name='supplier'),
        ),
    ]
