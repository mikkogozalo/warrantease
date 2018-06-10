;(function() {


  'use strict';

  /**
   * Responsive navigation
   *
   * Usage:
   * <responsive-nav></responsive-nav>
   *
   * Example in main-nav.html file
   *
   */
  angular.module('boilerplate')
    .directive('responsiveNav', function() {
      return {
        restrict: 'E',
        templateUrl: 'components/directives/responsive-nav.html',
        controller: 'MainController',
        link: function(scope, elem, attrs, ctrl) {
        	elem.on('click', function(e) {
        		$('.responsive-wrapper').slideToggle( 200, 'swing');
        	});
        }
      };
    });

})();
