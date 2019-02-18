from .forms import FormPopup
from order.models import ProductInBasket

def popup(request):
    form = FormPopup()

    #session key
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    # Фильтруем где session_key у модели корзины равен текущему session_key, тх количество и покажет нам количество товара
    sesiion_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)  # кверисет
    count = sesiion_in_basket.count()  # количество обьектов в кверисете

    return locals()