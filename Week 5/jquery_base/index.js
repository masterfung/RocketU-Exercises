$(document).ready(function() {
    var oneTotal = [];
    var twoTotal = [];
    var threeTotal = [];

    var productOne = 0;
    var productTwo = 0;
    var productThree = 0;

    var countOne = 0;
    var countTwo = 0;
    var countThree = 0;

    var tempSumOne = 0;
    var tempSumTwo = 0;
    var tempSumThree = 0;

    var grand1 = 0;
    var grand2 = 0;
    var grand3 = 0;
    var grandsum = 0;

    var headerReference = $('div h2');


    $(".tellMore").on('click', function() {
        $('.moreInfo').css('display', 'inline');
    });

    $('div.product').hover(function(){
        $(this).toggleClass('active');
    });

    $('.discount').on('click', function(){
        var x = 20 * 0.9;
        $('#price-1').text(x);
    });

    $("#1").on('click', function() {


        if (countOne < 1) {
            $("#ancient").clone().attr("id", "newAncient").appendTo('.cart');
            $('#newAncient').append('<button class="remove">Removed Item</button>');
        }

        countOne++;
        price = (parseInt($('#price-1').text()));
        oneTotal.push(price);
        productOne = price * countOne;

        tempSumOne = productOne + productTwo + productThree;

        headerReference.html('Total Wisdom: $' + tempSumOne + "<br/>").append( 'Quantity of Wisdom: ' + countOne);

        console.log(oneTotal);
        console.log(countOne);

    });

    $(document).on('click', '.remove', function() {

        oneTotal.pop();
        countOne -= 1;
        productOne = price * oneTotal.length;

//        productTwo = productTwo - Math.abs(price);
//        tempSumOne = productOne + productTwo + productThree;
//        console.log(tempSumOne);
//        console.log(countOne);
        headerReference.html('Total: $' + productOne + "<br/>" + "Quantity: " + countOne);
        console.log(oneTotal)
    });

    $("#2").on('click', function() {

        if (countTwo < 1) {
            $("#exlixir").clone().attr("id", "newExlixir").appendTo('.cart');
            $('#newExlixir').append('<button class="remove">Removed Item</button>');
        }

        countTwo++;
        price = (parseInt($('#price-2').text()));
        twoTotal.push(price);
        productTwo = price * countTwo;

        var tempSumTwo = productOne + productTwo + productThree;

        headerReference.html('Total: $' + productTwo + "<br/>").append( 'Quantity of Wisdom: ' + countTwo);

        console.log(twoTotal);
        console.log(countTwo);

        console.log(twoTotal);
    });

    $(document).on('click', '.remove', function() {

        twoTotal.pop();
        countTwo -= 1;
        productTwo = price * twoTotal.length;
        headerReference.html('Total: $' + productThree + "<br/>" + "Quantity: " + countTwo);
        console.log(tempSumTwo)
    });

    $("#3").on('click', function() {
        if (countThree < 1) {
            $("#truthEye").clone().attr("id", "newtruthEye").appendTo('.cart');
            $('#newtruthEye').append('<button class="remove">Removed Item</button>');
        }

        countThree++;
        price = (parseInt($('#price-3').text()));
        threeTotal.push(price);
        productThree = price * countTwo;

        var tempSumThree = productOne + productTwo + productThree;

        headerReference.html('Total: $' + tempSumThree + "<br/>").append( 'Quantity of Wisdom: ' + countThree);


            console.log(price);
            console.log(countThree);

        console.log(threeTotal);
    });

    $(document).on('click', '.remove', function() {

        threeTotal.pop();
        countThree -= 1;
        productThree = price * threeTotal.length;
        headerReference.html('Total: $' + productThree + "<br/>" + "Quantity: " + countThree);
        console.log(tempSumThree)
    });

    $(".checkout").on('click', function() {
        var x = confirm('Do you want to checkout?');
        if (x == true) {
            for (var i = 0; i < oneTotal.length; i++) {
               grand1 += oneTotal[i];
            }

            for (var j = 0; j < twoTotal.length; j++) {
               grand2 += twoTotal[j];
            }

            for (var k = 0; k < threeTotal.length; k++) {
               grand3 += threeTotal[k];
            }

            var grandsum = grand1 + grand2 + grand3;

            console.log(parseInt(grandsum));
            console.log(productOne);
            console.log(tempSumOne);

            $('.cart').toggle("hide");
            $(".checkout-box").css("display", 'inline');
            $('.checkout-box').prepend("Final Total: $" + grandsum);

            alert("Your total is: $" + grandsum + ".00 Okta");
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