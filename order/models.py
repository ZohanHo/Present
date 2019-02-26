from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User  # Импортировали модель User

class Status(models.Model):

    name_status = models.CharField(max_length=30, blank=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name_status

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"


class ProductInBasket(models.Model):
    product_name = models.CharField(max_length=100)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    product_nmb = models.IntegerField(default=0, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    is_active = models.BooleanField(default=True)
    image_product = models.ImageField(upload_to="static/images/", default="")
    session_key = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.product_name)

    class Meta:
        verbose_name = "Товар в корзине"
        verbose_name_plural = "Товары в корзине"

    def get_absolute_url_basket_del(self):
        return reverse("buket_del_url", kwargs={"pk": self.pk})


    #Переопределяем метод save для модели который дубет созранять в админке поля с сумой заказа и общей сумой по всем заказам
    def save(self, *args, **kwargs):
        # общая цена равна (цена товара умножено на количество), потом супер что бы работало по плану
        self.total_price = int(self.product_nmb) * int(self.price_per_item)
        super(ProductInBasket, self).save(*args, **kwargs)


class Order(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=True)
    product_name = models.CharField(max_length=100)
    number = models.IntegerField(default=0, blank=True, null=True)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_in_position = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=50, blank=True)
    customer_address = models.CharField(max_length=150, blank=True)
    comments = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    is_active = models.BooleanField(default=True)
    status = models.ForeignKey(Status, blank=True, on_delete=True, null=True)
    session_key = models.CharField(max_length=100, default=0)

    def __str__(self):
        return "{}".format(self.customer_name)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
