/**
 * Main application controller
 *
 * You can use this controller for your whole app if it is small
 * or you can have separate controllers for each logical section
 *
 */
;(function() {

  angular
    .module('boilerplate')
    .controller('MainController', MainController);

  MainController.$inject = ['LocalStorage', 'QueryService', '$scope'];


  function MainController(LocalStorage, QueryService, $scope) {

    // 'controller as' syntax
    var self = this;

    $scope.header = 'Purchases';

    $scope.isSearch = false;
    $scope.isPhotoView = false;
    $scope.isAddNewItem = false;
    $scope.isShowPopup = false;
    $scope.isShowProductInfo = false;

    $scope.isRetailerPhotoView = false;

    $scope.addItem = function() {
        $scope.isPhotoView = false;
        $scope.isAddNewItem = true;
    };

    $scope.invalidateItem = function() {
      $scope.isShowPopup = false;
    };

    $scope.toggleSearch = function() {
      $scope.isSearch = !$scope.isSearch;
    };

    $scope.validateItem = function() {
      $scope.isShowProductInfo = true;
      $scope.isPhotoView = false;
    };

    $scope.purchases = [
      {
        iconType: 'laptop',
        name: 'Macbook Pro 2017',
        timestamp: '5 Hours Ago',
        warrantyValidity: true
      },
      {
        iconType: 'phone',
        name: 'Samsung Galaxy S9+',
        timestamp: '6 Hours Ago',
        warrantyValidity: true
      },
      {
        iconType: 'watch',
        name: 'Fitbit Versa',
        timestamp: '5 Hours Ago',
        warrantyValidity: true
      }
    ];

    $scope.pastPurchases = [
      {
        iconType: 'car',
        name: 'Toyota GT86',
        timestamp: '28/11/2015',
        warrantyValidity: false
      },
      {
        iconType: 'tv',
        name: '65" QHD 4K Curved TV',
        timestamp: '06/11/2015',
        warrantyValidity: false
      },

    ];
  }
})();
