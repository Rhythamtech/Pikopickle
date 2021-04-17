from django.contrib import admin
from .models import *

admin.site.register(seller)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Wishlist)
admin.site.register(Buyer)
admin.site.register(Cart)
admin.site.register(Checkout)
