from django.db import models


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
    product_nmb = models.IntegerField(default=0, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    is_active = models.BooleanField(default=True)
    image_product = models.ImageField(upload_to="static/images/", default="")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    session_key = models.CharField(max_length=100)


    def __str__(self):
        return "{}".format(self.product_name)

    class Meta:
        verbose_name = "Товар в корзине"
        verbose_name_plural = "Товары в корзине"

    # Переопределяем метод save для модели который дубет созранять в админке поля с сумой заказа и общей сумой по всем заказам
    # def save(self, *args, **kwargs):
    #     self.total_price = self.price_per_item * self.product_nmb  # общая цена равна (цена товара умножено на количество)
    #     super( ProductInBasket, self).save(*args, **kwargs)




# class Order(models.Model):
#     total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # total price for products in order
#     customer_name = models.CharField(max_length=50, blank=True)
#     customer_email = models.EmailField(blank=True)
#     customer_phone = models.CharField(max_length=50, blank=True)
#     customer_address = models.CharField(max_length=150, blank=True)
#     comments = models.TextField(blank=True)
#     date = models.DateTimeField(auto_now_add=True, auto_now=False)
#     update = models.DateTimeField(auto_now=True, auto_now_add=False)
#     is_active = models.BooleanField(default=True)
#     status = models.ForeignKey(Status, blank=True, on_delete=True)
#
#
#     def __str__(self):
#         return "Заказ №{}, {}".format(self.id, self.status.name_status)
#
#     class Meta:
#         verbose_name = "Заказ"
#         verbose_name_plural = "Заказы"