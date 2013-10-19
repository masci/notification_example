var messageApp = angular.module('messageApp', []);


messageApp.controller('MainCtrl', ['$scope', '$http', function ($scope, $http) {
    // Messages array
    $scope.messages = {};

    // retrieve Messages from the restAPI
    $http({
        method: 'GET',
        url: '//127.0.0.1:8000/api/inbox/'
    })
    .success(function (data, status, headers, config) {
        $scope.messages = data;
    })
    .error(function (data, status, headers, config) {
        // something went wrong :(
    });
}]);
