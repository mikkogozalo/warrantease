;(function() {

  'use strict';

  /**
   * Main navigation, just a HTML template
   * @author Jozef Butko
   * @ngdoc  Directive
   *
   * @example
   * <main-nav><main-nav/>
   *
   */
  angular
    .module('boilerplate')
    .directive('retailerView', function() {
      return {
        restrict: 'E',
        templateUrl: 'components/directives/retailer-view.html',
        controller: 'MainController'
      };
    });

})();
