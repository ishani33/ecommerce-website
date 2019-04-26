from django.contrib import admin
from .cart import Cart
# Register your models here.
class Cart_item(admin.ModelAdmin):
    class Meta:
        model = Cart

# admin.site.register(Cart,Cart_item)
