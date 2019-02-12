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