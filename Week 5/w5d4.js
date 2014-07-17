/**
 * Created by htm on 7/17/14.
 */

$('li').css('color', 'red');
$('li').next(3).css('color', 'orange');
$('li > p').css('background', 'yellow');
$('li > div').css('background', 'green');
//$('div  div').css('background', 'white'); //optionally added
$('li div div').css('background', 'blue');
$('.indigo').css('color', 'indigo');
$('.violet').css('color', 'violet');


//first-child example use is really helpful!
$('li p:first-child').html('<ul><li>Books</li><li>Ice Cream</li><li>Movies</li></ul>');
$("#nameAwesome").text('Change this text to say "[Joe] is awesome!"');
$("#twoDivs").html('<div>Put this sentence inside a div.</div><div>Put this sentence in a second div.</div>');
$('#emptyString').text('');


