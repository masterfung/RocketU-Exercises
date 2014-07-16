/**
 * Created by htm on 7/16/14.
 */
for(var i = 0; i < 5; i++) {
    console.log("Hello! Many Times")
}

var myBooks = ['The Art of War', 'The Fountainhead', 'Lean Startup'];

for (var i = 0; i < myBooks.length; i++) {
    console.log(myBooks[i])


    var choice = myBooks[i]

    if (choice === 'The Art of War') {
        console.log('The world of tactics are with you. Use the knowledge wisely!')
    }
    else if (choice === "The Fountainhead") {
        console.log('Fine choice but really long!')
    }
    else if (choice === 'Lean Startup') {
        console.log('Hmm. Entrepreneurs! Horrah!')
    }

}

$('#practice').css('background', 'black');

$('#practice').text("I looked at the docs ");

$('#practice').append("and they were really helpful!");

$('#practice').append("<img src='http://reactiongifs.me/wp-content/uploads/2014/02/shaquille-o-neal-cat-shake.gif'>");



var movies = ['Terminator 2: Judgement Day', 'The Fellowship of the Ring', 'Finding Nemo']

$('#movies').append("<div>movies[0]</div>"); // doesnt work

$('#clickPractice').on('click', function() {
    $(this).text('Clicked!');
});
