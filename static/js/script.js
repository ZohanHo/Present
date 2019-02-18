//Carousel Auto-Cycle
 $(document).ready(function() {
    $('.carousel').carousel({
     interval: 6000
    })
   });


//popup
$('.open_fast').click(function () { // Описуем что будет происходить по клику на кнопку с класом .open_fast
    console.log('ok');
    $('.popup_fast').css({"top": $(window).scrollTop() + 220}).addClass('active'); // ccs свойство top, проскроливать + 220
    var bg_popup = $('.bg_popup');
    bg_popup.fadeIn(); // fadeIn() - плавно появляется
    bg_popup.click(function () {   // удаляем при нажати на на люьом месте кроме окна котрое появилось
    $('.popup_fast').removeClass('active');
    bg_popup.fadeOut();
    });
 });


<!-- цена в деталке по количеству килограм -->

    //Basket
    $(document).ready(function () {    //скрипт загрузится после того как загрузится вся страница DOM
        var form_basket = $('#basket_add');   //выбираем форму используя селектор ID формы
        form_basket.on('submit', function () {  // on('submit', function - используетсяя при сабмите формы
            //С помощью функции event.preventDefault(); - можно сделать что бы страница не обновлялась при отправке
            // формы(предотвращаеет стандартное поведение) передаем аргумент который может называтся как либо, тут event
           // event.preventDefault(); // применяеи фугкцию preventDefault()
            var nmb = $('#basket_add_input').val(); // Считали значение с input (Количество)

            var submit_button = $('#submit_button'); // Взяли ворму по id

            var name = submit_button.data('name'); // Считали по id название продукта с тега h4 (id)
            var id = submit_button.data('id'); //считали сначение атрибута с data (data-id)
            var price = submit_button.data('price'); //считали сначение атрибута с data (data-price)
            var session_key = submit_button.data('session_key'); //считали сначение атрибута с data (data-price)
            var images = submit_button.data('images'); //считали сначение атрибута с data (data-price)


    //Ajax
        var data = {}; // data ето данные (словарь) которые мы будем отправлять на бекенд, (название, цена, id)
        // url - куда будет перенаправлет post запрос, указать action то будет все как обычно Кажись !!!!
        var url = $('#basket_add').attr("action");  //form.attr("action"); - так можно считать url c атрибута формы если указать не путь
        // "/product/" + new_car_id + "/";
        //var csrftoken = $("[name=csrfmiddlewaretoken]").val(); //вытянуть токен и использовать если нужно
        var csrftoken = $('#basket_add [name="csrfmiddlewaretoken"]').val();

        //ложим нужные переменные в наш словарь data
        data["nmb"] = nmb;
        data["name"] = name;
        data["price"] = price;
        data["csrfmiddlewaretoken"] = csrftoken;
        data["id"] = id;
        data["session_key"] = session_key;
        data["images"] = images;

        console.log(data);

        $.ajax({
            url: url,
            type: 'post',
            data: data,
            cache: false,
            success: function (data) {  // data - словарь который передаем во views.py jsonresponse в словаре

            //добавляет товат в выпадающий список корзины


            // if (data.products_total_num){
            //     $('#span').text("("+ data.products_total_num  +")");
            // }



            console.log('OK - add - ajax');
            },
            error: function () {
                console.log('error');
            }
        });

    //EndAjax

        //$('.basket_item ul').append('<li>' + name + '   ' + '   ' + nmb + 'шт' + '   ' + '<a href="" class="del_item" >del</a>' + '</li>');







        })
    });
    //EndBasket

    //при нажатии на корзину показует список товаров
        var basket_top = $(".basket_top");
        var basket_item = $(".basket_item");

        basket_top.mouseover(function () { // или клие или наведение
        basket_item.toggleClass("d-none"); //при наведении удаляется временно класс если он есть
        });

        basket_top.mouseout(function () { // или клие или наведение
        basket_item.toggleClass("d-none"); //при наведении удаляется временно класс
        });



// Input количества товара
    $(function() {(function quantityProducts() {
        var $quantityArrowMinus = $(".quantity-arrow-minus");
        var $quantityArrowPlus = $(".quantity-arrow-plus");
        var $quantityNum = $(".quantity-num");

        $quantityArrowMinus.click(quantityMinus);
        $quantityArrowPlus.click(quantityPlus);

        function quantityMinus() {
          if ($quantityNum.val() > 1) {
            $quantityNum.val(+$quantityNum.val() - 1);
          }
        }

        function quantityPlus() {
          $quantityNum.val(+$quantityNum.val() + 1);
        }
        })
        ();
    });
// EndInput


//Basket size
    var checkbox1 = $('#s');
    var checkbox2 = $('#m');
    var checkbox3 = $('#l');

    var price_smoll = 2250..toFixed(2); // .toFixed(2) - 2 знака после запятой
    var price_medium = 2500..toFixed(2); // .toFixed(2) - 2 знака после запятой
    var price_lagre = 2750..toFixed(2); // .toFixed(2) - 2 знака после запятой

    var price_smoll_dop = 2330..toFixed(2); // .toFixed(2) - 2 знака после запятой
    var price_medium_dop = 2580..toFixed(2); // .toFixed(2) - 2 знака после запятой
    var price_lagre_dop = 2830..toFixed(2); // .toFixed(2) - 2 знака после запятой

    var span1 = document.getElementById('price_span1');
    var span2 = document.getElementById('price_span2');

    function smoll() {
        if (checkbox1) {
            span1.innerHTML = price_smoll;
            span2.innerHTML = price_smoll;

        }
    }

    function medium() {
        if (checkbox2) {
            span1.innerHTML = price_medium;
            span2.innerHTML = price_medium;
        }
    }

    function lagre() {
        if (checkbox3) {
            span1.innerHTML = price_lagre;
            span2.innerHTML = price_lagre;
        }
    }



<!-- значение с select-options -->
    var select = document.getElementById('dop_chocolate');


        select.addEventListener('change', function() {


        var i = this.selectedIndex; //по индексу можем выбрать options нужный от 0 и дальше по порядку
        if (checkbox1)
        if (i == 1) {
            //var value = this.options[i].value; // так можно считать значение с value у options
            if (checkbox1) {
                span1.innerHTML = price_smoll_dop;
            }
            if (checkbox2)  {
                span1.innerHTML = price_medium_dop;
            }
            if (checkbox3)  {
                span1.innerHTML = price_lagre_dop;
            }

        }

        if (i == 0) {

            if (checkbox1)  {
                span1.innerHTML = price_smoll;
            }
            if (checkbox2)  {
                span1.innerHTML = price_medium;
            }
            if (checkbox3)  {
                span1.innerHTML = price_lagre;
            }
        }
    });

