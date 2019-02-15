from django import forms
from .models import Contact


class FormPopup(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ["name", "phone"]