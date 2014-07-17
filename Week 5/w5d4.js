/**
 * Created by htm on 7/17/14.
 */

//first set of how
$('li').css('color', 'red');
$('li').next(3).css('color', 'orange');
$('li > p').css('background', 'yellow');
$('li > div').css('background', 'green');
//$('div  div').css('background', 'white'); //optionally added
$('li div div').css('background', 'blue');
$('.indigo').css('color', 'indigo');
$('.violet').css('color', 'violet');

//second set of hw
//first-child example use is really helpful!
$('li p:first-child').html('<ul><li>Books</li><li>Ice Cream</li><li>Movies</li></ul>');
$("#nameAwesome").text('Change this text to say "[Joe] is awesome!"');
$("#twoDivs").html('<div>Put this sentence inside a div.</div><div>Put this sentence in a second div.</div>');
$('#emptyString').text('');

$('ul li:first-child a').attr('href', "https://www.google.com/").text('Google');
$('ul li:nth-child(2) img').attr('src', "/static/img/deploy-yeti.jpg");
$('#changeText').text($('#changeText').data('text')); //text is the name of data-text (3-2) week 5

//third set of hw
$('ul li:first-child').addClass('red');
$('ul li:nth-child(2)').removeClass('blue');
$('ul li').addClass('border');

$('ul li:first-child').hover(function(){
    $(this).toggleClass('blue');
});

$('ul li:nth-child(2)').on('click', function() {
    $(this).toggleClass('blue')
});

$('ul li').hover(function(){
    $(this).toggleClass('border');
});