from django import forms
from .models import Contact
from order.models import Order


class FormPopup(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ["name", "phone"]



class FormOrderContact(forms.ModelForm):

    class Meta:
        model = Order
        fields = ["customer_name", "customer_address", "customer_phone", "comments",]
