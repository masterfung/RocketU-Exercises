$(document).ready(function() {
    var total = [];

    $(".tellMore").on('click', function() {
        $('.moreInfo').css('display', 'inline');
    });

    $('div.product').hover(function(){
        $(this).toggleClass('active');
    });

    $('.discount').on('click', function(){
        var x = 15 * 0.9;
        $('#price-1').text('$' + x);
    });

    $("#1").on('click', function() {
        count = 0;
        var x = confirm('Are you sure you want to add this product?')
        if (x == true) {
            $("#ancient").clone().appendTo('.cart');
            count++;
            total.push(parseInt($('#price-1').text()));
            console.log(total);
        }
    });

    $("#2").on('click', function() {
        $('#exlir').clone().appendTo('.cart');
        $("#price-2").clone().appendTo('.cart');
        total.push(parseInt($('#price-2').text()));
        console.log(total);
    });

    $("#3").on('click', function() {
        $('#truthEye').clone().appendTo('.cart');
        $("#price-3").clone().appendTo('.cart');
        total.push(parseInt($('#price-3').text()));
        console.log(total);
    });

    $(".checkout").on('click', function() {
        var x = confirm('Do you want to checkout?');
        if (x == true) {
            finalSum = 0;
            for (var i = 0; i < total.length; i++) {
                finalSum += total[i];
            }

            $('.cart').toggle("hide");
            $(".checkout-box").css("display", 'inline');
            $('.checkout-box').prepend("Final Total: $" + finalSum);

            alert("Your total is: $" + finalSum + ".00 Okta");
        }

    });



});

//function confirmation() {
//        var x;
//        if (confirm('Do you want to proceed to checkout?') == true) {
//
//            finalSum = 0;
//            for (var i = 0; i < total.length; i++) {
//                finalSum += total[i];
//            }
//
//            $('.cart').toggle("hide");
//            $(".checkout-box").css("display", 'inline');
//            $('.checkout-box').prepend("Final Total: $" + finalSum);
//
//            alert("Your total is: $" + finalSum + ".00 Okta");
//        } else {
//            x = 'Come back when you are ready';
//        }
//    }