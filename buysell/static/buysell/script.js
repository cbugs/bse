$(document).ready(function() {

    // Buy Sell Exchange Search Form Buttons Checkbox trigger
    $('.btn-checkbox-type').click(function(){
        var checkelem = $(this).find('input[type="checkbox"]');
        if(checkelem.prop('checked')){
            checkelem.prop('checked',false);
            $(this).removeClass('btn-warning');
            $(this).addClass('btn-outline-warning');
        } else {
            checkelem.prop('checked',true);
            $(this).removeClass('btn-outline-warning');
            $(this).addClass('btn-warning');
        }
    });

    // Categories selected Checbox trigger
    $('.checkbox-category').click(function(e){
        e.preventDefault();
        var checkelem = $(this).find('input[type="checkbox"]');
        if(checkelem.prop('checked')){
            checkelem.prop('checked',false);
            $(this).removeClass('active');
        } else {
            checkelem.prop('checked',true);
            $(this).addClass('active');
        }
    });

    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 50) {
            $('#back-to-top').fadeIn();
        } else {
            $('#back-to-top').fadeOut();
        }
    });
    $('#back-to-top').click(function () {
        $('#back-to-top').tooltip('hide');
        $('body,html').animate({
            scrollTop: 0
        }, 800);
        return false;
    });
    $('#back-to-top').tooltip();

    // Pagination form submit trigger on search
    $('.btn-paginate').click(function(){console.log('pp');
        $("#page").val($(this).attr('data-page'));console.log('dd');
        $("#search-form").submit();console.log('qq');
    });

});