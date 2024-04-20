from django.contrib import admin

from .models import *


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'discription')
    list_filter = ('name', 'price', 'discription')
    # fields = ( 'discription',('name', 'price'),)

    fieldsets = (
        (None, {
            'fields': ( 'name','discription')
        }),
        # ('Availability', {
        #     'fields': ('discription', 'price')
        # }),
    )

