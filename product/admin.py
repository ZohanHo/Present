from django.contrib import admin
from .models import Product
from .models import ProductCompanion, SizeProd, Recording, Buket, Basket, CategoryProduct, Chocolate

class CategoryProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]


    class Meta:
        model = Product

admin.site.register(Product, CategoryProductAdmin)


class CategoryProductCompanionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductCompanion._meta.fields]


    class Meta:
        model = ProductCompanion

admin.site.register(ProductCompanion, CategoryProductCompanionAdmin)

class CategorySizeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SizeProd._meta.fields]


    class Meta:
        model = SizeProd

admin.site.register(SizeProd, CategorySizeAdmin)



class BuketAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Buket._meta.fields]


    class Meta:
        model = SizeProd

admin.site.register(Buket, BuketAdmin)


class BasketAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Basket._meta.fields]


    class Meta:
        model = Basket

admin.site.register(Basket, BasketAdmin)

class CategoryProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CategoryProduct._meta.fields]


    class Meta:
        model = CategoryProduct

admin.site.register(CategoryProduct, CategoryProductAdmin)


class ChocolateAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Chocolate._meta.fields]


    class Meta:
        model = Chocolate

admin.site.register(Chocolate, ChocolateAdmin)

admin.site.register(Recording)
