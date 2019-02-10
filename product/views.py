from django.shortcuts import render, HttpResponse, redirect
from .models import Product, ProductCompanion, SizeProd, Recording, Buket, Basket
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
    template_name = "product/buket.html"



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