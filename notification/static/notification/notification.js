var messageApp = angular.module('messageApp', []);


messageApp.controller('MainCtrl', ['$scope', function ($scope) {
    // Messages array
    $scope.inbox = {};

    // retrieve Messages from the restAPI
    $http({
        method: 'GET',
        url: '//localhost:8000/api/inbox'
    })
    .success(function (data, status, headers, config) {
        $scope.inbox.messages = data;
    })
    .error(function (data, status, headers, config) {
        // something went wrong :(
    });
}]);


messageApp.directive('readitButton', function () {
  return {
    restrict: 'A',
    replace: true,
    transclude: true,
    template: '<a href="" class="myawesomebutton" ng-transclude>' +
                '<i class="icon-ok-sign"></i>' +
              '</a>',
    link: function (scope, element, attrs) {
      // DOM manipulation/events here!
    }
  };
});
