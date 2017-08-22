angular.module('app.controllers', [])

.controller('HomeCtrl', ['$scope', 'Products', 'Email', HomeCtrl])
.controller('ProductsCtrl', function($scope) {
	$scope.products = [1, 2, 3, 4]
})

.controller('ContactUsCtrl', function($scope) {
	$scope.products = [1, 2, 3, 4]
})

.controller('ProductDetailsCtrl', ['$scope', 'Products', 'product', ProductDetailsCtrl]);





// CTRL functions
function HomeCtrl($scope, Products, Email) {
	
	$scope.products = Products.query();


	$scope.joinEmailList = function(email) {
		if(email === undefined) {
			// Send back a message
			// this stuff is blank/or invalid email
			return;
		}
		var resp = Email.save({ 'email': email });
		resp.$promise.then(function(data) {
			console.log('Everything is okay!');
		}, function(error) {
			// This is where error happens
			var error_message = error.status + ' ' + error.data.message;
		});
		$scope.customer = {};
	};

};


function ProductDetailsCtrl($scope, Products, product) {
	console.log(product);
	$scope.product = product;
};