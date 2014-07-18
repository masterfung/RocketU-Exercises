$(document).ready(function() {
//    var random = Math.floor(Math.random() * (719 - 2) + 2);
//    console.log(random);

    $('.pokemon').on('click', function () {
        var random = Math.floor(Math.random() * (719 - 2) + 2);
        console.log(random);
        var pokemon = {};
        $.ajax({
            url: "http://pokeapi.co/api/v1/sprite/" + random + "/",
            type: "GET",
            dataType: "jsonp",
            success: function(data) {
                var spriteUrl = 'http://pokeapi.co' + data.image;
                    $('.pokemon').append("<img src=" + spriteUrl + "/><p class='name'>" + data.pokemon.name + "</p>");
        }
});
//        $('img').attr('img', "http://pokeapi.co" + pokemon.image);
    });
});

