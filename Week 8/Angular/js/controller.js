app.controller("bookCtrl", function($scope) {
	$scope.bookList = [
		{name: 'Narnia', genre: 'Fiction', author: 'Lewis', description: 'Awesome Stuff!'},
		{name: 'Hobbit', genre: 'Fiction', author: 'Tolkien', description: 'Bad ass book!'},
		{name: 'Goblet of Fire', genre: 'Fiction', author: 'Rowling', description: 'Magical things exist in this book!'},
	];
	$scope.addBook = function() {
		$scope.bookList.push($scope.book);

		if ($scope.bookList.length > 5) {
			$scope.joy = true;
		}
	};
	$scope.showDescription = function() {
		$scope.description = $scope.description ===  false ? true: false;
	}

});

app.controller("registrationCtrl", function ($scope) {
	$scope.regComplete = false;

	$scope.register = function() {
		$scope.regComplete = true;
	};

	$scope.newReg = function () {
		$scope.regComplete = false;
		$scope.user = {};
	}
});

app.controller('movieCtrl', function ($scope, $http) {
	$scope.titles = [];
	$scope.retrieveMovies = function () {
		$http.jsonp(
		 'http://api.rottentomatoes.com/api/public/v1.0/movies', {
				params: {
					apikey: '88a8qpv9kwg657jxb97ma5nn',
					q: $scope.movies,
					page_limit: '10',
					callback: 'JSON_CALLBACK'
				}
			}).then(function (promise) {
				console.log(promise.data.movies);
				for (var i = 0; i < promise.data.movies.length; i++) {
					$scope.titles.push(promise.data.movies[i]);
				}
				$scope.showResults = true;

			}
		);
	};
	$scope.showMovieInfo = function() {
		$scope.movieDescription = $scope.movieDescription ===  false ? true: false;
	};

});