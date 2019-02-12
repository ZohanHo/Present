from django.shortcuts import render, HttpResponse, redirect
from .models import Product, ProductCompanion, SizeProd, Recording, Buket, Basket, Chocolate, Air, Contact
from django.core.paginator import Paginator

from django.views.generic import *


def base(request):
    queryset_product1 = Product.objects.all()[:4]
    queryset_product2 = Product.objects.all()[4:8]
    queryset_product3 = Product.objects.all()[8:12]
    return render(request, "product/home.html",
                  context={
                                "product1": queryset_product1,
                                "product2": queryset_product2,
                                "product3": queryset_product3
                            })

class LandingDetailViewcarousel(DetailView):
    model = Product
    template_name = "product/card_detail_carousel.html"

    def get_context_data(self, **kwargs):
        queryset_compabion = ProductCompanion.objects.all()
        products = Product.objects.all()
        one = Product.objects.get(pk="1")
        filter = Product.objects.filter(product_name__icontains="букет")
        filter_get = filter.get(product_name__icontains="КИВИАН")
        size = SizeProd.objects.filter(slug__iexact="size")


        context = super(LandingDetailViewcarousel, self).get_context_data(**kwargs)

        context["product_companion"] = queryset_compabion
        context["products"] = products
        context["one"] = one

        context["filter"] = filter
        context["filter_get"] = filter_get
        context["size"] = size



        return context

def action(request):
    post = request.POST
    name = post["name_input"] # Считали значение с NAME  у инпута

    # ЗАПИСЬ В БД
    # Проверяем есть ли такая переменная через гет, если ессть ничего не делаем
    # try:
    #     obj = Recording.objects.get(rec=name)
    # except Recording.DoesNotExist: # тначе записум в базу и сохраняем
    #     obj = Recording(rec=name)
    #     obj.save()

    obj, created = Recording.objects.get_or_create(rec=name)
    obj.save()



    return render(request, "product/action.html", context={"post": post,"name": name})


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


        context["buket"] = basket
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
    return render(request, "product/contact.html", context={})


def ContactPopup(request):
    post = request.POST or None  # весь масив пост

    name = post["input_name"]  # Считали значение с NAME у инпута, передаем значение в контекст, который выводим на екран !!!!
    phone = post["input_phone"]  # Считали значение с NAME у инпута, передаем значение в контекст, который выводим на екран !!!!

    if name or phone != '':

        # Запись данных с инпута в базу, название базы Recordin, поле rec
        obj, created = Contact.objects.get_or_create(name=name, phone=phone)
        obj.save()

    return render(request, "product/popup_submit.html", context={})




class ListViewBasketBay(TemplateView):
    model = Buket

    def dispatch(self, request, *args, **kwargs):


        post = request.POST
        quantity = post["basket_add"]

        return render(request, "product/sale_basket.html", context={})







