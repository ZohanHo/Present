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
    path('pay/', pay,  name="pay"),
    path('delivery/', delivery,  name="delivery"),

]