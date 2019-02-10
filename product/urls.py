from django.urls import path, include
from .views import *

urlpatterns = [
    path('', base, name="base"),
    path('carousel/<pk>/', LandingDetailViewcarousel.as_view(),  name="carousel_url"),
    path('buket/<pk>/',DetailViewBuket.as_view(),  name="buket_url"),
    path('basket/<pk>/',DetailViewBasket.as_view(),  name="basket_url"),
    path('chocolate/<pk>/',DetailViewChocolate.as_view(),  name="chocolate_url"),
    path('action/', action,  name="action"),
    path('buket/', ListViewBuket.as_view(),  name="buket"),
    path('basket/', ListViewBasket.as_view(),  name="basket"),
    path('chocolate/', ListViewChocolate.as_view(),  name="chocolate"),
    path('bith/', ListViewBuketBith.as_view(),  name="bith"),
    path('bisnes/', ListViewBuketBisnes.as_view(),  name="bisnes"),
    path('men/', ListViewBuketMen.as_view(),  name="men"),
    path('year/', ListViewBuketYear.as_view(),  name="year"),
    path('mama/', ListViewBuketMama.as_view(),  name="mama"),
    path('love/', ListViewBuketLove.as_view(),  name="love"),
    path('kids/', ListViewBuketKids.as_view(),  name="kids"),
    path('pay/', pay,  name="pay"),
    path('delivery/', delivery,  name="delivery"),

]