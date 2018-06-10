/**
 * Main application controller
 *
 * You can use this controller for your whole app if it is small
 * or you can have separate controllers for each logical section
 *
 */

 function getRandomIntInclusive(min, max) {
   min = Math.ceil(min);
   max = Math.floor(max);
   return Math.floor(Math.random() * (max - min + 1)) + min; //The maximum is inclusive and the minimum is inclusive
 }

;(function() {

  angular
    .module('boilerplate')
    .controller('MainController', MainController);

  MainController.$inject = ['LocalStorage', 'QueryService', '$scope', '$http'];


  function MainController(LocalStorage, QueryService, $scope, $http) {

    // 'controller as' syntax
    var self = this;

    // http://10.101.2.28/

    $scope.header = 'Purchases';

    $scope.isLoading = true;
    $scope.isSearch = false;
    $scope.isPhotoView = false;
    $scope.isAddNewItem = false;
    $scope.isShowPopup = false;
    $scope.isShowProductInfo = false;
    $scope.isShowExistingProductInfo = false;

    $scope.isRetailerPhotoView = false;

    $scope.addItem = function() {
        $scope.isLoading = true;
        $http({
          method: 'POST',
          url: '//10.101.2.28:5000/create',
          data: {
            "account": 'clara',
            "manufacturer": 'samsung',
            "serial_number": Math.round(Math.random()*200000000000),
            "length_of_warranty": getRandomIntInclusive(30, 730),
            "coverage": 'Service and Parts',
            "region": 'Hong Kong',
            "contact_details": '66712457',
            "remarks": ''
          }
        }).then(function(response) {
          $scope.isPhotoView = false;
          itemNames = ['OnePlus 5t', 'iPhone X', 'Samsung Galaxy S9', 'LG V30', 'Nokia 3310', 'Google Pixel 2'];
          $http({
            method: 'POST',
            url: '//10.101.2.28:5000/change_nick',
            data: {
              "account": response.data.account,
              "serial_number": response.data.serial_number,
              "nickname": itemNames[getRandomIntInclusive(0, itemNames.length - 1)]
            }
          }).then(function(response) {
            $scope.isLoading = false;
            $scope.purchases.unshift(response.data);
          });
          // $scope.purchases.unshift(response.data);
          // $scope.isAddNewItem = true;
        });
    };

    $scope.invalidateItem = function() {
      $scope.isShowPopup = false;
    };

    $scope.toggleSearch = function() {
      $scope.isSearch = !$scope.isSearch;
    };

    $scope.validateItem = function(isShowExistingProductInfo) {
      if (isShowExistingProductInfo === false) {
        $scope.isShowProductInfo = true;
      }
      $scope.isPhotoView = false;
    };

    $scope.purchases = [
      // {
      //   iconType: 'laptop',
      //   name: 'Macbook Pro 2017',
      //   timestamp: '5 Hours Ago',
      //   warrantyValidity: true
      // },
      // {
      //   iconType: 'phone',
      //   name: 'Samsung Galaxy S9+',
      //   timestamp: '6 Hours Ago',
      //   warrantyValidity: true
      // },
      // {
      //   iconType: 'watch',
      //   name: 'Fitbit Versa',
      //   timestamp: '5 Hours Ago',
      //   warrantyValidity: true
      // }
    ];

    $http({
      method: 'POST',
      url: '//10.101.2.28:5000/list',
      data: {
        "account": 'clara'
      }
    }).then(function(response) {
      $scope.isLoading = false;
      $scope.purchases = response.data;
    });

    $scope.registerItem = function() {
      $http({
        method: 'POST',
        url: '//10.101.2.28:5000/create',
        data: {
          "account": 'clara',
          "manufacturer": 'samsung',
          "serial_number": Math.round(Math.random()*200000000000),
          "length_of_warranty": getRandomIntInclusive(30, 730),
          "coverage": 'Service and Parts',
          "region": 'Hong Kong',
          "contact_details": '66712457',
          "remarks": ''
        }
      }).then(function(response) {
        $scope.isPhotoView = false;
        itemNames = ['Nokia 5110', 'iPhone 4', 'RAZER Phone', 'SONY Xperia XZ1'];
        $http({
          method: 'POST',
          url: '//10.101.2.28:5000/change_nick',
          data: {
            "account": response.data.account,
            "serial_number": response.data.serial_number,
            "nickname": itemNames[getRandomIntInclusive(0, itemNames.length - 1)]
          }
        }).then(function(response) {
          $scope.isLoading = false;
          $scope.purchases.unshift(response.data);
        });
        // $scope.purchases.unshift(response.data);
        // $scope.isAddNewItem = true;
      });
      $scope.isShowProductInfo = false;
    }

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
