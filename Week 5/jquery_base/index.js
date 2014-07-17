$(document).ready(function() {
    var total = [];

    var productOne = 0;
    var productTwo = 0;
    var productThree = 0;

    var countOne = 0;
    var countTwo = 0;
    var countThree = 0;

    $(".tellMore").on('click', function() {
        $('.moreInfo').css('display', 'inline');
    });

    $('div.product').hover(function(){
        $(this).toggleClass('active');
    });

    $('.discount').on('click', function(){
        var x = 15 * 0.9;
        $('#price-1').text(x);
    });

    $("#1").on('click', function() {

        var x = confirm('Are you sure you want to add this product?')
        if (countOne < 1) {
            $("#ancient").clone().appendTo('.cart');
        }
        if (x == true) {

            countOne++;
            price = (parseInt($('#price-1').text()));
            total.push(price);
            productOne = price * countOne;

            tempSum = productOne + productTwo +productThree;

            $('div h2').text('Total: $' + tempSum);

            console.log(price);
            console.log(countOne);
        }

    });

    $("#2").on('click', function() {
        var x = confirm('Are you sure you want to add this product?')
        if (countTwo < 1) {
            $("#exlixir").clone().appendTo('.cart');
        }
        if (x == true) {

            countTwo++;
            price = (parseInt($('#price-2').text()));
            total.push(price);
            productTwo = price * countTwo;

            tempSum = productOne + productTwo +productThree;

            $('div h2').text('Total: $' + tempSum);

            console.log(price);
            console.log(countTwo);
        }
        console.log(total);
    });

    $("#3").on('click', function() {
        var x = confirm('Are you sure you want to add this product?')
        if (countThree < 1) {
            $("#truthEye").clone().appendTo('.cart');
        }
        if (x == true) {

            countThree++;
            price = (parseInt($('#price-3').text()));
            total.push(price);
            productThree = price * countThree;

            tempSum = productOne + productTwo +productThree;

            $('div h2').text('Total: $' + tempSum);

            console.log(price);
            console.log(countTwo);
        }
        console.log(total);
    });

    $(".checkout").on('click', function() {
        var x = confirm('Do you want to checkout?');
        if (x == true) {
            final = 0;
            for (var i = 0; i < total.length; i++) {
                final += total[i];
            }

            $('.cart').toggle("hide");
            $(".checkout-box").css("display", 'inline');
            $('.checkout-box').prepend("Final Total: $" + final);

            alert("Your total is: $" + final + ".00 Okta");
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