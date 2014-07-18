var substance = $.ajax({
    url: "/static/js/week5/books.json",
    type: "GET",
    success: function(response) {
        substance = response;
    }
});

//stored in responseText

var substance = $.ajax({
    url: "/static/js/week5/books.json",
    type: "GET",
    success: function(response) {
        console.log(response);
    }
});