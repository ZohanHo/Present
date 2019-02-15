from .forms import FormPopup

def popup(request):
    form = FormPopup()
    return locals()