from django.contrib import admin

from wafer.models import Wafer, WaferUser, Account, Customer

# Register your models here.
admin.site.register(Wafer)
admin.site.register(WaferUser)
admin.site.register(Account)
admin.site.register(Customer)