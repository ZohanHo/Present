from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User



class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    is_active = models.BooleanField(default=True)
    image_product = models.ImageField(upload_to="static/images/", default="")
    sizeprod = models.ManyToManyField('SizeProd',blank=True,  related_name='product')
    smoll_s = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    smoll_m = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    smoll_l = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return "{}".format(self.product_name)

    class Meta:
        verbose_name = "Фруктовый букет"
        verbose_name_plural = "Фруктовые букеты"

    def get_absolute_url_carousel(self):  # метод который возвращает ссылку на конкретный обьет класса, передаем url шаблона и словарь
        return reverse("carousel_url", kwargs={"pk": self.pk})  # в словарь в качестве ключа получает поле,
        # то поле по которому мы проводим идентификацию обьекта и self.slug или self.pk (поле конкретно обьекта )


class Buket(models.Model):

    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    is_active = models.BooleanField(default=True)
    image_product = models.ImageField(upload_to="static/images/", default="")
    sizeprod = models.ManyToManyField('SizeProd',blank=True,  related_name='buket')
    smoll_s = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    smoll_m = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    smoll_l = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    category = models.ForeignKey('CategoryProduct', null=True, blank=True, on_delete=True)

    def __str__(self):
        return "{}".format(self.product_name)

    class Meta:
        verbose_name = "Фруктовый букет"
        verbose_name_plural = "Фруктовые букеты"

    def get_absolute_url_buket(self):  # метод который возвращает ссылку на конкретный обьет класса, передаем url шаблона и словарь
        return reverse("buket_url", kwargs={"pk": self.pk})  # в словарь в качестве ключа получает поле,
        # то поле по которому мы проводим идентификацию обьекта и self.slug или self.pk (поле конкретно обьекта )



class ProductCompanion(models.Model):

    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    is_active = models.BooleanField(default=True)
    image_product = models.ImageField(upload_to="static/images/comp", default="")


    def __str__(self):
        return "{}".format(self.product_name)

    class Meta:
        verbose_name = "Сопутствующий товар"
        verbose_name_plural = "Сопутствующие товары"

    def get_absolute_url_carousel(self):
        return reverse("carousel_url", kwargs={"pk": self.pk})



class SizeProd(models.Model):
    size = models.CharField(max_length=100)
    kg = models.IntegerField(default=0, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return "{}".format(self.size)



class Recording(models.Model):
    rec = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.rec)


class Basket(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to="static/images/", default="")
    category = models.ForeignKey('CategoryProduct', null=True, blank=True, on_delete=True)

    def __str__(self):
        return "{}".format(self.product_name)

    class Meta:
        verbose_name = "Подарочная корзина"
        verbose_name_plural = "подарочные корзины"

    def get_absolute_url_basket(self):
        return reverse("basket_url", kwargs={"pk": self.pk})



class CategoryProduct(models.Model):
    name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = "Категория товара"
        verbose_name_plural = "категория товаровв"

class Chocolate(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to="static/images/", default="")
    category = models.ForeignKey('CategoryProduct', null=True, blank=True, on_delete=True)

    def __str__(self):
        return "{}".format(self.product_name)

    class Meta:
        verbose_name = "Фрукты в шоколаде"
        verbose_name_plural = "Фрукты в шоколаде"

    def get_absolute_url_chocolate(self):
        return reverse("chocolate_url", kwargs={"pk": self.pk})


class Air(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to="static/images/", default="")
    category = models.ForeignKey('CategoryProduct', null=True, blank=True, on_delete=True)

    def __str__(self):
        return "{}".format(self.product_name)

    class Meta:
        verbose_name = "Воздушный шарик"
        verbose_name_plural = "Воздушные шарики"

    def get_absolute_url_air(self):
        return reverse("air_url", kwargs={"pk": self.pk})

class Contact(models.Model):
    name = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "контакты"
