angular.module('app.services', [])

.factory('Products', ['API', '$resource', ProductsFactory])
.factory('Email', ['API', '$resource', EmailFactory]);

// Products Factory Constructor
function ProductsFactory(API, $resource) {
	return $resource(API + '/api/products/:slug');
};


// Email Factorty Constructor
function EmailFactory(API, $resource) {
	return $resource(API + '/api/email');
}