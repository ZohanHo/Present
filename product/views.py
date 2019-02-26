from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import Product, ProductCompanion, SizeProd, Recording, Buket, Basket, Chocolate, Air, Contact
from order.models import ProductInBasket, Status, Order
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from .forms import FormPopup, FormOrderContact
from django.views.generic import *
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.contrib.auth.models import User

def base(request):
    queryset_product1 = Product.objects.all()[:4]
    queryset_product2 = Product.objects.all()[4:8]
    queryset_product3 = Product.objects.all()[8:12]
    return render(request, "product/home.html",
                  context={"product1" : queryset_product1, "product2" : queryset_product2,"product3" : queryset_product3, })

class LandingDetailViewcarousel(DetailView):
    model = Product
    template_name = "product/card_detail_carousel.html"

    def get_context_data(self, **kwargs):
        queryset_companion = ProductCompanion.objects.all()
        products = Product.objects.all()
        one = Product.objects.get(pk="1")
        filter = Product.objects.filter(product_name__icontains="букет")
        filter_get = filter.get(product_name__icontains="КИВИАН")
        size = SizeProd.objects.filter(slug__iexact="size")
        context = super(LandingDetailViewcarousel, self).get_context_data(**kwargs)
        context["product_companion"] = queryset_companion
        context["products"] = products
        context["one"] = one
        context["filter"] = filter
        context["filter_get"] = filter_get
        context["size"] = size
        return context



class ListViewBuket(ListView):
    model = Buket
    template_name = "product/buket_list.html"


    def get_context_data(self, **kwargs):
        buket = Buket.objects.all()

        # Paginator
        paginator = Paginator(buket, 9)
        page_number = self.request.GET.get("page")
        page = paginator.get_page(page_number)
        is_paginated = page.has_other_pages()
        if page.has_previous():
            prev_url = "?page={}".format(page.previous_page_number())
        else:
            prev_url = ""
        if page.has_next():
            next_url = "?page={}".format(page.next_page_number())
        else:
            next_url = ""

        context = super(ListViewBuket, self).get_context_data(**kwargs)
        context["buket"] = buket
        context["page"] = page
        context["is_paginated"] = is_paginated
        context["prev_url"] = prev_url
        context["next_url"] = next_url
        return context

class ListViewBuketBith(ListView):
    model = Buket
    template_name = "product/buket_list.html"

    def get_context_data(self, **kwargs):
        birth = Buket.objects.filter(category__name__iexact="На день рождения")
        # Paginator
        paginator = Paginator(birth, 9)
        page_number = self.request.GET.get("page")
        page = paginator.get_page(page_number)
        is_paginated = page.has_other_pages()
        if page.has_previous():
            prev_url = "?page={}".format(page.previous_page_number())
        else:
            prev_url = ""
        if page.has_next():
            next_url = "?page={}".format(page.next_page_number())
        else:
            next_url = ""
        context = super(ListViewBuketBith, self).get_context_data(**kwargs)
        context["birth "] = birth
        context["page"] = page
        context["is_paginated"] = is_paginated
        context["prev_url"] = prev_url
        context["next_url"] = next_url
        return context


class DetailViewBuket(DetailView):
    model = Buket
    template_name = "product/card_detail_buket.html"


    def get_context_data(self, **kwargs):

        #session_key
        # session_key = self.request.session.get('session_key')
        # print(session_key)
        # if not session_key:
        #     self.request.session.cycle_key()
        #     print(session_key)
            # print(self.request.session.session_key)


        buket = Buket.objects.all()
        compabion = ProductCompanion.objects.all()
        context = super(DetailViewBuket, self).get_context_data(**kwargs)
        context["buket"] = buket
        context["companion"] = compabion
        return context

class ListViewBasket(ListView):
    model = Basket
    template_name = "product/basket_list.html"

    def get_context_data(self, **kwargs):

        basket = Basket.objects.all()

        # Paginator
        paginator = Paginator(basket, 9)
        page_number = self.request.GET.get("page")
        page = paginator.get_page(page_number)
        is_paginated = page.has_other_pages()
        if page.has_previous():
            prev_url = "?page={}".format(page.previous_page_number())
        else:
            prev_url = ""
        if page.has_next():
            next_url = "?page={}".format(page.next_page_number())
        else:
            next_url = ""

        context = super(ListViewBasket, self).get_context_data(**kwargs)


        context["basket"] = basket
        context["page"] = page
        context["is_paginated"] = is_paginated
        context["prev_url"] = prev_url
        context["next_url"] = next_url

        return context

class DetailViewBasket(DetailView):
    model = Basket
    template_name = "product/card_detail_basked.html"

    def get_context_data(self, **kwargs):
        basket = Buket.objects.all()
        compabion = ProductCompanion.objects.all()
        context = super(DetailViewBasket, self).get_context_data(**kwargs)
        context["buket"] = basket
        context["companion"] = compabion
        return context


class ListViewChocolate(ListView):
    model = Chocolate
    template_name = "product/chocolate_list.html"

    def get_context_data(self, **kwargs):

        chocolate = Chocolate.objects.all()

        # Paginator
        paginator = Paginator(chocolate, 9)
        page_number = self.request.GET.get("page")
        page = paginator.get_page(page_number)
        is_paginated = page.has_other_pages()
        if page.has_previous():
            prev_url = "?page={}".format(page.previous_page_number())
        else:
            prev_url = ""
        if page.has_next():
            next_url = "?page={}".format(page.next_page_number())
        else:
            next_url = ""

        context = super(ListViewChocolate, self).get_context_data(**kwargs)


        context["chocolate"] = chocolate
        context["page"] = page
        context["is_paginated"] = is_paginated
        context["prev_url"] = prev_url
        context["next_url"] = next_url

        return context

class DetailViewChocolate(DetailView):
    model = Chocolate
    template_name = "product/card_detail_chocolate.html"

    def get_context_data(self, **kwargs):
        chocolate = Chocolate.objects.all()
        compabion = ProductCompanion.objects.all()
        context = super(DetailViewChocolate, self).get_context_data(**kwargs)
        context["chocolate"] = chocolate
        context["companion"] = compabion
        return context

def pay(request):
    return render(request, "product/pay.html", context={})

def delivery(request):
    return render(request, "product/delivery.html", context={})

class ListViewBuketBisnes(ListView):
    model = Buket
    template_name = "product/buket_list.html"

    def get_context_data(self, **kwargs):
        bisnes = Buket.objects.filter(category__name__iexact="Бизнес подарки")
        # Paginator
        paginator = Paginator(bisnes, 9)
        page_number = self.request.GET.get("page")
        page = paginator.get_page(page_number)
        is_paginated = page.has_other_pages()
        if page.has_previous():
            prev_url = "?page={}".format(page.previous_page_number())
        else:
            prev_url = ""
        if page.has_next():
            next_url = "?page={}".format(page.next_page_number())
        else:
            next_url = ""
        context = super(ListViewBuketBisnes, self).get_context_data(**kwargs)
        context["bisnes"] = bisnes
        context["page"] = page
        context["is_paginated"] = is_paginated
        context["prev_url"] = prev_url
        context["next_url"] = next_url
        return context

class ListViewBuketYear(ListView):
    model = Buket
    template_name = "product/buket_list.html"

    def get_context_data(self, **kwargs):
        year = Buket.objects.filter(category__name__iexact="Букет на годовщину")
        # Paginator
        paginator = Paginator(year, 9)
        page_number = self.request.GET.get("page")
        page = paginator.get_page(page_number)
        is_paginated = page.has_other_pages()
        if page.has_previous():
            prev_url = "?page={}".format(page.previous_page_number())
        else:
            prev_url = ""
        if page.has_next():
            next_url = "?page={}".format(page.next_page_number())
        else:
            next_url = ""
        context = super(ListViewBuketYear, self).get_context_data(**kwargs)
        context["bisnes"] = year
        context["page"] = page
        context["is_paginated"] = is_paginated
        context["prev_url"] = prev_url
        context["next_url"] = next_url
        return context

class ListViewBuketMen(ListView):
    model = Buket
    template_name = "product/buket_list.html"

    def get_context_data(self, **kwargs):
        men= Buket.objects.filter(category__name__iexact="Для мужчин")
        # Paginator
        paginator = Paginator(men, 9)
        page_number = self.request.GET.get("page")
        page = paginator.get_page(page_number)
        is_paginated = page.has_other_pages()
        if page.has_previous():
            prev_url = "?page={}".format(page.previous_page_number())
        else:
            prev_url = ""
        if page.has_next():
            next_url = "?page={}".format(page.next_page_number())
        else:
            next_url = ""
        context = super(ListViewBuketMen, self).get_context_data(**kwargs)
        context["men"] = men
        context["page"] = page
        context["is_paginated"] = is_paginated
        context["prev_url"] = prev_url
        context["next_url"] = next_url
        return context

class ListViewBuketMama(ListView):
    model = Buket
    template_name = "product/buket_list.html"

    def get_context_data(self, **kwargs):
        mama= Buket.objects.filter(category__name__iexact="Букет для мамы")
        # Paginator
        paginator = Paginator(mama, 9)
        page_number = self.request.GET.get("page")
        page = paginator.get_page(page_number)
        is_paginated = page.has_other_pages()
        if page.has_previous():
            prev_url = "?page={}".format(page.previous_page_number())
        else:
            prev_url = ""
        if page.has_next():
            next_url = "?page={}".format(page.next_page_number())
        else:
            next_url = ""
        context = super(ListViewBuketMama, self).get_context_data(**kwargs)
        context["mama"] = mama
        context["page"] = page
        context["is_paginated"] = is_paginated
        context["prev_url"] = prev_url
        context["next_url"] = next_url
        return context

class ListViewBuketLove(ListView):
    model = Buket
    template_name = "product/buket_list.html"

    def get_context_data(self, **kwargs):
        love = Buket.objects.filter(category__name__iexact="Любимым")
        # Paginator
        paginator = Paginator(love, 9)
        page_number = self.request.GET.get("page")
        page = paginator.get_page(page_number)
        is_paginated = page.has_other_pages()
        if page.has_previous():
            prev_url = "?page={}".format(page.previous_page_number())
        else:
            prev_url = ""
        if page.has_next():
            next_url = "?page={}".format(page.next_page_number())
        else:
            next_url = ""
        context = super(ListViewBuketLove, self).get_context_data(**kwargs)
        context["love"] = love
        context["page"] = page
        context["is_paginated"] = is_paginated
        context["prev_url"] = prev_url
        context["next_url"] = next_url
        return context

class ListViewBuketKids(ListView):
    model = Buket
    template_name = "product/buket_list.html"

    def get_context_data(self, **kwargs):
        kids = Buket.objects.filter(category__name__iexact="Детские букеты")
        # Paginator
        paginator = Paginator(kids, 9)
        page_number = self.request.GET.get("page")
        page = paginator.get_page(page_number)
        is_paginated = page.has_other_pages()
        if page.has_previous():
            prev_url = "?page={}".format(page.previous_page_number())
        else:
            prev_url = ""
        if page.has_next():
            next_url = "?page={}".format(page.next_page_number())
        else:
            next_url = ""
        context = super(ListViewBuketKids, self).get_context_data(**kwargs)
        context["kids"] = kids
        context["page"] = page
        context["is_paginated"] = is_paginated
        context["prev_url"] = prev_url
        context["next_url"] = next_url
        return context

    # Basket

class ListViewBasketLove(ListView):
    model = Basket
    template_name = "product/basket_list.html"

    def get_context_data(self, **kwargs):
        love = Basket.objects.filter(category__name__iexact="Любимым")
        # Paginator
        paginator = Paginator(love, 9)
        page_number = self.request.GET.get("page")
        page = paginator.get_page(page_number)
        is_paginated = page.has_other_pages()
        if page.has_previous():
            prev_url = "?page={}".format(page.previous_page_number())
        else:
            prev_url = ""
        if page.has_next():
            next_url = "?page={}".format(page.next_page_number())
        else:
            next_url = ""
        context = super(ListViewBasketLove, self).get_context_data(**kwargs)
        context["love"] = love
        context["page"] = page
        context["is_paginated"] = is_paginated
        context["prev_url"] = prev_url
        context["next_url"] = next_url
        return context

class ListViewBasketBith(ListView):
    model = Basket
    template_name = "product/basket_list.html"

    def get_context_data(self, **kwargs):
        love = Basket.objects.filter(category__name__iexact="Бизнес подарки")
        # Paginator
        paginator = Paginator(love, 9)
        page_number = self.request.GET.get("page")
        page = paginator.get_page(page_number)
        is_paginated = page.has_other_pages()
        if page.has_previous():
            prev_url = "?page={}".format(page.previous_page_number())
        else:
            prev_url = ""
        if page.has_next():
            next_url = "?page={}".format(page.next_page_number())
        else:
            next_url = ""
        context = super(ListViewBasketBith, self).get_context_data(**kwargs)
        context["love"] = love
        context["page"] = page
        context["is_paginated"] = is_paginated
        context["prev_url"] = prev_url
        context["next_url"] = next_url
        return context

class ListViewBasketBisnes(ListView):
    model = Basket
    template_name = "product/basket_list.html"

    def get_context_data(self, **kwargs):
        love = Basket.objects.filter(category__name__iexact="На день рождения")
        # Paginator
        paginator = Paginator(love, 9)
        page_number = self.request.GET.get("page")
        page = paginator.get_page(page_number)
        is_paginated = page.has_other_pages()
        if page.has_previous():
            prev_url = "?page={}".format(page.previous_page_number())
        else:
            prev_url = ""
        if page.has_next():
            next_url = "?page={}".format(page.next_page_number())
        else:
            next_url = ""
        context = super(ListViewBasketBisnes, self).get_context_data(**kwargs)
        context["love"] = love
        context["page"] = page
        context["is_paginated"] = is_paginated
        context["prev_url"] = prev_url
        context["next_url"] = next_url
        return context

class ListViewChocolateFructs(ListView):
    model = Chocolate
    template_name = "product/chocolate_list.html"

    def get_context_data(self, **kwargs):
        love = Chocolate.objects.filter(category__name__iexact="Фрукты в шоколаде")
        # Paginator
        paginator = Paginator(love, 9)
        page_number = self.request.GET.get("page")
        page = paginator.get_page(page_number)
        is_paginated = page.has_other_pages()
        if page.has_previous():
            prev_url = "?page={}".format(page.previous_page_number())
        else:
            prev_url = ""
        if page.has_next():
            next_url = "?page={}".format(page.next_page_number())
        else:
            next_url = ""
        context = super(ListViewChocolateFructs, self).get_context_data(**kwargs)
        context["love"] = love
        context["page"] = page
        context["is_paginated"] = is_paginated
        context["prev_url"] = prev_url
        context["next_url"] = next_url
        return context

class ListViewChocolateChery(ListView):
    model = Chocolate
    template_name = "product/chocolate_list.html"

    def get_context_data(self, **kwargs):
        love = Chocolate.objects.filter(category__name__iexact="Клубника в шоколаде")
        # Paginator
        paginator = Paginator(love, 9)
        page_number = self.request.GET.get("page")
        page = paginator.get_page(page_number)
        is_paginated = page.has_other_pages()
        if page.has_previous():
            prev_url = "?page={}".format(page.previous_page_number())
        else:
            prev_url = ""
        if page.has_next():
            next_url = "?page={}".format(page.next_page_number())
        else:
            next_url = ""
        context = super(ListViewChocolateChery, self).get_context_data(**kwargs)
        context["love"] = love
        context["page"] = page
        context["is_paginated"] = is_paginated
        context["prev_url"] = prev_url
        context["next_url"] = next_url
        return context

class ListViewAir(ListView):
    model = Air
    template_name = "product/air.html"

    def get_context_data(self, **kwargs):
        air = Air.objects.all()
        context = super(ListViewAir, self).get_context_data(**kwargs)
        context["air"] = air
        return context

class DetailViewAir(DetailView):
    model = Air
    template_name = "product/card_detail_air.html"

    def get_context_data(self, **kwargs):
        air = Air.objects.all()
        compabion = ProductCompanion.objects.all()
        context = super(DetailViewAir, self).get_context_data(**kwargs)
        context["air"] = air
        context["companion"] = compabion
        return context

def contact(request):
    return render(request,"product/contact.html")


def form_popup(request):
    if request.method == 'POST':
        form = FormPopup(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FormPopup()
    return redirect('/', {"form":form})


# Функция которая обрабатывает форму с деталки и через ajax (через post) передает данные в post,
# которые тут считываем и добавляем в ProductInBaske, отрисовует шаблон корзины - sale_basket.html
def basket_product(request):
    dict_json = dict()

    session = request.session.session_key

    id = request.POST.get('id')
    nmb = request.POST.get('nmb')
    price = request.POST.get('price')
    name = request.POST.get('name')
    key = request.POST.get('session_key')
    images = request.POST.get('images')



    if session == key:
        # Данная конструкция обновляе количество в базе, в нам нужно добавлять
        # try:
        #     product = ProductInBasket.objects.get(product_name = name)
        #     if product:
        #         product.product_nmb = nmb
        #         product.save()
        # except:
        #     ProductInBasket.objects.create(
        #                                 product_name = name,
        #                                 product_nmb = nmb,
        #                                 image_product= images,
        #                                 session_key = key,
        #                                 price_per_item = price,
        #                                 )

        new_product, created = ProductInBasket.objects.get_or_create(
                                        # Get ищит совпадения по етим полям
                                        product_name = name,
                                        image_product= images,
                                        session_key = key,
                                        # Тут то что попадает под create
                                        defaults={"product_nmb": nmb, "price_per_item" : price}
                                        )
        if not created:
            new_product.product_nmb += int(nmb)
            new_product.save(force_update=True)


    # Обшщий прайс по всем позициям, выыдираем из кверисета цену по всем позициям и сумируем, можно сделать на можели post_save для друугой модели
    # all_total_price = 0
    # all_price = ProductInBasket.objects.all()
    # for foo in all_price:
    #     one_total_price = foo.total_price
    #     all_total_price += int(one_total_price)



    return render(request, "product/sale_basket.html", context={}) #"all_total_price": all_total_price

"""
Представление, которое отображает страницу подтверждения и удаляет существующий объект.
 Данный объект будет удален только если используется метод запроса POST. 
 Если это представление получено через GET, оно отобразит страницу подтверждения, 
 которая должна содержать форму, которая отправляет по тому же URL-адресу.
"""
# class BuketDeleteView(DeleteView):
#     model = ProductInBasket
#     success_url = reverse_lazy('basket_product_url')
#     template_name = "product/test.html"


def BuketDeleteView(request, pk):
    obj = ProductInBasket.objects.get(pk=pk)
    obj.delete()
    return render(request, "product/sale_basket.html", context={})





def checkout(request):
    all_total_price = 0
    all_price = ProductInBasket.objects.all()
    for foo in all_price:
        one_total_price = foo.total_price
        all_total_price += int(one_total_price)


    if request.method == 'POST':  # Проверяем ето запрос POST, если пост то:
        form_c = FormOrderContact(request.POST)  # Создаем новый обьект (новую форму)
        if form_c.is_valid():  # Проыеряем валидна ли форма, отвечает ли требованиям полей модели
            form_c.save()  # Сохраняем в БД
    else:  # Если Get или другой
        form_c = FormOrderContact()  # Создаем новый обьект (новую форму)

    user = request.user
    session = request.session.session_key
    obj = ProductInBasket.objects.filter(session_key=session, is_active=True)

    return render(request, "product/checkout.html",context={"obj":obj, "user": user, 'all_total_price':all_total_price, "forma":form_c})



def congratulations(request):

    session = request.session.session_key

    all_total_price = 0
    all_price = ProductInBasket.objects.all()
    for foo in all_price:
        one_total_price = foo.total_price
        all_total_price += int(one_total_price)

    user = User.objects.get(username=request.user)

    post = request.POST
    customer_name = post['customer_name']
    customer_address = post['customer_address']
    customer_phone = post['customer_phone']
    date = post["date"]
    comments = post["comments"]

    obj = ProductInBasket.objects.filter(session_key = session, is_active=True)

    for foo in obj:
        product_name = foo.product_name
        price_per_item = foo.price_per_item
        total_price = all_total_price
        product_nmb = foo.product_nmb
        total_in_position = foo.total_price
        session_key = foo.session_key

        if session == session_key:

            new_product = Order.objects.create(
                                              session_key= session_key,
                                              product_name= product_name,
                                              number= product_nmb,
                                              price_per_item= price_per_item,
                                              total_price= total_price,
                                              total_in_position = total_in_position,
                                              customer_name= customer_name,
                                              customer_phone= customer_phone,
                                              customer_address= customer_address,
                                              comments= comments,
                                              date= date,
                                              user= user,
                                            )

            new_product.save(force_update=True)

    # Удаляет все с корзины после додавления товара в заказ
    all_price.delete()

    return render(request, "product/congratulations.html", context={})


# Добавляет товат в корзиру с лендинговой страницы, через get_abs_url
def companion(request, pk):
    obj = ProductCompanion.objects.get(pk=pk)
    price = obj.price
    name = obj.product_name
    number = 1
    images = obj.image_companion

    session_key = request.session.session_key
    new_product, created = ProductInBasket.objects.get_or_create(
        session_key=session_key, product_name = name,
        defaults={
        "product_name":name,
        "image_product":images,
        "price_per_item":price,
        "product_nmb":number,
        "session_key":session_key
        }
    )

    if not created:
        new_product.product_nmb += 1
        new_product.save(force_update=True)

    return render(request, "product/sale_basket.html", context={})