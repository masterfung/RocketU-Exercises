$(document).ready(function() {
    var total = [];

    $(".tellMore").on('click', function() {
        $('.moreInfo').css('display', 'inline');
    });


    $("#1").on('click', function() {
        $("#ancient").clone().appendTo('.cart');
        $("#price-1").clone().appendTo('.cart');
        total.push(parseInt($('#price-1').text()))
        console.log(total);
    });

    $("#2").on('click', function() {
        $('#exlir').clone().appendTo('.cart');
        $("#price-2").clone().appendTo('.cart');
        total.push(parseInt($('#price-2').text()))
        console.log(total);
    });

    $("#3").on('click', function() {
        $('#truthEye').clone().appendTo('.cart');
        $("#price-3").clone().appendTo('.cart');
        total.push(parseInt($('#price-3').text()))
        console.log(total);
    });

    $(".checkout").on('click', function() {
        finalSum = 0;
        for (var i = 0; i < total.length; i++) {
            finalSum += total[i];
        }

        $('.cart').toggle("hide");
        $(".checkout-box").css("display", 'inline');

        alert("Your total is: $" + finalSum + ".00 Okta");
    });



});

