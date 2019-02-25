
from django.contrib import admin
from .models import ProductInBasket, Status, Order

class ProductInBasketAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInBasket._meta.fields]


    class Meta:
        model = ProductInBasket

admin.site.register(ProductInBasket, ProductInBasketAdmin)

class StatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]


    class Meta:
        model = Status

admin.site.register(Status, StatusAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]


    class Meta:
        model = Order

admin.site.register(Order, OrderAdmin)
