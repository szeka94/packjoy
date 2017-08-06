angular.module('app.services', [])

.factory('Products', [ProductsFactory])
.factory('Email', ['$resource', EmailFactory]);

// Products Factory Constructor
function ProductsFactory() {

	function getProducts() {
		return [
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
		]
	};

	// returned factory object
	return {
		getProducts: getProducts
	};
};


// Email Factorty Constructor
function EmailFactory($resource) {
	return $resource('http://localhost:5000/api/email');
}