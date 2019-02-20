from django.shortcuts import render, HttpResponse, redirect
from product.models import Product, ProductCompanion, SizeProd, Recording, Buket, Basket, Chocolate, Air, Contact
from .models import ProductInBasket, Status
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from product.forms import FormPopup
from django.views.generic import *
from django.urls import reverse_lazy





