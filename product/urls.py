from django.urls import path, include
from .views import *

urlpatterns = [
    path('', base, name="base"),
    path('carousel/<pk>/', LandingDetailViewcarousel.as_view(),  name="carousel_url"),
    path('buket/<pk>/',DetailViewBuket.as_view(),  name="buket_url"),
    path('basket/<pk>/',DetailViewBasket.as_view(),  name="basket_url"),
    path('chocolate/<pk>/',DetailViewChocolate.as_view(),  name="chocolate_url"),
    path('air/<pk>/',DetailViewAir.as_view(),  name="air_url"),
    path('buket/', ListViewBuket.as_view(),  name="buket"),
    path('basket/', ListViewBasket.as_view(),  name="basket"),
    path('chocolate/', ListViewChocolate.as_view(),  name="chocolate"),
    path('bith/', ListViewBuketBith.as_view(),  name="bith"),
    path('bisnes/', ListViewBuketBisnes.as_view(),  name="bisnes"),
    path('men/', ListViewBuketMen.as_view(),  name="men"),
    path('year/', ListViewBuketYear.as_view(),  name="year"),
    path('mama/', ListViewBuketMama.as_view(),  name="mama"),
    path('love/', ListViewBuketLove.as_view(),  name="love"),
    path('bith_basket/', ListViewBasketBith.as_view(),  name="bith_basket"),
    path('bisnes_basket/', ListViewBasketBisnes.as_view(),  name="bisnes_basket"),
    path('love_basket/', ListViewBasketLove.as_view(),  name="love_basket"),
    path('fruct_chocolate/', ListViewChocolateFructs.as_view(),  name="fruct_chocolate"),
    path('chery_chocolate/', ListViewChocolateChery.as_view(),  name="chery_chocolate"),
    path('kids/', ListViewBuketKids.as_view(),  name="kids"),
    path('pay/', pay,  name="pay"),
    path('delivery/', delivery,  name="delivery"),
    path('contact/', contact,  name="contact"),
    path('air/', ListViewAir.as_view(),  name="air"),
    path('form_popup/', form_popup, name="form_popup_url"),
    path('basket_product/', basket_product, name="basket_product_url"),
    path('basket_product/<pk>/delete/', BuketDeleteView, name="buket_del_url"),
    path('checkout/', checkout, name="checkout"),
    path('checkout/', checkout, name="checkout"),
    path('congratulations/', congratulations, name="congratulations"),
    path('companion/<pk>/', companion, name="companion_url"),


]