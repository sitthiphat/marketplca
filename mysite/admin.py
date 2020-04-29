from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Gender)
admin.site.register(Address)
admin.site.register(Country)



admin.site.register(Seller)
admin.site.register(Bank)
admin.site.register(SellerBank)


admin.site.register(Buyer)