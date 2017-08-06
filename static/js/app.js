angular.module('app', [
	'ui.router',
	'ngResource',
	'app.controllers',
	'app.services',
])

.run(function($state) {
	// Doesn't seems like working
	$state.go('home');
})

.config(function($stateProvider, $locationProvider, $urlRouterProvider) {
	// This is a bug fix for the new 1.6
	// angular js. Url encoding issue
	$locationProvider.hashPrefix('');

	$stateProvider
		.state('home', {
			url: "/",
			templateUrl: '../static/partials/index.html',
			controller: 'HomeCtrl'
		})
		.state('products', {
			url: "/products",
			templateUrl: '../static/partials/products.html',
			controller: 'ProductsCtrl'
		})
		.state('contactUs', {
			url: "/contact-us",
			templateUrl: '../static/partials/contact-us.html',
			controller: 'ContactUsCtrl'
		})
		.state('productDetails', {
			url: "/:prodSlug",
			templateUrl: '../static/partials/product-details.html',
			controller: 'ProductDetailsCtrl'
		});

	$urlRouterProvider.otherwise('/');

});