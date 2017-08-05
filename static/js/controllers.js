angular.module('app.controllers', [])

.controller('HomeCtrl', function($scope) {
	var dumy_products = [
		{
			id: 1,
			name: 'Product 1',
			description: 'This is a description for product 1',
			image: '../static/img/prod.jpg',
			slug: 'cool-product-1'
		},
		{
			id: 2,
			name: 'Product 2',
			description: 'This is a description for product 2',
			image: '../static/img/prod.jpg',
			slug: 'awesome-product'
		},
		{
			id: 3,
			name: 'Product 3',
			description: 'This is a description for product 3',
			image: '../static/img/prod.jpg',
			slug: 'amazing-product'
		},
		{
			id: 4,
			name: 'Product 4',
			description: 'This is a description for product 4',
			image: '../static/img/prod.jpg',
			slug: 'shot-product'
		}
	];

	$scope.products = dumy_products;

	$scope.joinEmailList = function(email) {
		if(email === undefined) {
			// Send back a message
			// this stuff is blank
			return;
		}
		console.log($scope.customer.email);
		$scope.customer = {};
	};

})

.controller('ProductsCtrl', function($scope) {
	$scope.products = [1, 2, 3, 4]
})

.controller('ContactUsCtrl', function($scope) {
	$scope.products = [1, 2, 3, 4]
})

.controller('ProductDetailsCtrl', function($scope) {
	$scope.products = [1, 2, 3, 4]
});