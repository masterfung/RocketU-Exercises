$(document).ready(function() {

    var team = [];
    var pokemon = {};

    $('button').on('click', function () {
        for (var i = 0; i < 6; i++) {
            var random = Math.floor(Math.random() * (720) + 2);
            console.log(random);

            $.ajax({
                url: "http://pokeapi.co/api/v1/sprite/" + random + "/",
                type: "GET",
                dataType: "jsonp",
                success: function(data) {
                    pokemon = data;
                    team.push(pokemon);
                    console.log(team.length);
                    console.log(pokemon);

                }
            }).done(function() {
                // code here
                console.log(team);
                console.log(team[1].image);
                var spriteUrl = 'http://pokeapi.co' + team[0].image;
                $('.pokemon')
            .append("<div class='pokebox'><div class='selection inactive'><img src=" + spriteUrl + "/>" +
                "<p class='name'>" + team[0].name.charAt(0).toUpperCase() + team[0].name.substr(1).toLowerCase() + "</p></div></div>")
            .append("<div class='pokebox'><div class='field inactive'><img src=" + spriteUrl + "/>" +
                "<p class='name'>" + team[0].name.charAt(0).toUpperCase() + team[0].name.substr(1).toLowerCase() + "</p></div></div>");

            });
        }

//        if (team.length < 6) {
//            var spriteUrl = 'http://pokeapi.co' + team[0].image;
//        console.log(spriteUrl);
//        $('.pokemon')
//            .append("<div class='pokebox'><div class='selection inactive'><img src=" + spriteUrl + "/>" +
//                "<p class='name'>" + team.pokemon.name.charAt(0).toUpperCase() + team.pokemon.name.substr(1).toLowerCase() + "</p></div></div>")
//            .append("<div class='pokebox'><div class='field inactive'><img src=" + spriteUrl + "/>" +
//                "<p class='name'>" + team.pokemon.name.charAt(0).toUpperCase() + team.pokemon.name.substr(1).toLowerCase() + "</p></div></div>");
//
//        }
//                    $(function() {
//
//                        $('.pokebox').on('click', function(event) {
//                            event.preventDefault();
//
//                            $(this).children('.inactive').toggle();
//                        })
//
//
//                    });

//        function() {
//            // loop over team
//            // add each pokemon to the page
//            // loop ends
//            // add pokebox click event here
//
//        }
    });

//    $('.field .inactive').toggle();

});

//$('#pokeImg').attr('src', 'http://pokeapi.co' + pokemon.image);
