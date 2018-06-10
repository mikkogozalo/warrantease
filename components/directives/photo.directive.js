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
    .directive('photo', function() {
      return {
        restrict: 'E',
        templateUrl: 'components/directives/photo.html',
        link: function(scope, element, attrs) {
          var btn = angular.element(element).find('.shutter-button');
          btn.click(function() {
            window.setTimeout(function() {
              angular.element('html').animate({
                  scrollTop: 0
              }, 2000);
            });
          });
        }
      };
    });
})();
