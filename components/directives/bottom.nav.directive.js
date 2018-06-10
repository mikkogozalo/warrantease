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
    .directive('bottomNav', function() {
      return {
        restrict: 'E',
        templateUrl: 'components/directives/bottom-nav.html'
      };
    });
})();
