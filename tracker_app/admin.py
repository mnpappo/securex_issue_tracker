from django.contrib import admin

from .models import Issue, Product, ProductSupplier

class IssueAdmin(admin.ModelAdmin):
    list_display = ('employee', 'issue_date', 'return_date', 'is_returned')
    list_filter = ['is_returned', 'employee', 'return_date']
    search_fields = ['employee']

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'supplier')
    list_filter = ['product_name', 'supplier']

class ProductSupplierAdmin(admin.ModelAdmin):
    list_display = ('supplier_name',)


admin.site.register(Issue, IssueAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductSupplier, ProductSupplierAdmin)

admin.site.site_title = 'My App Admin'